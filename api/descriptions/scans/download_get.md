Retrieves all scan reports for either Jenkins plugin or twistcli scans in csv format. In the console, this would be the equivalent of pressing the 
**CSV** download button in **Monitor > Vulnerabilities > Jenkins Jobs** and **Monitor > Vulnerabilities > Twistcli Scans**.

The following example curl command uses basic auth to retrieve and save your console's Jenkins and twistcli scan reports to a csv file called `registry_report.csv`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/scans/download \
  > scans_report.csv
```
