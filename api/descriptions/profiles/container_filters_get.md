Returns a list of os and images from page monitor/runtime/container-models in Console.


Example curl command:

```bash
$ curl -k -G \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  --data-urlencode 'image=istio/examples-bookinfo-reviews-v2:1.8.0'
  https://<CONSOLE>:8083/api/v1/profiles/container/filters
```
