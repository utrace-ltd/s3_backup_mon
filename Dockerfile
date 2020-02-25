FROM python:3

WORKDIR /opt/s3_backup_mon

RUN python -m pip install --upgrade pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY s3_backup_mon.py ./

ENV AWS_ACCESS_KEY_ID='your_access_key_for_aws'
ENV AWS_SECRET_ACCESS_KEY='your_secret_access_key_for_aws'
ENV AWS_BUCKET_NAME='your_aws_bucket_name'
ENV AWS_STORAGE_URL='s3-storage.example.com'
ENV AWS_AUTH_REGION_NAME='example-region'

CMD [ "python", "s3_backup_mon.py" ]
