import os
import boto3
from pathlib import Path

def upload_media():
    bucket = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    endpoint = os.environ.get('AWS_S3_ENDPOINT_URL')
    
    if not all([bucket, access_key, secret_key, endpoint]):
        print("Error: Missing R2 environment variables.")
        print("Required: AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_ENDPOINT_URL")
        return

    print("Connecting to Cloudflare R2...")
    s3 = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='auto'
    )
    
    media_dir = Path(__file__).resolve().parent.parent / 'backend' / 'media'
    print(f"Scanning media directory: {media_dir}")
    
    for file_path in media_dir.rglob('*'):
        if file_path.is_file():
            # Calculate the R2 key (relative path from media_dir)
            relative_path = file_path.relative_to(media_dir)
            r2_key = f"media/{relative_path.as_posix()}"
            
            print(f"Uploading {file_path.name} to R2 as '{r2_key}'...")
            try:
                s3.upload_file(
                    str(file_path),
                    bucket,
                    r2_key
                )
                print(f"✓ Uploaded {file_path.name} successfully.")
            except Exception as e:
                print(f"✗ Failed to upload {file_path.name}: {e}")

if __name__ == '__main__':
    upload_media()
