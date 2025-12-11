AWS Explorer – Setup Mission

This repository documents the completion of the AWS Explorer Setup Mission. It includes the installation and configuration of boto3, the creation of an IAM user with appropriate permissions, the secure configuration of AWS credentials, and a Python script that lists all available AWS regions. Supporting evidence in the form of screenshots and configuration snippets is included as required.

1. Environment Setup

The project was developed in a Python virtual environment to ensure isolation from system-level packages.

Creating and activating the virtual environment
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate

Installing boto3
pip install boto3

2. IAM User Configuration

A dedicated IAM user was created in the AWS Management Console.

Steps undertaken:

Opened IAM → Users → Create User

Assigned the username aws-explorer-student

Attached the following AWS-managed policies:

AmazonEC2ReadOnlyAccess

AmazonS3ReadOnlyAccess

AmazonRDSReadOnlyAccess

Generated an access key for programmatic use, selecting the “Local code” option

Downloaded the key material for use in local development

A screenshot of the permission configuration is included in:

screenshots/iam_permissions.png

3. AWS Credentials Configuration

AWS credentials were stored in the standard configuration directory at:

~/.aws/

credentials file
[default]
aws_access_key_id = AKIA************
aws_secret_access_key = ********************

config file
[default]
region = ap-south-1
output = json


A redacted credentials snippet is included in:

screenshots/credentials_redacted.png





5. Script Execution Evidence

A screenshot of successful execution is included in the following location:

screenshots/script_output.png

6. Running the Script

To execute the script after setting up the environment:

source venv/bin/activate
python3 list_regions.py


The expected output is a printed dictionary containing the list of AWS regions and the submitter identifier.

7. Submission Summary

This repository includes:

A correctly configured Python environment

boto3 installed and functional

A securely configured IAM user and AWS credential setup

A working Python script that lists AWS regions

Screenshots demonstrating IAM permissions and script execution

Documentation fulfilling all requirements for the AWS Explorer Setup Mission

The repository may be submitted in the designated DevOps channel with the required task identifier.