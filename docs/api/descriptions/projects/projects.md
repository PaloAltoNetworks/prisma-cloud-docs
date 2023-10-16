Manage [Projects](https://docs.twistlock.com/docs/latest/deployment_patterns/projects.html).

Before you can provision a project using this endpoint, you must designate one instance of Console as master using the `POST /api/v1/settings/projects` endpoint.

#### Accessing the REST API of a supervisor Console

[comment]: # (See twistlock/pkg/console/route_handler_middleware.go: function NewRouteOpt, for the list of endpoints that are proxied.)

After enabling projects and provisioning a new project, access to the supervisor Console is proxied through Central Console.
You cannot access a supervisor's REST API directly.
All API requests to a supervisor must be made through Central Console.

To retrieve data from a project, add the the following query parameter to your request:

`project=<PROJECT_NAME>`

Where the default value for `project` is `Central+Console`.
If `project` is not specified, it is set to `Central+Console`.

For example, to retrieve the compliance policies for a tenant project named `mobile_payments_division`, use the following curl command:

```
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/policies/compliance?project=mobile_payments_division
```

Not all REST endpoints are proxied to the supervisor.
It largely depends on the project type (tenant or supervisor).
In some cases, requests cannot be proxied because management of that system is delegated to Central Console only.
Proxying a request to the right project is mostly a concern for tenant projects, which operate with their own policies and settings.

The following user management endpoints can be accessed from Central Console only.
An administrator centrally manages all users, and specifies who has access to which projects.
These calls are handled by Central Console only.

* `/api/v1/users`
* `/api/v1/groups`
* `/api/v1/projects`

The following endpoints are proxied to the relevant supervisor for tenant projects only.

* `/api/v1/policies`
* `/api/v1/trust`
* `/api/v1/settings`
* `/api/v1/collections`
* `/api/v1/feeds`

The following endpoints are proxied to the relevant supervisor for both tenant and scale projects:

* `/api/v1/settings/alerts`
* `/api/v1/alert-profiles`
* `/api/v1/settings/regisry`
* `/api/v1/settings/certs`
* `/api/v1/settings/secrets`
* `/api/v1/policies/secrets`

