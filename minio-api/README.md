## MinIO Service

### minio

```python
# Client example:
res = requests.post("http://127.0.0.1:5000/api/v1/getUploadFileUrl", json={"object_name": "abc.zip"})
data = open(file_path, "rb").read()
pre_signed_url = res.json().get("url")
headers = {"Content-Type":"application/binary",}
r = requests.put(pre_signed_url, data=data, headers=headers)

```
