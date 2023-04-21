Returns all activities that were alerted or blocked by Defender functioning as Open Policy Agent admission controller.

### cURL Request
Refer to the following example cURL command that gives a list of all admission audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/admission"

```
### cURL response

```
{
        "time": "2022-11-24T13:46:37.057Z",
        "ruleName": "Twistlock Labs - CIS - Pod created in host process ID namespace",
        "message": "Pod created in host process ID namespace",
        "operation": "CREATE",
        "kind": "Pod",
        "resource": "pods",
        "username": "kubernetes-admin",
        "userUid": "aws-iam-authenticator:496947949261:AIDAXHNDH53GRQMZMIOQT",
        "userGroups": "system:masters, system:authenticated",
        "namespace": "default",
        "effect": "alert",
        "rawRequest": "{\"uid\":\"78d11e35-14ab-4b19-b3d3-a97b4252b56f\",\"kind\":{\"group\":\"\",\"version\":\"v1\",\"kind\":\"Pod\"},\"resource\":{\"group\":\"\",\"version\":\"v1\",\"resource\":\"pods\"},\"requestKind\":{\"group\":\"\",\"version\":\"v1\",\"kind\":\"Pod\"},\"requestResource\":{\"group\":\"\",\"version\":\"v1\",\"resource\":\"pods\"},\"name\":\"nginx2\",\"namespace\":\"default\",\"operation\":\"CREATE\",\"userInfo\":{\"username\":\"kubernetes-admin\",\"uid\":...
    ...
    ...
    ...
}”,
        "accountID": "496947949261",
        "collections": [
            "All"
        ],
        "cluster": "johndoe-eks-123",
        "attackTechniques": [
            "privilegedContainer"
        ]
}

```