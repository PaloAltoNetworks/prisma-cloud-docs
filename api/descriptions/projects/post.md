Provisions a new project.

The following example curl command provisions a new project named `my-project`.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "_id":"my-project",
   "type":"tenant",
   "address":"https://<SUPERVISOR_CONSOLE>:8083"
}' \
  https://<CENTRAL_CONSOLE>:8083/api/v1/projects
```

If you have installed a new instance of Console, and you have already created an initial admin user for it, then you can specify the admin username name and password when you provision the project.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "_id":"my-project",
   "type":"tenant",
   "address":"https://<SUPERVISOR_CONSOLE>:8083",
   "username":"henry",
   "password":{"plain":"testing123"}
}' \
  https://<CENTRAL_CONSOLE>:8083/api/v1/projects
```
