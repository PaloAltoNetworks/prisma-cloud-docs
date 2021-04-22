Retrieves the list of registries Prisma Cloud is configured to scan.
It also retrieves a partial webhook URL.

This endpoint maps to the following information on the **Defend > Vulnerabilities > Images > Registry settings** Console UI page:

* **Registries** table data
* The URL suffix under **Webhooks**

### Webhook

You can optionally configure your registry with a webook to trigger Prisma Cloud to scan repositories when there is a pertinent event (e.g. a new image is pushed to the registry).

Construct the full webhook using the publicly accessible DNS name or IP address, plus the webhook URL suffix.

### cURL Request

The following cURL command retrieves all the registries to scan and the URL suffix for the registry's webhook URL suffix.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/settings/registry'
```
