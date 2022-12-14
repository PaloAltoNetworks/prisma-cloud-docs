Returns all VM image scan reports.

**Note**: This endpoint maps to the table in **Monitor > Vulnerabilities > Hosts > VM images** in the Prisma Cloud Compute.

### cURL Request

Refer to the following example cURL command that retrieves all VM image scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/vms"
```

### cURL Response

Refer to the following example VM scan report:

```
{
    "_id": "2226875301309860442",
    "type": "vm",
    "hostname": "",
    "scanTime": "2022-12-01T18:08:15.299Z",
    "binaries": [],
    "Secrets": [],
    "startupBinaries": [],
    "osDistro": "redhat",
    "osDistroVersion": "7",
    "osDistroRelease": "RHEL7",
    "distro": "CentOS Linux release 7.9.2009 (Core)",
    "packages": [
      {
        "pkgsType": "package",
        "pkgs": [
          {
            "version": "0.100-7.el7",
            "name": "dbus-glib",
            "cveCount": 8,
            "license": "AFL and GPLv2+",
            "layerTime": 0
          },
          {
            "version": "2.02-0.87.el7.centos.7",
            "name": "grub2-common",
            "cveCount": 184,
            "license": "GPLv3+",
            "layerTime": 0
          }
        ...
        ...
        ...
        ]
      }
    ]
}
```
