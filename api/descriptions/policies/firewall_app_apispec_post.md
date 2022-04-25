Resolves the endpoints defined in an OpenAPI/Swagger specification and returns a `waas.APISpec` object.

The `waas.APISpec` object can be included in the body of a subsequent call to the `PUT api/v1/policies/firewall/app/app-embedded` endpoint to define an app that WAAS monitors and protects.

To invoke this endpoint in the Console UI:

1. Navigate to the **Defend > WAAS > App-Embedded** page.
2. Click **Add rule**.
3. Enter the details for the new rule and click **Add new app**.
4. On the **App definition** tab, click the **Import** button and select an OpenAPI/Swagger specification file.

**Note:** You can use a YAML or JSON format for the OpenAPI/Swagger specification.

### cURL Request

Refer to the following example cURL command that imports an API from an OpenAPI/Swagger specification:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/apispec' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
  "swagger": "2.0",
  "info": {
    "version": "2021.7.28",
    "title": "Book API",
    "description": "A simple API for books.",
    "contact": {
      "name": "John Smith",
      "email": "test.email@email.com",
      "url": "http://mywebsite.com"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    }
  },
  "host": "api.mywebsite.com",
  "basePath": "/api",
  "schemes": [
    "http"
  ],
  "consumes": [
    "application/json"
  ],
  "produces": [
    "application/json"
  ],
  "paths": {
    "/books": {
      "get": {
        "description": "Returns a list of books.",
        "operationId": "findBooks",
        "responses": {
          "200": {
            "description": "Success response",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Book"
              }
            }
          },
          "default": {
            "description": "unexpected error",
            "schema": {
              "$ref": "#/definitions/Error"
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Book": {
      "allOf": [
        {
          "required": [
            "id"
          ],
          "properties": {
            "id": {
              "type": "integer",
              "format": "int64"
            }
          }
        }
      ]
    },
    "Error": {
      "required": [
        "code",
        "message"
      ],
      "properties": {
        "code": {
          "type": "integer",
          "format": "int32"
        },
        "message": {
          "type": "string"
        }
      }
    }
  }
}'
```

A successful response returns a `waas.APISpec` object containing the API specification that was imported.
