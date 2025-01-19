````mermaid
sequenceDiagram
    Actor API
    API ->>+ Server : load a json
    Server -)+ AwsService : connect()
    activate AwsService
    Server ->>- AwsService : load(json)
    AwsService ->>+ AwsSdk : put_object(json)
    activate AwsSdk
    AwsSdk -->>- AwsService : sdk response
    AwsService -->>- Server : response
````