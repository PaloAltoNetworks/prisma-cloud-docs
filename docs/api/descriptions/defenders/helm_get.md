Creates a Helm deployment file  that can be used to deploy Defenders to your cluster.

For more information about how to use this endpoint, see
[Deploy a Defender Helm using the API](https://docs.twistlock.com/docs/19.07/install/install_kubernetes.html#install-twistlock-with-helm-charts).

### cURL Request

Refer to the following example curl command that returns a Defender Helm deployment file:

The `<HOSTNAME>` query parameter specifies the address that Defender uses to communicate with Console.
It can be a DNS name or IP address.

`<HOSTNAME>` is a single list item from the `/api/v<VERSION>/defenders/names` endpoint.

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  -o twistlock-defender-helm.tar.gz \
  'https://<CONSOLE>/api/v<VERSION>/defenders/helm/twistlock-defender-helm.tar.gz?consoleaddr=<HOSTNAME>&namespace=twistlock&orchestration=kubernetes'
```
