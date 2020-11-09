Returns the forensic data for a container, which can be used to investigate runtime incidents.  This will return a tar.gz file as a zipped file.

The following example command retrieves forensic data for a specific container, where `id` is the profle ID (model) that Twistlock created for the container, and `hostname` is the machine where the Defender detected the incident.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o twistlock_container_forensics.tar.gz
  "https://<CONSOLE>:8083/api/v1/profiles/container/{id}/forensic/bundle?hostname={hostname}"
```
