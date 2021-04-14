import boto3
import os
import datetime
def upload_files(path):
    session = boto3.Session(
        aws_access_key_id='AKIA5DAV65HJUPYKB5MM',
        aws_secret_access_key='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'
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('backup-test-101803645')
    print(bucket.name)
    print(path)
    print(os.walk(path))
    for root in os.walk(path):
        print(root)
    for subdir, dirs, files in os.walk(path):
        print("in")
        for file in files:
            full_path = os.path.join(subdir, file)
            print(full_path)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
                print(full_path)



if __name__ == "__main__":
    upload_files("/home/deity/Documents/C++")