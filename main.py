import os
from app.Server import Server
from app.cloud_services.aws_service import AwsService

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION")
AWS_DESTINATION = os.getenv("AWS_DESTINATION", "")

server = Server(AwsService(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, AWS_REGION, AWS_DESTINATION))
server.start()
