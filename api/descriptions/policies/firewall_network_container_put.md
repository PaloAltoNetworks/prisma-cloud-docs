Updates all container and host CNNS rules in a single shot.
Updating all rules at the same time makes it possible to maintain strict ordering between rules.

The procedure to add, edit, or remove rules is:

1. Get all rules using the GET endpoint.

  ### cURL Request
  Refer to the following example cURL command that retrieves a list of all rules, pretty-print the JSON response, and save the results to a file:

   ```bash
   $ curl -k \
     -u <USER> \
     -X PUT \
     -H "Content-Type:application/json" \
     -o <network_firewall_rules.json> \
     "https://<CONSOLE>/api/v<VERSION>/policies/firewall/network/container"
   ```

2. Modify the JSON output according to your needs.

3. Update rules by pushing the new JSON payload.

  ### cURL Request
  Refer to the following example cURL command that installs the rules defined in your `network_firewall_rules.json` file.
   Do not forget to specify the `@` symbol.

   ```bash
   $ curl -k \
     -u <USER> \
     -X PUT \
     -H "Content-Type:application/json" \
     --data-binary "@network_firewall_rules.json" \
     "https://<CONSOLE>/api/v<VERSION>/policies/firewall/network/container"
   ```

Any previously installed rules are overwritten.
