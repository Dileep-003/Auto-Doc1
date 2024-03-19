# main.tf

provider "aws" {
  region = var.region 
}

resource "aws_iam_user" "user" {
  name = var.user_name
}

resource "aws_iam_access_key" "user" {
  user = aws_iam_user.user.name
}

resource "aws_iam_user_policy" "allow_s3_access" {
  name = "allow-s3-access"
  user = aws_iam_user.user.name

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
  })
}

resource "aws_s3_bucket" "data_upload" {
  bucket = "my-data-upload-bucket"
  acl    = "private"

  tags = {
    Name        = "My data upload bucket"
  }
}
