
This is a stateless, serverless application.

# Installation

First you will need to install serverless globally:
```
brew install serverless -g
sls --help
```

handler.js - AWS used to describe function, actual Lambda function
serverless.yml - configuration for serverless framework
    service - names of lambda function to deploy
    provider - aws and environment
    functions - specify name and path for the lambda function   
    
    
# Test
To run a function on localstack use invoke command:
`sls invoke local -f hello`
 
    