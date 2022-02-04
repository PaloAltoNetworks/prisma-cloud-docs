Returns the forensic data for a container, which can be used to investigate runtime incidents.

The following example command retrieves forensic data for a specific container, where `id` is the profile ID (model) that Prisma Cloud Compute created for the container, and `hostname` is the machine where the Defender detected the incident.

## cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/profiles/container/{id}/forensic?hostname={hostname}"
```
