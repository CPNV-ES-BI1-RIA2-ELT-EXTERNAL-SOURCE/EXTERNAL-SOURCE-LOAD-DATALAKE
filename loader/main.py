import os
import uvicorn
from src.Server import Server
from src.cloud_services.aws_service import AwsService

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION")
AWS_DESTINATION = os.getenv("AWS_DESTINATION", "")

def main():
    server = Server(AwsService(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, AWS_REGION, AWS_DESTINATION))
    server.start()

    uvicorn.run(server.app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()