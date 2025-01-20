from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from app.cloud_services.aws_service import AwsService
from app.cloud_services.cloud_service import CloudService
from app.services.environement_varriables import get_env_variables

router : APIRouter = APIRouter()
_VERSION : str = "v1"

@router.post("/" + _VERSION + "/object")
async def load_content(
    bucket_name: str = Form(...),
    bucket_destination: str = Form(...),
    object: UploadFile = File(...)
):

    try:
        variables = get_env_variables(variables=["AWS_ACCESS_KEY", "AWS_SECRET_KEY", "AWS_REGION"])

        service = AwsService(
            access_key=variables["AWS_ACCESS_KEY"],
            secret_key=variables["AWS_SECRET_KEY"],
            region=variables["AWS_REGION"],
            bucket=bucket_name,
            destination=bucket_destination
        )

        service.connect()

        service.load(object=object)

        # TODO : should response with the url of the object or an error.

        return {}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")
