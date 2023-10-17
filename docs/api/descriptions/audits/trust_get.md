Retrieves all the trust audit events.

### cURL Request
Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/trust"
```
### cURL Response

```
{
        "_id": "quay.io/openshift-release-dev/ocp-v4.0-art-dev",
        "time": "2022-11-22T18:15:06.793Z",
        "total": 7,
        "resource": {
            "images": [
                "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:9dd1b7719d2a52910d7860f22d038ab57e1d3aa5274a3d0850112394fdf4aec0"
            ],
            "accountIDs": [
                "twistlock-test-247119"
            ],
            "clusters": [
                "openshift-v1-22-89e95cb9-cri-o-1-22-5-14-rhaos4-9-git80a8e67-el8-u-openshift-370392"
            ]
        },
        "collections": [
            "All"
        ],
        "cluster": "openshift-v1-22-89e95cb9-cri-o-1-22-5-14-rhaos4-9-git80a8e67-el8-u-openshift-370392",
        "audits": {
            "untrusted": {
                "count": 7,
                "audits": [
                    {
                        "_id": "quay.io/openshift-release-dev/ocp-v4.0-art-dev",
                        "time": "2022-11-22T18:15:06.793Z",
                        "imageName": "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:c3f8fe342716c0d9ba925a65f6f234e5c4d9670e7ea84bd227cf2af454dd4f0d",
                        "imageID": "0fad6b33183ae7dbd050b095bdd1d004911ba8f49d08104d513f4e0e1ee460b1",
                        "effect": "alert",
                        "ruleName": "TV 1",
                        "msg": "Untrusted by rule TV 1",
                        "count": 1,
                        "accountID": "twistlock-test-247119",
                        "cluster": "openshift-v1-22-89e95cb9-cri-o-1-22-5-14-rhaos4-9-git80a8e67-el8-u-openshift-370392"
                    },
                    {
                        "_id": "quay.io/openshift-release-dev/ocp-v4.0-art-dev",
                        "time": "2022-11-22T18:15:04.922Z",
                        "imageName": "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:9dd1b7719d2a52910d7860f22d038ab57e1d3aa5274a3d0850112394fdf4aec0",
                        "imageID": "90e290196294063f8638cbc4e4c8f1db669a0b2ff67ac2c3d6612e6f783ffbd3",
                        "effect": "alert",
                        "ruleName": "TV 1",
                        "msg": "Untrusted by rule TV 1",
                        "count": 1,
                        "accountID": "twistlock-test-247119",
                        "cluster": "openshift-v1-22-89e95cb9-cri-o-1-22-5-14-rhaos4-9-git80a8e67-el8-u-openshift-370392"
                    },
                    {
                        "_id": "quay.io/openshift-release-dev/ocp-v4.0-art-dev",
                        "time": "2022-11-22T18:00:02.682Z",
                        "imageName": "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:c3f8fe342716c0d9ba925a65f6f234e5c4d9670e7ea84bd227cf2af454dd4f0d",
                        "imageID": "0fad6b33183ae7dbd050b095bdd1d004911ba8f49d08104d513f4e0e1ee460b1",
                        "effect": "alert",
                        "ruleName": "TV 1",
                        "msg": "Untrusted by rule TV 1",
                        "count": 1,
                        "accountID": "twistlock-test-247119",
                        "cluster": "openshift-v1-22-89e95cb9-cri-o-1-22-5-14-rhaos4-9-git80a8e67-el8-u-openshift-370392"
                    },
                    {
                        "_id": "quay.io/openshift-release-dev/ocp-v4.0-art-dev",
                        "time": "2022-11-22T18:00:00.733Z",
                        "imageName": "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:9dd1b7719d2a52910d7860f22d038ab57e1d3aa5274a3d0850112394fdf4aec0",
                        "imageID": "90e290196294063f8638cbc4e4c8f1db669a0b2ff67ac2c3d6612e6f783ffbd3",
                        "effect": "alert",
                        "ruleName": "TV 1",
                        "msg": "Untrusted by rule TV 1",
                        "count": 1,
                        "accountID": "twistlock-test-247119",
                        "cluster": "openshift-v1-22-89e95cb9-cri-o-1-22-5-14-rhaos4-9-git80a8e67-el8-u-openshift-370392"
                    },
                    {
                        "_id": "quay.io/openshift-release-dev/ocp-v4.0-art-dev",
                        "time": "2022-11-22T17:45:14.196Z",
                        "imageName": "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:c3f8fe342716c0d9ba925a65f6f234e5c4d9670e7ea84bd227cf2af454dd4f0d",
                        "imageID": "0fad6b33183ae7dbd050b095bdd1d004911ba8f49d08104d513f4e0e1ee460b1",
                        "effect": "alert",
                        "ruleName": "TV 1",
                        "msg": "Untrusted by rule TV 1",
                        "count": 1,
                        "accountID": "twistlock-test-247119",
                        "cluster": "openshift-v1-22-89e95cb9-cri-o-1-22-5-14-rhaos4-9-git80a8e67-el8-u-openshift-370392"
                    }
                ]
            }
        }
    }
```