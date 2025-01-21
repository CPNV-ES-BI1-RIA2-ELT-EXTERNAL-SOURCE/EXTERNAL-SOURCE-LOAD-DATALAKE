from fastapi import APIRouter, HTTPException
from app.schemas.requests.job_request import JobRequest
from app.services.api_service import api_service
from app.services.environement_varriables import get_env_variables

router = APIRouter()

@router.post('/{job_id}')
def job(job_id: int, request: JobRequest):
    try:
        variables = get_env_variables(variables=["LOADER_API"])

        response = api_service(url=request.dataSource, method="GET")

        params = {
            "dataSource": response,
            "dataDestination": request.dataDestination,
        }

        response = api_service(
            url=variables["LOADER_API"],
            method="POST",
            params=params
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")
