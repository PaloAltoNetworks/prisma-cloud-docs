Retrieves all scan reports from the Jenkins plugin and twistcli in CSV format.
In Console, this would be the equivalent of clicking the **CSV** download button in **Monitor > Vulnerabilities > Jenkins Jobs** and **Monitor > Vulnerabilities > Twistcli Scans**.

The following example curl command retrieves and saves your Jenkins and twistcli scan reports to a CSV file called `registry_report.csv`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/scans/download \
  > scans_report.csv
```
