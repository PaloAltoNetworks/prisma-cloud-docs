The agentless security scan monitors hosts and containers for vulnerabilities and compliance risks by scanning the root volumes of snapshots without the need to install an agent. 
Supported cloud service provider platforms for agentless scanning:
* Hosts - Amazon AWS, Google Cloud Platform, Microsoft Azure, and Oracle Cloud Infrastructure. 
* Containers- AWS, Azure, and GCP

When you add a cloud account in the Prisma Cloud Compute (Manage > Cloud accounts), enable the agentless scan option and configure the scan scope.

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