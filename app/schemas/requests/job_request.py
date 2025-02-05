from pydantic import BaseModel

class JobRequest(BaseModel):
    dataSource: str
    dataDestination: str
