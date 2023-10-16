Retrieves the list of code repositories Prisma Cloud is configured to scan. 
It also retrieves a partial webhook URL.

> _**Note:**_ The API rate limit for this endpoint is 30 requests per 30 seconds.
You get an HTTP error response 429 if the limit exceeds.

This endpoint maps to **Defend > Vulnerabilities > Code repositories** in the Console UI page.

* **GitHub repositories scan scope** table data
* URL suffix in **Webhook settings**

### Webhook

You can optionally configure your code repositories with a webhook to trigger Prisma Cloud to scan repositories when there are pertinent events (e.g., new code commits).

Construct the full webhook using Console's publicly accessible DNS name or IP address, plus the webhook URL suffix.

### cURL Request

Refer to the following example cURL command that retrieves all code repositories to scan, as well as the webhook URL suffix:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/settings/coderepos'
```
