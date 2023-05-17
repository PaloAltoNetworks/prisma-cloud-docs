Updates all the custom vulnerabilities and associated rules simultaneously for handling internally created or packaged apps.

### cURL Request

Refer to the following cURL command that updates a vulnerability for a library named `internal-lib`, and specifies that its versions `1.1` to `1.8` are known to be vulnerable.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '
{
  "rules": [
    {
      "_id": "<ID>",
      "package": "internal-lib",
      "type": "package",
      "minVersionInclusive": "1.1",
      "name": "internal-lib",
      "maxVersionInclusive": "1.8",
      "md5": ""
    }
  ]
}' \
"https://<CONSOLE>/api/v<VERSION>/feeds/custom/custom-vulnerabilities"
```

**Note:** No response will be returned upon successful execution.

### Maintain your Custom Vulnerabilities

We suggest you maintain your custom vulnerabilities using the following steps:

1. Get all the custom vulnerability rules from the `GET` endpoint and save the results to a file.

	**Note:** You will need `jq` to execute this command.

   ```
   $ curl -k \
     -u <USER> \
     https://<CONSOLE>/api/v<VERSION>/feeds/custom/custom-vulnerabilities \
     | jq '.' > custom_vulnerability_rules.json
   ```

2. Open the JSON file and add, modify, and/or delete the rules by directly editing the JSON output. For example:

	```json
	{
		"id": "customVulnerabilities",
		"rules": [
		    {
		      "_id": "<ID>",
		      "package": "internal-lib",
		      "type": "package",
		      "minVersionInclusive": "1.1",
		      "name": "internal-lib",
		      "maxVersionInclusive": "1.8",
		      "md5": ""
		    }
		],
		"digest": "97de7f27XXXXXXXXXX"
	}
	```

3. Update the rules by pushing the new JSON payload. **Note:** Do not forget to specify the `@` symbol.

   ```
   $ curl -k \
     -u <USER> \
     -X PUT \
     -H "Content-Type:application/json" \
     -d @custom_vulnerability_rules.json \
     https://<CONSOLE>/api/v<VERSION>/feeds/custom/custom-vulnerabilities
   ```

4. Run the cURL command for the `GET /api/vVERSION/feeds/custom/custom-vulnerabilities` endpoint and you can see that the previously installed rules are now overwritten with your new rules.

	```bash
	$ curl -k \
	  -u <USER> \
	  -H 'Content-Type: application/json' \
	  -X GET \
	  https://<CONSOLE>/api/v<VERSION>/feeds/custom/custom-vulnerabilities
```
