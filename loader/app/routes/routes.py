from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from app.services.environement_varriables import get_env_variables
from app.services.api_service import (api_service)

router : APIRouter = APIRouter()
_VERSION : str = "v1"
_bucket_destination = "/"

@router.post("/" + _VERSION + "/raw-object")
async def load_content(
    dataSource: str = Form(...),
    dataDestination: str = Form(...)
):
    try:
        variables = get_env_variables(variables=["LOADER_API"])

        response = api_service(url=dataSource, method="GET")

        params = {
            "dataSource": response,
            "dataDestination": dataDestination,
        }

        response = api_service(
            url=variables["LOADER_API"],
            method="POST",
            params=params
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")
