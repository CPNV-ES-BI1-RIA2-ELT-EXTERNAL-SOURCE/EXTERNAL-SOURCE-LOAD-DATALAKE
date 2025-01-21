from pydantic import BaseModel

class JobResponse(BaseModel):
    dataSource: str