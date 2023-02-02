from minio_api.config import app
from minio_api.logging import logger
from flask import jsonify, make_response


# Get Pre-signed URLs
@app.route('/api/v1/getUploadFileUrl', methods=['GET'])
def get_upload_file_url():
    try:
        # http://127.0.0.1:5000/api/v1/getUploadFileUrl
        mess = {"message": "hello world!"}
        return make_response(jsonify(mess), 200)
    except Exception as ex:
        logger.info(str(ex))
