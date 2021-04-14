import boto3
import os
import datetime
import schedule

##defaults
default_path = "/home/deity/Documents/C++"
default_interval = 1
default_access_key_id = "AKIA5DAV65HJUPYKB5MM"
default_access_key = 'CtGmDfCJVlrZEvcq9Q6kMMFfLABm6hVCVXAHcPfc'
default_bucket_name = 'backup-test-101803645'



## I/o
print(" Hello Welcome to your personal backup service,\n Your backup will be stored and managed over AWS S3 ")
print("##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<##")
print("Please provide a path to the directory that you want to backup other wise default path will be taken:")
temp = input()
path = default_path if temp == "" else temp
print("Enter time interval (in hours) for recreating backup")
tmep = input()
interval = default_interval if temp == "" else temp
print("Enter access key id")
temp = input()
access_key_id = default_access_key_id if temp == "" else temp
print("enter access key ")
temp = input()
access_key = default_access_key if temp == "" else temp
print("enter Bucket name")
temp = input()
bucket_name = default_bucket_name if temp == "" else temp



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

schedule.every(interval).hour.do(upload_files(path))
while True:
    schedule.run_pending()

# if __name__ == "__main__":
#     upload_files("/home/deity/Documents/C++")