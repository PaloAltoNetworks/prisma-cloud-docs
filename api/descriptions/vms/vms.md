Scan VM images in AWS, Azure, and GCP for vulnerabilities.

Prisma Cloud can scan the following VM images:
* AWS: Linux Amazon Machine Images (AMIs)
* Azure: Managed, Gallery and Marketplace images
* GCP: Public and Custom images (including Premium images)

For more information, see [Configure VM Image Scanning](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/vulnerability_management/vm_image_scanning)

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
