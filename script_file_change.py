
## main function

def upload_files(path):
    logs = open("logs.txt", "a")
    logs.write(f"Starting Backup for path {path} at {datetime.datetime.now}")
    session = boto3.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=access_key
    )
    logs.write("Session created Successfully")
    s3 = session.resource('s3')
    bucket = s3.Bucket('backup-test-101803645')
    logs.write("bucket {bucket} opened")
    
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            logs.write(f"opening {full_path}")
            # print(full_path)
            with open(full_path, 'rb') as data:
                log = bucket.put_object(Key=full_path[len(path)+1:], Body=data)
                logs.write(str(log))
                print(log)