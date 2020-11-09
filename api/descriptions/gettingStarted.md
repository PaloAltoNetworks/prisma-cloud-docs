The number of objects returned from paginated API requests is capped to a max of 50 because very large responses could DoS your Console.
If the response contains more than 50 objects, cycle through the collection with the `offset` query parameter.
For example:

```
https://CONSOLE:8083/api/v1/images?limit=50&offset=X
```
