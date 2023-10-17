Scans the OpenAPI specifications file of size not more than 100 KB and generates a report for any errors, or shortcomings such as structural issues, compromised security, best practices, and so on. API definition scan supports scanning OpenAPI 2.X and 3.X definition files in either YAML or JSON formats.

### cURL Request

Refer to the following example cURL command that generates a report for any errors or shortcomings in the OpenAPI specification:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/waas/openapi-scans' \
-k \
-H 'Content-Type: multipart/form-data' \
-u <USER> \
-X POST \
-v -F‘spec=@<FILE NAME>.json;type=application/json’-F‘data={“source”:“manual”};type=application/json’
```