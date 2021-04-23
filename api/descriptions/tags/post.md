Creates a new tag.
Any field left unspecified is assigned the value of `""` (an empty string).

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "name": "my tag",
   "color": "#ff0000",
   "description": "A test collection"
 }' \
  https://<CONSOLE>:8083/api/v1/tags
```
