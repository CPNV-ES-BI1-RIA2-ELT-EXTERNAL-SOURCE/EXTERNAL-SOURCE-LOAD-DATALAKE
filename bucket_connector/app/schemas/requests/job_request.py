from pydantic import BaseModel

class JobRequest(BaseModel):
    data: any
    dataDestination: str
