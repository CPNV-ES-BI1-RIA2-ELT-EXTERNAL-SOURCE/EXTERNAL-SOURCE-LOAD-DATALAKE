````mermaid
sequenceDiagram
    Actor API
    API ->>+ main : 
    main ->>+ jobs : 
    activate jobs
    jobs ->>+ getEnvVariables : get env variables
    activate getEnvVariables
    getEnvVariables -->>- jobs : array of variables
    jobs ->>+ apiCall : GET 
    apiCall -->>- jobs : response 
    
    jobs ->>+ apiCall : POST
    apiCall -->>- jobs : response 
    
    main -->>- API : 
    
````