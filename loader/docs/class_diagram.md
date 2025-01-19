````mermaid
classDiagram
    class CloudService {
        <<Interface>>        
        + connect() void
        + disconect() void
        + load(source : any) void
    }
    
    CloudService <|-- GcpService
    class GcpService {
        - connectionString : string
        - destinationName : string
        - connection : SdkGcp

        + GcpService(connectionString : string, destinationName : string)
        + connect() void 
        + disconect() void
        + load(source : any) void        
    }
    
    CloudService <|-- AwsService
    class AwsService {
        - connectionString : string
        - destinationName : string
        - access_key : string
        - secret_key : string
        - bucket : string
        - region_name : string
        - connection : SdkAws

        + AwsService(access_key : string, secret_key : string, bucket : string, region : string, destination: string)
        + connect() void 
        + disconect() void
        + load(source : any) void        
    }
    
    CloudService <-- Server
    class Server {
        - app : FastApi
        - service : CloudService

        Server(service : CloudService)
        + start() void
        + stop() void
    }
    
    DestinationNotFoundException <-- CloudService
    class DestinationNotFoundException {
        DestinationNotFoundException()
    }
    
    ObjectAlreadyExistException <-- CloudService
    class ObjectAlreadyExistException {
        ObjectAlreadyExistException()
    }
    
    AuthenticationFailedException <-- CloudService
    class AuthenticationFailedException {
        AuthenticationFailedException()
    }

    GcpService --() SdkGcp
    Server --() FastApi
    
````