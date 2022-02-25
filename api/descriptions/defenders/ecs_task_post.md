Creates an Amazon Elastic Container Service (ECS) task definition JSON file.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -o <ecs-task.json> \
  -d \
 '{
    "taskName": "my-task",
    "orchestration": "container",
    "consoleAddr": "servo-vmware71",
    "namespace": "twistlock"
  }' \
  "https://<CONSOLE>/api/v1/defenders/ecs-task.json"
```