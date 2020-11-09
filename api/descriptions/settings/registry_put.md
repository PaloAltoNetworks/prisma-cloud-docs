Specifies the registries to scan.
The list of registries is set in a single shot.
Any previous settings are completely overwritten.

Each registry to scan is specified as an item in the `specifications` array.

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

The following example curl command configures Twistlock to scan the Ubuntu 18.04 and Alpine 3.10 images in Docker Hub.

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '
  {
    "specifications": [
      {
        "version": "2",
        "registry": "",
        "repository": "library/ubuntu",
        "tag": "18.04",
        "os": "linux",
        "cap": 5,
        "hostname": "",
        "scanners": 2
      },
      {
        "version": "2",
        "registry": "",
        "repository": "library/alpine",
        "tag": "3.10",
        "os": "linux",
        "cap": 5,
        "hostname": "",
        "scanners": 2
      }
    ]
  } ' \
  https://<CONSOLE>:8083/api/v1/settings/registry
```

To remove a registry from the list, retrieve the current list using the GET method.
Then remove the entry from the `specifications` array, and PUT the updated JSON object.

To delete all entries, submit an empty `specifications` array:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{"specifications":[]}' \
  https://<CONSOLE>:8083/api/v1/settings/registry
```
