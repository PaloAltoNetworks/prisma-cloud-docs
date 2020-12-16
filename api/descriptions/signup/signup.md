Creates the initial admin user after Console is first installed, to help automation of Console setup.
Invoke this endpoint after Prisma Cloud Compute is first installed.

You can use this endpoint along with other endpoints to automate the Prisma Cloud Compute installation and setup.
For example, see `POST /api/v1/settings/license` to automate the submission of your license key.

**Note:** This sign up endpoint can only be executed once from Console *or* the API.
Invoking this endpoint after completion of the initial sign up will result in a `400` error response.
