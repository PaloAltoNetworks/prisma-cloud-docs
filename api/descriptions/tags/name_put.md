Updates the parameters that define a given tag.

The following example curl command updates the parameters that define the tag named `my_tag`.
In general, all parameters in your PUT request should be defined or redefined.
Any field left unspecified is assigned the value of `""` (i.e. an emtpy string).

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d \
'{
   "name": "my_tag2",
   "color": "#ff0000",
   "description": "A super cool tag"
 }' \
  https://<CONSOLE>:8083/api/v1/tags/my_tag
```
