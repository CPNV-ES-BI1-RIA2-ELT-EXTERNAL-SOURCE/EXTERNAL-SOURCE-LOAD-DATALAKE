import json
from fastapi import APIRouter, HTTPException
from app.schemas.requests.job_request import JobRequest
from app.schemas.responses.job_response import JobResponse
from app.services.api_service import api_call
from app.services.environement_varriables import get_env_variables

router = APIRouter()

@router.post('/{job_id}', response_model=JobResponse)
def job(job_id: int, request: JobRequest):
    try:
        variables = get_env_variables(variables=["LOADER_API"])

        response = api_call(url=request.dataSource, method="GET")

        data = {
            "data": response,
            "dataDestination": request.dataDestination,
        }

        response = api_call(
            url=variables["LOADER_API"],
            method="POST",
            data=data
        ).replace("\"", "")
        return JobResponse(dataSource=response)

    //TODO Check API framwork best practices
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")
