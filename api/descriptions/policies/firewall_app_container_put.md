Updates all application firewall (CNAF) rules in a single shot.
Updating all rules at the same time makes it possible to maintain strict ordering between rules.

The procedure to add, edit, or remove application firewall rules is:

1. Get all application firewall rules using the GET endpoint.

  The following curl command uses basic auth to retrieve a list of all rules, pretty-print the JSON response, and save the results to a file.

   ```
   $ curl -k \
     -u <USER> \
     https://<CONSOLE>:8083/api/v1/policies/firewall/app/container \
     | jq '.' > app_firewall_rules.json
   ```

2. Modify the JSON output according to your needs.

3. Update rules by pushing the new JSON payload.

   The following curl command installs the rules defined in your *app_firewall_rules.json* file.
   Do not forget to specify the `@` symbol.

   ```
   $ curl -k \
     -u <USER> \
     -X PUT \
     -H "Content-Type:application/json" \
     https://<CONSOLE>:8083/api/v1/policies/firewall/app/container \
     --data-binary "@app_firewall_rules.json"
   ```

Any previously installed rules are overwritten.
