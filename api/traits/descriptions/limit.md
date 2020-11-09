Specifies the maximum number of objects (events, incidents, etc) to return.
If left unspecified, all objects are returned (optionally constrained by the 'offset' parameter).
Use the 'limit' parameter with the 'offset' parameter to select specific objects in the collection.
For example, to retrieve a single object (the oldest object in the collection):

```
GET https://<CONSOLE>:8083/api/v1/<RESOURCE>?offset=0&limit=1
```

Where `RESOURCE` can be a top-level resource, such as `images` or `containers`.
