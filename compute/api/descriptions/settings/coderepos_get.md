Retrieves the list of code repositories Prisma Cloud is configured to scan. 
It also retrieves a partial webhook URL.

This endpoint maps to the following information on the **Defend > Vulnerabilities > Code repositories** Console UI page:

* **GitHub repositories scan scope** table data
* URL suffix in **Webhook settings**

### Webhook

You can optionally configure your code repositories with a webhook to trigger Prisma Cloud to scan repositories when there are pertinent events (e.g., new code commits).

Construct the full webhook using Console's publicly accessible DNS name or IP address, plus the webhook URL suffix.

### cURL Request

The following cURL command retrieves all code repositories to scan, as well as the webhook URL suffix.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/settings/coderepos'
```
