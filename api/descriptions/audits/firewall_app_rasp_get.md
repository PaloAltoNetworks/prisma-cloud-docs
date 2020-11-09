All of CNAF's capabilities are available to apps protected by RASP Defender.
This API endpoint retrieves all firewall audits for all RASP Defenders.
Audits are logged when there are violations to your CNAF for RASP policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/firewall/app/rasp
```

