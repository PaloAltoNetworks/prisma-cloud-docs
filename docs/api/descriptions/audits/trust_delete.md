Deletes all the trust audits from the events page in Console.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/audits/trust
```
