Retrieves the latest log messages for a given Defender.
The Defender is specified by the host where it runs.
You can retrieve the hostname for each Defender from the `GET /api/v1/defenders` endpoint.

The following example curl command retrieves the 10 log messages for the Defender that runs on `worker.sandbox.internal`.
Note that you must quote the URL when running the following command.
Otherwise the shell misinterprets the ampersand (`&`) as the end of the command, and puts the curl command in the background.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/logs/defender?lines=10&hostname=worker.sandbox.internal"
```
