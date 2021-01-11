Policies are sets of ordered rules.
[Rule order](https://docs.twistlock.com/docs/latest/configure/rule_ordering_pattern_matching.html) determines how a policy is evaluated.

You can manage your rules and policies programmatically using the policy API endpoints.

### How to Add / Update Policy Rules

All of the `PUT /api/v1/policies/*` endpoints work similarly. 

To add, edit, or remove vulnerability rules from a policy:

1. Retrieve the entire policy, which includes all the vulnerability rules using the `GET` endpoint.

  For example, the following cURL command uses basic auth to retrieve a list of all image vulnerability rules, pretty-prints the JSON response, and saves the results to a `vulnerability_rules.json` file.

   ```bash
   $ curl -k \
     -u <USER> \
     https://<CONSOLE>/api/v1/policies/runtime/host \
     | jq '.' > vulnerability_rules.json
   ```

2. Modify the saved JSON with the updates, including any new rule insertions. **Note:** Rule order is important.

3. Update the rules by pushing the new JSON payload into the `PUT` endpoint.

   For example, the following cURL command installs the rules defined in your `vulnerability_rules.json` file.
   
   **Note:** Remember to specify the `@` symbol.

   ```bash
   $ curl -k \
     -u <USER> \
     -X PUT \
     -H "Content-Type:application/json" \
     https://<CONSOLE>/api/v1/policies/runtime/host \
     --data-binary "@vulnerability_rules.json"
   ```

Any previously installed rules are overwritten.

#### Minimum Rule Parameters

To create or update a rule, specify the following:

* Rule name
* At least 1 collection specifying a collection name (at minimum)
* A block threshold (optional, but recommended)
* An alert threshold (optional, but recommended)

For example, to replace all the vulnerability rules for CI image deployments:

```bash
$ curl 'https://<CONSOLE>/api/v1/policies/vulnerability/ci/images?project=<PROJECT>' \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
  "rules": [
    {
      "name": "<RULE_NAME>",
      "collections":[
         {
            "name":"<COLLECTION_NAME>",
         }
      ],
      "alertThreshold":{
         "disabled":false,
         "value":4
      },
      "blockThreshold":{
         "enabled":false,
         "value":0
      },
    }
  ],
  "policyType": "ciImagesVulnerability"
}'
```

**Note:** The default alert threshold of `Low` is typically too broad and not actionable. Usually you'll want to specify a threshold of `Critical` or `High`.

##### Referencing Collections by Name

You can reference a collection by its name when creating / updating a rule.
If the collection name exists in Console, the remaining resource fields for the collection will automatically be filled in.

**Note:** The referenced collections *must* exist prior to creating / updating rules, or the API will not add / update your rules.

In Console, the default collection is `All`.
`All` is a collection created by the system when the software is installed / upgraded.
When using the API, you can specify `All` as the `<COLLECTION_NAME>` to apply the default collection.

### How to Delete Policy Rules

In general, the policy endpoints don't have `DELETE` methods.
Use the `PUT` method to delete all rules by submitting an empty JSON object.

For example, to delete all host runtime rules:

```
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{}' \
  https://<CONSOLE>/api/v1/policies/runtime/host
```