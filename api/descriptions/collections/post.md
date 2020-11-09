Creates a new collection.
Any field left unspecified is assigned the value of `""` (i.e. an emtpy string).

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "name": "my collection",
   "color": "#ff0000",
   "description": "A test collection",
   "images": [
     "docker.io/library/hello-world:latest",
     "docker.io/library/ian_app:1.0"
   ],
   "hosts": [
     "*"
   ]
 }' \
  https://<CONSOLE>:8083/api/v1/collections
```
