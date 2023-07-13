Specifies a single registry to scan.

Each registry to scan is specified as an item in the `specifications` array.
The POST method appends an entry to the `specifications` array.
In contrast, the PUT method adds all registries in a single shot, completely overwriting any previous configuration by replacing the contents of the `specifications` array.
For more information about the `specifications` array, see the GET endpoint.

The `version` string specifies the type of registry to scan.
It can be one of the following strings:

* Amazon EC2 Container Registry: `aws`
* Azure Container Registry: `azure`
* Docker Registry v2: `2`
* Docker Trusted Registry: `dtr`
* Google Container Registry: `gcr`
* JFrog Artifactory: `jfrog`
* Sonatype Nexus: `sonatype`
* CoreOS Quay: `coreos`
* Red Hat OpenShift: `redhat`
* IBM Cloud Container Registry: `bluemix`

**Note**: From 22.11 (Lagrange) release or later, you can add a maximum of 19,999 registry entries in **Defend > Vulnerabilities > Images > Registry settings**. 

The API response returns an HTTP 400 error, if the number of registry specifications exceeds the maximum allowable limit of 19,999 registry entries.

Refer to the following example cURL command,
that configures Prisma Cloud Compute to scan the Ubuntu 16.04 repository on Docker Hub:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '
  {
    "version": "2",
    "registry": "",
    "repository": "library/ubuntu",
    "tag": "16.04",
    "os": "linux",
    "cap": 5,
    "hostname": "",
    "scanners": 2,
    "collections": ["All"]
  } ' \
  'https://<CONSOLE>/api/v<VERSION>/settings/registry'
```
