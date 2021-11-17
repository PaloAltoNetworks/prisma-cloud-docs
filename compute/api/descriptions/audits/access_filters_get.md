Retrieves all access audits by specific host filters. 
There are three types of host filters based on host history, sudo events on host and SSHD events on hosts.

The following example uses basic auth to list history of commands that are run on hosts protected by Prisma Cloud Compute.


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/history/host
```

The following command gives list of sudo events on hosts. 


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/access/filters?type=sudo

```

The following command gives list of SSHD events on hosts. 

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/access/filters?type=sshd

```

