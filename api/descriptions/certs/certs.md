Retrieve and manage the client and server certificates from the Prisma Cloud Compute.

### Authentication 

#### Basic Auth
##### Headers
 - Authorization: required (string): Authenticates with the Base64-encoded "username:password" credentials.

#### JWT Access Token
Use POST, /api/vVERSION/authenticate for authorization
##### Headers
 - Authorization: required (string): Authenticates with the Bearer authentication scheme to transmit the access token.
    Example:
    Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJk…………
