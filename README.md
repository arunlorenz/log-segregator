# Log File Scanner and Uploader
This Flask application allows users to upload text files, scans them for errors, and uploads the merged error logs to Amazon S3. It provides a simple interface for file upload and displays a download link for the merged error logs.

## Prerequisites
- Python installed on your system
- An Amazon S3 bucket set up for storing files
- Flask, Boto3, and python-dotenv Python packages installed

## Installation
1. Clone the repository to your local machine:

    ```bash
    git clone <repository_url>

2. Navigate to the project directory:
    
    ```bash
    cd log-file-scanner-uploader

3. Install dependencies:

    ```bash
    pip install flask boto3 python-dotenv

## Configuration
1. Create a .env file in the project directory and add the following variables:

    ```plaintext
    Copy code
    AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
    AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
    AWS_BUCKET_NAME=<your_s3_bucket_name>
    AWS_REGION=<your_aws_region>

Replace your_aws_access_key_id, your_aws_secret_access_key, your_s3_bucket_name, and your_aws_region with your actual AWS credentials and bucket information.

## Usage
1. Start the Flask server:
    ```bash
    python app.py
2. Access the application in your web browser:

    ```arduino
    http://localhost:5000/
3. Upload text files containing logs using the provided form.

4. After upload, the application will scan the files for errors and merge them into a single output file.

5. The merged error logs will be uploaded to Amazon S3, and a download link will be provided.

## Notes
- Uploaded files are saved locally in the 'uploads' directory.
- Error logs are searched case-insensitively for the term 'error'.
- Ensure that your S3 bucket has the necessary permissions for uploading and downloading files.

## License
This project is licensed under the MIT License
