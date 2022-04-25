Retrieves a list of all WAAS network lists.
Network lists are groups or related IPv4 addresses and CIDR blocks used in WAAS policy rules.

This endpoint is typically called as part of a process to programmatically update network lists based on new threat intelligence.
For example: add, update, or delete IP addresses.

This endpoint maps to **Defend > WAAS > Network lists** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/network-list'
```

A successful response returns the lists of IPv4 addresses/IP CIDR blocks for networks in WAAS.
