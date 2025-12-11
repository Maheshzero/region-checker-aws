import boto3

def list_aws_regions():
    ec2 = boto3.client("ec2")
    regions = ec2.describe_regions()["Regions"]
    return [region["RegionName"] for region in regions]

if __name__ == "__main__":
    print({
        "regions": list_aws_regions(),
        "submitted_by": "maheshs-1@mulearn"
    })
