from datetime import timedelta
from minio_api.logging import logger
from minio_api.config import app, client
from minio_api.utils import malcheck_send_telegram
from flask import jsonify, make_response, request
from minio_api.config import MINIO_BUCKET_NAME as bucket_name


# Get Pre-signed URLs
@app.route('/api/v1/getUploadFileUrl', methods=['POST'])
def get_upload_file_url():
    try:
        request_data = request.get_json()
        object_name = request_data["object_name"]
        if object_name is not None:
            url = client.presigned_put_object(bucket_name, object_name, expires=timedelta(hours=1))
            malcheck_send_telegram(object_name)
            return make_response(jsonify({"url": url}), 200)
    except Exception as ex:
        logger.info(str(ex))
