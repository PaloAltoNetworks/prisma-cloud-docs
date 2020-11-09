Creates a DaemonSet deployment file in YAML format that can be used to deploy Defender to your cluster.

For more information about how to use this endpoint, see
[Deploy a Defender DaemonSet using the API](https://docs.twistlock.com/docs/latest/api/automate_defender_install.html).

The following example curl command returns a Defender DaemonSet deployment file.
The `<HOSTNAME>` query parameter specifies the address that Defender uses to communicate with Console.
It can be a DNS name or IP address.

`<HOSTNAME>` is a single list item from the `/api/v1/defenders/names` endpoint.

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  'https://<CONSOLE>:8083/api/v1/defenders/daemonset.yaml?consoleaddr=<HOSTNAME>&listener=none&namespace=twistlock&orchestration=kubernetes'
```
