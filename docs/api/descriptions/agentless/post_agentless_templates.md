Downloads a tarball file that contains the agentless resource permission templates for the cloud accounts. Apply these permission templates to complete the onboarding process for agentless scanning.

* AWS: The tarball contains templates in JSON format ending with the following names:
  * _aws_hub_target_user_permissions.json
  * _aws_hub_user_permissions.json
  * _aws_target_user_permissions.json

For more information on how to apply the permission templates, refer to the "Configure agentless scanning" section in the Prisma Cloud Compute administration guide.

* Azure: Use the following script, that comes bundled in the tarball file, to apply permission template to an Azure cloud account:
  * apply_azure_permissions.sh: Run the script with a location (that specifies location of the resource) parameter. For more information on location parameters, see [resource location in ARM template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/resource-location?tabs=azure-cli). 

* OCI: Use the following script, that comes bundled in the tarball file, to apply permission template to an OCI cloud account:
  * pcc-apply-permissions.sh: Run the script with a compartment name parameter.

* GCP: The tarball contains Jinja templates in YAML format ending with the following names:
  * _hub_target_access_permissions.yaml.jinja
  * _hub_target_user_permissions.yaml.jinja
  * _hub_user_permissions.yaml.jinja
  * _target_user_permissions.yaml.jinja

For more information on how to apply the permission templates, refer to the "Configure agentless scanning" section in the Prisma Cloud Compute administration guide.

**Note**: The body parameter `credentialID` is required to download templates in tar.gz format.

### Before you begin
Add the supported cloud accounts (AWS, Azure, GCP, and OCI) in Prisma Cloud Compute.

### cURL Request

Refer to the following example cURL command:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -O <agentlesstemplate.tar.gz> \
  -d {"credentialID":"aws_docs"} \
  “https://<CONSOLE>/api/v<VERSION>/agentless/templates”
```
