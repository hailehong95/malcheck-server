from datetime import timedelta
from malcheck_dash.models import Users
from malcheck_dash.logging import logger
from malcheck_dash.utils import dash_send_telegram
from malcheck_dash.config import app, db, client, auth, users
from flask import jsonify, make_response, request, render_template
from malcheck_dash.config import MINIO_BUCKET_NAME as bucket_name


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/')
@auth.login_required
def index():
    return render_template('server_table.html', title='MalCheck Dash!')


@app.route('/api/v1/data')
def data():
    try:
        query = Users.query

        # search filter
        search = request.args.get('search[value]')
        if search:
            query = query.filter(db.or_(
                Users.name.like(f'%{search}%'),
                Users.emp_id.like(f'%{search}%')
            ))
        total_filtered = query.count()

        # sorting
        order = []
        i = 0
        while True:
            col_index = request.args.get(f'order[{i}][column]')
            if col_index is None:
                break
            col_name = request.args.get(f'columns[{col_index}][data]')
            if col_name not in ['name', 'address', 'emp_id']:
                col_name = 'name'
            descending = request.args.get(f'order[{i}][dir]') == 'desc'
            col = getattr(Users, col_name)
            if descending:
                col = col.desc()
            order.append(col)
            i += 1
        if order:
            query = query.order_by(*order)

        # pagination
        start = request.args.get('start', type=int)
        length = request.args.get('length', type=int)
        query = query.offset(start).limit(length)

        # response
        return {
            'data': [users.to_dict() for users in query],
            'recordsFiltered': total_filtered,
            'recordsTotal': Users.query.count(),
            'draw': request.args.get('draw', type=int),
        }
    except Exception as ex:
        pass


# Get Pre-signed URLs
@app.route('/api/v1/upload', methods=['POST'])
def user_get_upload_url():
    try:
        request_data = request.get_json()
        object_name = request_data["object_name"]
        if object_name is not None:
            url = client.presigned_put_object(bucket_name, object_name, expires=timedelta(hours=1))
            return make_response(jsonify({"url": url}), 200)
    except Exception as ex:
        logger.info(str(ex))


# Users register/checkin
@app.route('/api/v1/checkin', methods=['POST'])
def user_checkin():
    try:
        request_data = request.get_json()
        status = "Scanning"
        name = request_data.get("name")
        emp_id = request_data.get("emp_id")
        address = request_data.get("address")
        signature = request_data.get("signature")
        platform_os = request_data.get("platform_os")
        item = Users(address=address, emp_id=emp_id, name=name, platform_os=platform_os, status=status,
                     signature=signature)
        db.session.add(item)
        db.session.commit()
        return make_response(jsonify({"message": "successful"}), 200)
    except Exception as ex:
        logger.info(str(ex))


# Users finish/checkout
@app.route('/api/v1/checkout', methods=['POST'])
def user_checkout():
    try:
        request_data = request.get_json()
        name = request_data.get("name")
        emp_id = request_data.get("emp_id")
        address = request_data.get("address")
        signature = request_data.get("signature")
        dash_send_telegram(f"{address} - {emp_id} - {name}")
        item = Users.query.filter_by(emp_id=emp_id, signature=signature, status="Scanning").first()
        item.status = "Successful"
        db.session.commit()
        return make_response(jsonify({"message": "successful"}), 200)
    except Exception as ex:
        logger.info(str(ex))
