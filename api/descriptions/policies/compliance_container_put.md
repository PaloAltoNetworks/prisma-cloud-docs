Updates all rules that make up your compliance policy for containers in a single shot.
Updating all rules at the same time makes it possible to maintain strict ordering between rules.

The procedure to add, edit, or remove rules is:

1. Get all rules using the GET endpoint.

  The following curl command uses basic auth to retrieve a list of all rules, pretty-print the JSON response, and save the results to a file.

   ```
   $ curl -k \
     -u <USER> \
     https://<CONSOLE>:8083/api/v1/policies/compliance/container \
     | jq '.' > compliance_rules.json
   ```

2. Modify the JSON output according to your needs.

3. Update rules by pushing the new JSON payload.

   The following curl command installs the rules defined in your *compliance_rules.json* file.
   Do not forget to specify the `@` symbol.

   ```
   $ curl -k \
     -u <USER> \
     -X PUT \
     -H "Content-Type:application/json" \
     https://<CONSOLE>:8083/api/v1/policies/compliance/container \
     --data-binary "@compliance_rules.json"
   ```

Any previously installed rules are overwritten.

For more information, see [Manage compliance policies with the API](https://docs.twistlock.com/docs/latest/api/manage_compliance_api.html).
