Updates all serverless runtime rules in a single shot.
Updating all rules at the same time makes it possible to maintain strict ordering between rules.

The procedure to add, edit, or remove compliance rules is:

1. Get all host runtime rules using the GET endpoint.

  The following curl command uses basic auth to retrieve the rules, pretty-print the JSON response, and save the results to a file.

   ```
   $ curl -k \
     -u <USER> \
     -H 'Content-Type: application/json' \
     -X GET
     https://<CONSOLE>:8083/api/v1/policies/runtime/serverless \
     | jq '.' > serverless_runtime_rules.json
   ```

2. Modify the JSON output according to your needs.

3. Update rules by pushing the new JSON payload.

   The following curl command installs the rules defined in your *serverless_runtime_rules.json* file.
   Do not forget to specify the `@` symbol.

   ```
   $ curl -k \
     -u <USER> \
     -H "Content-Type:application/json" \
     -X PUT \
     https://<CONSOLE>:8083/api/v1/policies/runtime/serverless \
     --data-binary "@serverless_runtime_rules.json"
   ```

Any previously installed rules are overwritten.
