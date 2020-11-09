Creates a Helm deployment file  that can be used to deploy Defenders to your cluster.

For more information about how to use this endpoint, see
[Deploy a Defender Helm using the API](https://docs.twistlock.com/docs/19.07/install/install_kubernetes.html#install-twistlock-with-helm-charts).

The following example curl command returns a Defender Helm deployment file.
The `<HOSTNAME>` query parameter specifies the address that Defender uses to communicate with Console.
It can be a DNS name or IP address.

`<HOSTNAME>` is a single list item from the `/api/v1/defenders/names` endpoint.

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  -o twistlock-defender-helm.tar.gz
  'https://<CONSOLE>:8083/api/v1/defenders/helm/twistlock-defender-helm.tar.gz?consoleaddr=<HOSTNAME>&namespace=twistlock&orchestration=kubernetes'
```
