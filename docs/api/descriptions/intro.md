# How to evaluate <CONSOLE>

All the example API commands in these documents specify a `<CONSOLE>` variable, which represents the address for Console.
The Console address will depend on how Console was installed.

## For SaaS Installations

To find your `<CONSOLE>` path for a SaaS environment:

1. Log into Console.
2. Navigate to **Compute** > **Manage** > **System** > **Downloads**.
3. You can find your `<CONSOLE>` path listed under **Path to Console**. Click **Copy** to quickly copy the path to your clipboard.

<img src="console_saas.png" alt="console" width="100%"/>



## For Self-hosted Installations

For self-hosted environments, the Prisma Cloud Compute API is exposed on port `8083` (HTTPS).
This port is specified at install time in `twistlock.cfg`.

* **(Default) Kubernetes installations:** Console service is exposed by a LoadBalancer.
	
	The value for `<CONSOLE>` is the LoadBalancer followed by port `8083`:

	```
	https://<LOAD_BALANCER>:8083
	```

* **Onebox installations:** Console installed on a stand-alone host.

	The value for `<CONSOLE>` is the IP address or DNS name of the host followed by port `8083`:

	```
	https://<IP_ADDRESS>:8083
	```

# Using the curl example commands


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


# API restrictions


Paginated API requests are capped to a max of 50 returned objects because very large responses could DoS Console.

If the response contains more than 50 objects, cycle through the collection with the `offset` query parameter to retrieve more objects.
For example:

```
https://<CONSOLE>/api/v1/images?limit=50&offset=X
```
