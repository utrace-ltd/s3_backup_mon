# -*- coding: utf-8 -*-
import os
from datetime import datetime, timedelta
import re
from boto.s3.key import Key
from boto.s3.connection import S3Connection

# Yandex S3 settings.
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
AWS_STORAGE_URL = os.environ.get('AWS_STORAGE_URL')
AWS_AUTH_REGION_NAME = os.environ.get('AWS_AUTH_REGION_NAME')

conn = S3Connection(
    host=AWS_STORAGE_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

conn.auth_region_name = AWS_AUTH_REGION_NAME

bucket = conn.get_bucket(AWS_BUCKET_NAME)

k = Key(bucket)

keys_list = bucket.list()

date = datetime.now()
newdate = date - timedelta(days=1)
yesterday = ('{:%Y-%m-%d}'.format(newdate))

arr = []
i = 0
boolNum1 = ''

for key in keys_list:
    ssd = str(key.key)
    rgxs = bool(re.search(yesterday, ssd))
    i += 1
    if rgxs == bool(True):
        boolNum = 0
    else:
        boolNum = 1

    arr.append(
        {'id': i, 'boolNum': boolNum})

q = len(arr)

for q in range(0, q):
    boolNum1 = arr[q]['boolNum']
    if boolNum1 == 0:
        print('ok')
        break





