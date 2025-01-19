from botocore.exceptions import ClientError

from src.cloud_services.cloud_service import CloudService
from src.exceptions.authentication_failed_exception import AuthenticationFailedException
from src.exceptions.destination_not_found_exception import DestinationNotFoundException
from src.exceptions.object_alread_exist_exception import ObjectAlreadyExistException

from src.objects.object import Object
import boto3


class AwsService(CloudService):

    _destination_name : str
    _access_key : str
    _secret_key : str
    _bucket : str
    _region_name : str
    _connection : boto3

    def __init__(self, access_key : str, secret_key : str, bucket : str, region : str, destination: str) -> None:
        self._access_key = access_key
        self._secret_key = secret_key
        self._bucket = bucket
        self._region_name = region
        self._destination_name = destination


    def connect(self) -> None:
        try:
            self._connection = boto3.client('s3',
                                            aws_access_key_id=self._access_key,
                                            aws_secret_access_key=self._secret_key,
                                            region_name=self._region_name)

        except Exception as e:
            raise AuthenticationFailedException("Authentication has failed!")

    def disconnect(self) -> None:
        self._connection.Client.close()

    def load(self, source: any) -> None:
        print(source)

        try:
            self._connection.put_object(
                Bucket=self._bucket,
                Key=self._destination_name,
                Body=source
            )
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'NoSuchBucket':
                raise DestinationNotFoundException("Destination not found!")
            if error_code == 'PreconditionFailed':
                raise ObjectAlreadyExistException("Object already exists!")