Retrieves all policies that uses a specified collection.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Collections and Tags > Collections**.
2. Click the dotted icon under the **Actions** column to open up the menu options. **Note:** The default collections do not have a dotted icon in the **Actions** column. Use the **Manage** cog icon to open the update window.
3. Click the **Manage** button. 
4. The **Usages** table displays the collection's usages.

### cURL Request

Refer to the following example cURL command that retrieves all policies with name `my-collection`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/collections/my-collection/usages'
```
