Specifies the index of the first object (event, incident, etc) to return.
The default value is 0.
Use the 'offset' parameter with the 'limit' parameter to select specific objects in the collection.
For example, to retrieve the second oldest object in the collection:

```
GET https://<CONSOLE>:8083/api/v1/<RESOURCE>?offset=1&limit=1
```

Where `RESOURCE` can be a top-level resource, such as `images` or `containers`.
