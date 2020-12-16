Paginated API requests are capped to a max of 50 returned objects because very large responses could DoS Console.

If the response contains more than 50 objects, cycle through the collection with the `offset` query parameter to retrieve more objects.
For example:

```
https://<CONSOLE>/api/v1/images?limit=50&offset=X
```
