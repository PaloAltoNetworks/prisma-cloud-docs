This api call gives a list of incident categories found in your environment.

The following example uses basic auth to list incident filters.

```bash
$ curl -k \
  -u <USER> \
  https://console:8083/api/v1/audits/incidents/filters
```

Response:

```
{"hostname":["aqsa-lab.internal"],"category":["hijackedProcess","dataExfiltration"]}
```
