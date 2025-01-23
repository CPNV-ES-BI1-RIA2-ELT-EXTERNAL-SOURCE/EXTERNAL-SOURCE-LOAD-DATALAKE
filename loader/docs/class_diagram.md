````mermaid
classDiagram
    EnvironmentVariableException
    class EnvironmentVariableException {
        EnvironmentVariableException()
    }
    
    DestinationNotFoundException
    class DestinationNotFoundException {
        DestinationNotFoundException()
    }
    
    JobRequest <|-- BaseModel
    class JobRequest {
    + dataSource: str
    + dataDestination: str
    }
    
    JobResponse <|-- BaseModel
    class JobResponse {
    + dataSource: str
    }
````