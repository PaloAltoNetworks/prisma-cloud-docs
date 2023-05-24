Returns the trusted registries, repositories, and images.

## cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \                                                                     
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/trust/data
```

## cURL Response

Refer to the following example response:

```bash
$ {
 "policy": {
   "_id": "trust",
   "enabled": false,
   "rules": [
     {
       "modified": "2023-05-11T09:24:33.936Z",
       "owner": "ss",
       "name": "Copy of combined",
       "previousName": "",
       "disabled": true,
       "allowedGroups": [
         "by_cluster"
       ],
       "deniedGroups": [
         "by_host"
       ],
       "collections": [
         {
           "hosts": [
             "ss-ubu2204-dock-0905t072802-cont-def-pre-lngcon443.c.example-247119.internal"
           ],
           "images": [
             "*"
           ],
           "labels": [
             "*"
           ],
           "containers": [
             "*"
           ],
           "functions": [
             "*"
           ],
           "namespaces": [
             "*"
           ],
           "appIDs": [
             "*"
           ],
           "accountIDs": [
             "*"
           ],
           "codeRepos": [
             "*"
           ],
           "clusters": [
             "*"
           ],
           "name": "trust_by_host",
           "owner": "ss",
           "modified": "2023-05-11T09:17:17.556Z",
           "color": "#D64CA8",
           "system": false,
           "prisma": false
         }
       ],
       "effect": "alert"
     },
     {
       "modified": "2023-05-11T09:24:13.952Z",
       "owner": "ss",
       "name": "combined",
       "previousName": "",
       "disabled": true,
       "allowedGroups": [
         "by_cluster"
       ],
       "deniedGroups": [
         "by_host"
       ],
       "collections": [
         {
           "hosts": [
             "jen-ubu2204-dock-0905t072802-cont-def-pre-lngcon443.c.twistlock-test-247119.internal"
           ],
           "images": [
             "*"
           ],
           "labels": [
             "*"
           ],
           "containers": [
             "*"
           ],
           "functions": [
             "*"
           ],
           "namespaces": [
             "*"
           ],
           "appIDs": [
             "*"
           ],
           "accountIDs": [
             "*"
           ],
           "codeRepos": [
             "*"
           ],
           "clusters": [
             "*"
           ],
           "name": "trust_by_host",
           "owner": "ss",
           "modified": "2023-05-11T09:17:17.556Z",
           "color": "#D64CA8",
           "system": false,
           "prisma": false
         }
       ],
       "effect": "alert"
     },
     {
       "modified": "2023-05-10T19:05:27.651Z",
       "owner": "ss",
       "name": "Default - alert all",
       "previousName": "",
       "collections": [
         {
           "hosts": [
             "*"
           ],
           "images": [
             "*"
           ],
           "labels": [
             "*"
           ],
           "containers": [
             "*"
           ],
           "functions": [
             "*"
           ],
           "namespaces": [
             "*"
           ],
           "appIDs": [
             "*"
           ],
           "accountIDs": [
             "*"
           ],
           "codeRepos": [
             "*"
           ],
           "clusters": [
             "*"
           ],
           "name": "All",
           "owner": "system",
           "modified": "2023-05-09T07:00:08.761Z",
           "color": "#3FA2F7",
           "description": "System - all resources collection",
           "system": true,
           "prisma": false
         }
       ],
       "effect": "alert"
     }
   ]
 },
 "groups": [
   {
     "modified": "2023-05-10T19:08:34.893Z",
     "owner": "mbarash",
     "name": "",
     "previousName": "",
     "_id": "by_host",
     "images": [
       "alpine:*"
     ]
   },
   {
     "modified": "2023-05-10T19:16:46.886Z",
     "owner": "ss",
     "name": "",
     "previousName": "",
     "_id": "by_cluster",
     "images": [
       "registry.k8s.io/etcd:*"
     ]
   },
   {
     "modified": "2023-05-11T09:11:54.683Z",
     "owner": "ss",
     "name": "",
     "previousName": "",
     "_id": "by_image",
     "images": [
       "node:*"
     ]
   },
   {
     "modified": "2023-05-11T09:21:23.54Z",
     "owner": "ss",
     "name": "",
     "previousName": "",
     "_id": "by_registry",
     "images": [
       "mcr.azk8s.cn/*"
     ]
   },
   {
     "modified": "2023-05-11T09:22:13.522Z",
     "owner": "ss",
     "name": "",
     "previousName": "",
     "_id": "by_repository",
     "images": [
       "python:*"
     ]
   },
   {
     "modified": "2023-05-11T09:22:47.854Z",
     "owner": "ss",
     "name": "",
     "previousName": "",
     "_id": "bu_layer_automated",
     "layers": [
       "sha256:a0d44e5352dcb84bca48b6ee3d30a9ec91b5e6eb6793747e06d2454d360a9338",
       "sha256:5ad177daa048ca8b354b9ad03deac863ff519a2860a35dc9fdc0011619aacc3c",
       "sha256:543bb037d9827e706ea0ee9277e56ff916439a114fa56c520ac7dcaf6daae84a",
       "sha256:efd3b1563a816d85c6414e0c139691df720c34d6f65abaa19819d37b11459b40",
       "sha256:bc30bde5a6578b9643d05dd47105414777adadaf5df93b493eff1785e1e07328",
       "sha256:77e7191206a99af5cf1718885fb45262c2e2da30ad650c5868dfa3c54739c24a",
       "sha256:4fcf730353158873699670f97f2556942ff470c360539ff9283d80c72f275030",
       "sha256:d1a8d814c41eab7ee00b94a9184f081bf4c36721d559c5b349b9653bd473d8a0"
     ]
   },
   {
     "modified": "2023-05-11T09:23:21.338Z",
     "owner": "ss",
     "name": "",
     "previousName": "",
     "_id": "by_manual_manual",
     "layers": [
       "sha256:05f4935ad90ae437375c64090af07a6232bfeffc9f311e3e315919627c542ac9",
       "sha256:5aea01ea0a0f088b7844c169b9b8fd5ea034a21b4aa075ae3c54a1cb64138b93",
       "sha256:d8183b2c9c73e92b3569c8c77f05a245d1d4a58c3d3f23e740ea4f69c5e8d8f4",
       "sha256:ee50c22fdf6c99affec8690f7ef820f0e8cd19f4ece9a32503cdcf59a391514d"
     ]
   },
   {
     "modified": "2023-05-11T12:41:27.885Z",
     "owner": "ss",
     "name": "",
     "previousName": "",
     "_id": "ss_test",
     "images": [
       "kuku:*",
       "example/cves:*"
     ]
   }
 ]
}
```