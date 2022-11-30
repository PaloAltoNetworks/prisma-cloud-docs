Updates the registries to scan.
The list of registries to scan is updated in a single shot.

To invoke this endpoint in the Console UI:

1. Navigate to **Defend > Vulnerabilities > Images > Registry settings**.
2. Under the **Registries** table, add a registry item using **+ Add registry**
3. Click the **Save** button.

**Note**: From 22.11 (Lagrange) release or later, you can add a maximum of 19,999 registry entries in **Defend > Vulnerabilities > Images > Registry settings**. 

The API response returns an HTTP 400 error, if the number of registry specifications exceeds the maximum allowable limit of 19,999 registry entries.

### General Set up and Scan Process

This endpoint works hand-in-hand with the `/policies` endpoints.

**To set up a registry for scanning:**

1. Add your registry account information using this endpoint.

   For example, specify the location and credentials of an ECR registry in your AWS account.

2. Prisma Cloud auto-discovers the images in the registries specified with this endpoint.

3. The list of auto-discovered images is passed to the scanner for evaluation.

   The scanner uses the corresponding `/policies/vulnerability/images` and `/policies/compliance/images` endpoints to assess each image.


### cURL Request

Each registry to scan is specified as an item in the `specifications` array.

The critical fields for this endpoint are:

* `registry` - String specifying the registry URL.
* `credentialID` - String specifying the registry credential.
* `version` - String specifying the type of registry to scan and may be one of the following strings:

Version|Description
 ---|---
 `aws`|Amazon EC2 Container Registry
 `azure`|Azure Container Registry
 `2`|Docker Registry v2
 `dtr`|Docker Trusted Registry
 `gcr`|Google Container Registry
 `jfrog`|JFrog Artifactory
 `sonatype`|Sonatype Nexus
 `coreos`|CoreOS Quay
 `redhat`|Red Hat OpenShift
 `bluemix`|IBM Cloud Container Registry

The remaining fields in the `specifications` object (e.g., `repository`, `exclusions`, etc.) are optional.
They let you refine the scope of what Prisma Cloud auto-discovers.

**Note:** An empty string in `registry` implicitly refers to Docker Hub.
In `repository`, use the `library/` namespace to specify a [Docker official image](https://docs.docker.com/docker-hub/official_images/).
To see the current list of Docker official images, see [here](https://github.com/docker-library/official-images/tree/master/library).

#### Set up a Private Registry for Scanning

Most registries you'll configure for scanning will be private.
Prisma Cloud needs credentials to access private registries.
To set this up:

* Create the credentials with the `/credentials` endpoint.
* Retrieve the credential ID from the `/credentials` endpoint (`_id`).
* Create the registry setting with the recommended minimum required fields (`version`, `registry`, and `credentialID`).

#### Example cURL Request

The following cURL command overwrites the current list of registries to scan with two new registries:

* The official Ubuntu 18.04 image in Docker Hub
* All repositories in a private AWS ECR registry

```bash
$ curl 'https://<CONSOLE>/api/v1/settings/registry' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
  '{
    "specifications": [
      {
        "version": "2",
        "registry": "",
        "repository": "library/ubuntu",
        "tag": "18.04",
        "os": "linux",
        "cap": 5,
        "credentialID": "<CREDENTIAL_ID1>",
        "scanners": 2,
        "collections": ["All"]
      },
      {
        "version": "aws",
        "registry": "<ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com",
        "os": "linux",
        "credentialID": "<CREDENTIAL_ID2>",
        "scanners": 2,
        "cap": 5,
        "collections": ["All"]
      }
    ]
  }'
```

**Note:** No response will be returned upon successful execution.

### Remove a Registry

To remove a registry from the list:

1. Retrieve the current list using the GET method.
2. Remove the entry from the `specifications` JSON array in the response.
3. Use the PUT method to submit the updated JSON object.

To delete all entries, submit an empty `specifications` array. For example:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{"specifications":[]}' \
  https://<CONSOLE>/api/v1/settings/registry
```
