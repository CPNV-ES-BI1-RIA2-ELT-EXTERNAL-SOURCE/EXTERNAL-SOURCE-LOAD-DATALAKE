from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from app.cloud_services.aws_service import AwsService
from app.cloud_services.cloud_service import CloudService
from app.services.environement_varriables import get_env_variables

from loader.app.api_handler import APIHandler

from loader.app.services.request import api_service

router : APIRouter = APIRouter()
_VERSION : str = "v1"

@router.post("/" + _VERSION + "/raw-object")
async def load_content(
    bucket_name: str = Form(...),
    bucket_destination: str = Form(...),
    object_url: str = Form(...)
):
    try:
        variables = get_env_variables(variables=["LOADER_API"])
        params={
            "url": object_url,
        }

        response = api_service(url=object_url, method="GET", params=params)

        params = {
            "object": response,
            "bucket_name": bucket_name,
            "bucket_destination": bucket_destination,
        }

        response = api_service(
            url=variables["LOADER_API"],
            method="POST",
            params=params
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")
