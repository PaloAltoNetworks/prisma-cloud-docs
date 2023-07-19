Specifies a single registry to scan.

Each registry to scan is specified as an item in the `specifications` array.
The POST method appends an entry to the `specifications` array.
In contrast, the PUT method adds all registries in a single shot, completely overwriting any previous configuration by replacing the contents of the `specifications` array.
For more information about the `specifications` array, see the GET endpoint.

The `version` string specifies the type of registry to scan.
It can be one of the following strings:

* Amazon EC2 Container Registry: `aws`
* Azure Container Registry: `azure`
* CoreOS Quay: `coreos`
* Docker Registry v2: `2`
* Docker Trusted Registry: `dtr`
* Google Container Registry: `gcr`
* GitLab Container Registry: `gitlab`
* IBM Cloud Container Registry: `bluemix`
* JFrog Artifactory: `jfrog`
* Red Hat OpenShift: `redhat`
* Sonatype Nexus: `sonatype`


**Note**: From 22.11 (Lagrange) release or later, you can add a maximum of 19,999 registry entries in **Defend > Vulnerabilities > Images > Registry settings**. 

The API response returns an HTTP 400 error, if the number of registry specifications exceeds the maximum allowable limit of 19,999 registry entries.

**cURL Request**

Refer to the following example cURL command that configures Prisma Cloud Compute to scan the Ubuntu 16.04 repository on Docker Hub:

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

Starting with 30.03, you can directly add a GitLab Container Registry.
To add settings for a GitLab Container Registry, you must specify the following parameters:

* **version**:  Specify the value *gitlab* for GitLab Container Registry.
* **registry**: Specify the GitLab registry URL address. Example, for native registries, you can specify the address as "https://registry.gitlab.com" 
* **credentialID**: Specify the GitLab credential that you added in the credential store in Prisma Cloud Compute. For example, an API token that has atleast the *read_api* scope.
* **gitlabRegistrySpec**: Specify at least one of the following fields:
    * **userID**: Specify your GitLab user ID to add all registries associated with it.
    * **projectIDs**: Specify the project IDs to add all registries associated with a GitLab project.
    * **groupIDs**: Specify the group ID to add all registries associated with a GitLab group.
    * **excludedGroupIDs**: Specify the top-level group IDs that you don't want to add.

Refer to the following example cURL command:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '
  {
    "version":"gitlab",
    "registry":"https://registry.gitlab.com",
    "namespace":"",
    "repository":"",
    "tag":"",
    "credentialID":"<Credential ID from Credential Store>",
    "os":"linux",
    "harborDeploymentSecurity":false,
    "collections":["All"],
    "cap":5,
    "scanners":2,
    "versionPattern":"",
    "gitlabRegistrySpec":{"userID":"14631394"}
  } ' \
  'https://<CONSOLE>/api/v<VERSION>/settings/registry'
```