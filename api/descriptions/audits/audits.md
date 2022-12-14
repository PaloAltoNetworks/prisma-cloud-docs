Retrieve audits from the Prisma Cloud Compute database.
Prisma Cloud Compute creates and stores audit events for the components that are associated with a policy (rule) and shows deviation from that policy.
Endpoints support a wide range of filtering options.

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