from s3fs import S3FileSystem


def connect(key: str, secret: str) -> S3FileSystem:
    """Create a Boto3 client for S3 service."""
    filesystem = S3FileSystem(key=key, secret=secret)
    # filesystem.ls('my-bucket')
    return filesystem

def save_data(filesystem: str, bucket: str, data: str) -> dict:
    """saves the data received from AI Service"""
    with filesystem.open(bucket, 'w') as f:  #bucket = 'myaiops/aidata'
        f.write(data)
    filesystem.du(bucket)
