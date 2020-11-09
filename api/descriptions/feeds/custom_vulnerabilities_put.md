Updates all custom vulnerability rules in a single shot.

The following example curl command defines a vulnerability for a library named internal-lib, where it's known that versions 1.1 to 1.8 are vulnerable.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d \
'{
  "rules": [
    {
      "_id": "",
      "package": "internal-lib",
      "type": "package",
      "minVersionInclusive": "1.1",
      "name": "internal-lib",
      "maxVersionInclusive": "1.8",
      "md5": ""
    }
  ]
}' \
  https://<CONSOLE>:8083/api/v1/feeds/custom/custom-vulnerabilities
```

The procedure to maintain your custom vulnerabilities is:

1. Get all custom vulnerability rules from the GET endpoint and save the results to a file.

   ```
   $ curl -k \
     -u <USER> \
     https://<CONSOLE>:8083/api/v1/feeds//custom/custom-vulnerabilities \
     | jq '.' > custom_vulnerability_rules.json
   ```

2. Add, modify, and/or delete rules by directly editing the JSON output.

3. Update your rules by pushing the new JSON payload.
Do not forget to specify the `@` symbol.

   ```
   $ curl -k \
     -u <USER> \
     -X PUT \
     -H "Content-Type:application/json" \
     https://<CONSOLE>:8083/api/v1/custom/custom-vulnerabilities \
     --data-binary "@custom_vulnerability_rules.json"
   ```

Any previously installed rules are overwritten with your new rules.
