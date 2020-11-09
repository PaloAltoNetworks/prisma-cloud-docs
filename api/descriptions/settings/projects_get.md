Tells you whether the [Projects](https://docs.twistlock.com/docs/latest/deployment_patterns/projects.html) feature is enabled.
Projects are enabled when an instance of Console is designated as master.

The following example curl command retrieves the state of the Projects feature from Console.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/projects
```

If you direct the request to a supervisor Console, the response object tells you the URL Central Console (master) uses to communicate with the supervisor Console.
All API calls must be proxied through Central Console, where the request is automatically rerouted to the appropriate supervisor Console.
To retrieve the Projects settings from a supervisor Console, append the `project` query parameter to your request.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CENTRAL-CONSOLE>:8083/api/v1/settings/projects?project=<PROJECT_NAME>
```
