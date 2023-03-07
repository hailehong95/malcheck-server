#!/usr/bin/env python

from minio_api.config import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
