from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import boto3

app = Flask(__name__)
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AWS_REGION = os.getenv('AWS_REGION')

# Function to scan text files for errors and write them to the output file
def scan_logs(log_files, output_file):
    with open(output_file, 'w') as output:
        for log_file in log_files:
            with open(log_file, 'r') as file:
                for line in file:
                    if 'error' in line.lower():
                        output.write(line)

# Function to upload file to S3 with explicit AWS credentials
def upload_to_s3(file_name, object_name):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    s3.upload_file(file_name, AWS_BUCKET_NAME, object_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    # Create the 'uploads' directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    uploaded_files = request.files.getlist('files')
    output_file = 'output.txt'
    log_files = []

    # Save uploaded files locally
    for file in uploaded_files:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        log_files.append(file_path)

    # Merge all error logs from multiple input files into a single output file
    scan_logs(log_files, output_file)

    # Upload output file to S3
    upload_to_s3(output_file, output_file)

    # Return download link for the output file
    s3_download_link = f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{output_file}"
    return render_template('result.html', download_link=s3_download_link)

if __name__ == '__main__':
    app.run(debug=True)
