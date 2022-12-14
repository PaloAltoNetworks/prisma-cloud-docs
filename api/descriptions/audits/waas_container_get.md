Retrieves all container Web-Application and API Security (WAAS) audits. 

**Note:** These audit events relate to violations of WAAS policies defined under **Defend > WAAS > Container > Container WAAS Policy**.

### cURL Request
Refer to the following example cURL command that retrieves all container WAAS audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/container"

```

### cURL Response
```
{
    "_id": "636aa20ca5eab1d485abc519",
    "profileId": "sha256:a9301dac5a66b3f54a324b9ee737c64a1cc68d2186d8082df82755fb6d551a06_waas_k8s-v1-23-13-docker-20-10-21-kube-ssugandh-2b19f07bd1e31534",
    "time": "2022-11-08T18:38:04Z",
    "hostname": "kube-ssugandh-2b19f07bd1e31534-k8s-worker-1",
    "fqdn": "",
    "effect": "alert",
    "ruleName": "k8s-7878_384_kubernetes",
    "ruleAppID": "zhdmrlnr",
    "msg": "Detected Local File Inclusion attack in request body, match ../, value ../../",
    "host": false,
    "containerName": "/k8s_mock-web-service-36666_mock-web-service-32001_waas_52d3dccd-44b4-48fa-b149-60835b47c614_0",
    "containerId": "22c03ede91779978eb664c03189e3b69432e754b984dd9be203e7567fc6461ba",
    "imageName": "doctwistlock/waas-mock-service:latest",
    "appID": "",
    "type": "lfi",
    "count": 1,
    "region": "us-central1-a",
    "version": "22.11.384",
    "accountID": "twistlock-test-247119",
    "url": "10.180.31.40:32001/",
    "userAgentHeader": "python-requests/2.27.1",
    "method": "POST",
    "urlPath": "/",
    "subnet": "10.180.31.40",
    "requestHeaders": "POST / HTTP/1.1\r\nHost: 10.180.31.40:32001\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nContent-Length: 6\r\nUser-Agent: python-requests/2.27.1\r\n",
    "requestHost": "10.180.31.40:32001",
    "requestHeaderNames": [
      "Accept",
      "Accept-Encoding",
      "Connection",
      "Content-Length",
      "User-Agent"
    ],
    "responseHeaderNames": [
      "Content-Length",
      "Content-Type",
      "Date",
      "Server"
    ],
    "statusCode": 404,
    "collections": [
      "All",
      "Prisma Cloud resources"
    ],
    "os": "Ubuntu 20.04.5 LTS",
    "ns": [
      "waas"
    ],
    "resource": {
      "images": [
        "doctwistlock/waas-mock-service:latest"
      ],
      "namespaces": [
        "waas"
      ],
      "accountIDs": [
        "twistlock-test-247119"
      ]
    },
    "cluster": "k8s-v1-23-13-docker-20-10-21-kube-ssugandh-2b19f07bd1e31534",
    "attackTechniques": [
      "exploitPublicFacingApplication",
      "applicationExploitRCE"
    ],
    "protection": "firewall",
    "attackField": {
      "value": "../../",
      "type": "rawBody"
    },
    "eventID": "dc2fb804-27b1-40f4-6b73-ae54783c548a",
    "provider": "gcp"
  },
  ...
  ...
  ...

}

```
