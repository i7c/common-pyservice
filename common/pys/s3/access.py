

def load(s3_client, bucket: str, key: str) -> bytes:
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        return response['Body'].read()
    except s3_client.exceptions.NoSuchKey:
        return None


def write(s3_client, bucket: str, key: str, content: bytes):
    s3_client.put_object(Bucket=bucket, Key=key, Body=content)


def delete_object(s3_client, bucket: str, key: str):
    s3_client.delete_object(Bucket=bucket, Key=key)
