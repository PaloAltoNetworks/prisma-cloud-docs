The cURL example for each endpoint is called with a username (`-u <USER>`) only.
The cURL can be modified to use any of the following:

* **Authentication Token:** Use the `-H` option to pass the authentication token from the `/api/v1/authenticate` endpoint into the request header.

For example, replace `<ACCESS_TOKEN>` with the token from the `/api/v1/authenticate` endpoint.

```bash
$ curl -k \
-H 'Authorization: Bearer <ACCESS_TOKEN>' \
-X POST \
https://<CONSOLE>/api/v1/<ENDPOINT_PATH>
```

* **Username and Password:** Use the `-u` and `-p` options to include the username and password, eliminating the need to enter a password in a secondary step.

For example, replace `<USER>` with the username string and `<PASSWORD>` with the password string.

```bash
$ curl -k \
-u <USER> \
-p <PASSWORD> \
-X POST \
https://<CONSOLE>/api/v1/<ENDPOINT_PATH>
```

* **Username Only:** This will require the user's password to be entered as a secondary step.

For example, replace `<USER>` with the username string.

```bash
$ curl -k \
-u <USER> \
-X POST \
https://<CONSOLE>/api/v1/<ENDPOINT_PATH>
```

**Note:** This is a more secure method than including the `-p` option since your terminal history won't contain the password.
