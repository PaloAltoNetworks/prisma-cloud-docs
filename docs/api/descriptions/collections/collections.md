Collections are predefined filters that let you group related resources together.
Resources include things like containers, images, hosts, functions, and clusters.

Use collections to scope policy rules and segment data/views in the Console UI and the Prisma Cloud API.


### Endpoints with a `{id}` URL Parameter

Some `/collections` endpoints take a URL parameter called `{id}`.
The value for `{id}` should be a collection name.
You can retrieve collection names from the `GET /api/v1/collections` endpoint.
Each collection object in the response has a key called `name`, which can be used for `{id}`.

**Note:** Spaces are considered [unsafe characters in a URL](https://www.ietf.org/rfc/rfc1738.txt).
If your collection name has a space, encode the space with the value `%20` before passing it as a URL parameter.
