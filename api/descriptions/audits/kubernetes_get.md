Retrieves events that occur in an integrated Kubernetes cluster that you configured for Prisma Cloud Compute under **Defend > Access > Kubernetes**.

**Note:** This endpoint relates to the **Monitor > Events > Kubernetes** audits in Prisma Cloud Compute.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/kubernetes"
```

### cURL Response

```
{
        "time": "2022-11-23T16:20:20.383Z",
        "verb": "io.k8s.core.v1.pods.exec.create",
        "user": {
            "username": "johndoe@paloaltonetworks.com"
        },
        "authorizationInfo": {
            "authorization.k8s.io/decision": "allow",
            "authorization.k8s.io/reason": "access granted by IAM permissions.",
            "failed-open.validating.webhook.admission.k8s.io/round_0_index_0": "validating-webhook.twistlock.com"
        },
        "message": "Exec or attach to a pod detected on GKE",
        "sourceIPs": [
            "private"
        ],
        "resources": "core/v1/namespaces/default/pods/test-pd/exec",
        ...
        ...
        ...,
        "attackTechniques": [
            "execIntoContainer"
        ],
        "cluster": "johndoe-gke-9916911d51921853",
        "accountID": "twistlock-test-247119",
        "provider": "gcp",
        "collections": [
            "All",
            "user1",
            "tv test",
            "tv test2"
        ]
    }


```

