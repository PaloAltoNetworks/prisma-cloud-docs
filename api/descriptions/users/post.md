Adds a new user to the system.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Users**.
2. Click **+ Add user** and enter the user's information.
3. Click the **Save** button.

Every Console has a project name, even if projects aren't enabled.
If you've deployed a single stand-alone Console, it's called `Central Console`.
If you've enabled projects, the master Console is called `Central Console`.
Each connected tenant project has a unique name, which is specified when the project is created.

All users are created and managed in `Central Console`.

### cURL Requests

Refer to the following example cURL requests:

#### Add a New User

When `authType` is set to `basic`, the system creates a "local" user that's managed in Console's database.
If you integrated Prisma Cloud with an identity provider, set `authType` to a supported value, such as `saml`.

The following example cURL command adds a new user to Central Console:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/users' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "username":"<ID>",
   "password":"<PASSWORD>",
   "role":"auditor",
   "authType":"basic"   
}'
```

**Note:** No response will be returned upon successful execution.

#### Add a New User and Grant Access to a Project

Use the `permissions` object to grant a user access to specific projects and specific collections in a project.

When you define the `permissions` object, specify the following parameters:
`projects`: (Required.) Specifies a project name.
`collections`: (Requires initialization with a valid collection name.) Specifies a valid collection to assign to the user.
If left unspecified, users are granted access to the `All` collection by default.

The following example cURL command adds a new user to Console and grants access to the tenant project `PROJECT_NAME`:

Before you invoke this request:

1. In the Console UI navigate to **Manage > Projects**.
2. Enable the **Use projects** setting.
3. If no project is provisioned, use the **+ Provision project** button to create a new project.
4. Retrieve a tenant project name from the table from the **Project** column.

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/users' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "username":"<ID>",
   "password":"<PASSWORD>",
   "role":"auditor",
   "authType":"basic",
   "permissions":[
      {
         "project":"<PROJECT_NAME>"
      }
   ]   
}'
```

**Note:** No response will be returned upon successful execution.

#### Add a New User and Grant Access to a Collection

When assigning collections, you must explicitly specify a project.
When you're working with a single stand-alone Console, the value for project is `Central Console`.

The following example cURL command adds a new user to Console and grants access to the `finance-app` collection in `Central Console`:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/users' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "username":"<ID>",
   "password":"<PASSWORD>",
   "role":"auditor",
   "authType":"basic",
   "permissions":[
      {
         "project":"Central Console",
         "collections":[
            "finance-app"
         ]
      }
   ]   
}'
```

**Note:** No response will be returned upon successful execution.
