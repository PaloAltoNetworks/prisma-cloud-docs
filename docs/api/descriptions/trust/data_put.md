Updates a trusted image to the system.
Specify trusted images using either the image name or layers properties.

## cURL Request

Refer to the following example cURL command that uses basic auth to specify that the Ubuntu 16.04 image on Docker Hub is a trusted image:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{"image":"ubuntu/16.04", "_id":"docker-ubuntu-group"}' \
  https://<CONSOLE>/api/v<VERSION>/trust/data
```

To edit a trust group based on image base layers, use PUT to specify a list of SHA256 hashes for the layers that are trusted.

Refer to the following example that specifies the Ubuntu 16.04 image is a trusted base OS.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{"layers":"["sha256:a94e0d5a7c404d0e6fa15d8cd4010e69663bd8813b5117fbad71365a73656df9",
    "sha256:88888b9b1b5b7bce5db41267e669e6da63ee95736cb904485f96f29be648bfda",
    "sha256:52f389ea437ebf419d1c9754d0184b57edb45c951666ee86951d9f6afd26035e",
    "sha256:52a7ea2bb533dc2a91614795760a67fb807561e8a588204c4858a300074c082b",
    "sha256:db584c622b50c3b8f9b8b94c270cc5fe235e5f23ec4aacea8ce67a8c16e0fbad"]", "_id":"docker-ubuntu-group"}' \
  "https://<CONSOLE>/api/v<VERSION>/trust/data"
```
