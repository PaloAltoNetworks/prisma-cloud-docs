Sets a tag to a vulnerability based on Common Vulnerability and Exposures (CVE) ID, package, and resource.

**Consider the following scenarios**: 
  - When you apply a tag to a vulnerability only on a package, the tag applies to the vulnerability in all the resources related to it.
  - When you apply a tag only to a vulnerability, the tag applies to the vulnerability in all the packages and resources related to it.
  - When you apply a tag to a vulnerability on a resource type, specify the scope of the resources using either a wildcard "*" or resource names.
  
A vulnerability can be found in a source package or a binary package. 
The vulnerability feed reports CVE data either on source packages or binary packages. 
For example, Debian and Ubuntu report CVEs on the source package, while RHEL reports on binary packages. 

**Source package:** Provides all the necessary files to compile or build the desired piece of software. For more information, see [Source Package](https://wiki.debian.org/Packaging/SourcePackage).

**Binary package:** Built from a source package. There could be multile binary packages that are built from a source package. 
For example, `perl` is a source package, and you can build different binary packages such as `libperl-dev`, `perl`, or `perl-base`. For more information, see [Perl](https://packages.ubuntu.com/source/focal/perl).

Prisma Cloud ingests all the various distro vulnerability feeds, and normalizes them so that they can be used uniformly across the product. 

The **package info** tab shows both source and binary package fields in a vulnerability report.

Refer to the following parameter descriptions:
- **id**: `Required` Specifies the Common Vulnerability and Exposures (CVE) ID.
- **packageName**: `Required` Specifies the source or the binary package name where the vulnerability is found. 
Specify the source package name for tagging when the vulnerability is found in the source package.
Use the wildcard `*` to apply the tag to all the packages where the vulnerability is found.
- **resourceType**: Specifies the resource type for tagging where the vulnerability is found. 
Use the wildcard `*` to apply the tag to all the resource types where the vulnerability is found.
The available values are: `image`, `host`, `function`, `codeRepo`, and `""`.
- **resources**: `Required when you define the resource type.` Specifies the resource for tagging where the vulnerability is found. 
Either specify the resource names separated by a comma or use the wildcard `*` to apply the tag to all the resources where the vulnerability is found.
- **checkBaseLayer**: `Applies only to the resource type image.` Checks for the base image in the resources and whether to tag those resources.
- **comment**: Adds a comment.

Consider the following scenarios for source and binary packages:

- Debian or Ubuntu lists the binary packages and source packages. 
  A CVE-2020-16156 is found in a binary package `perl-base` and source package `perl` in Ubuntu 20.04.3 LTS distro.

  ![Package information](https://cdn.twistlock.com/docs/api/Ubuntu-Vuln-Bin-Package-Info.png)

  The parameter *packageName* in the endpoint accepts only the source package name for tagging if a source package is available.

  ### cURL Request

  Refer to the following example cURL command that tags `Ignored` to the CVE `CVE-2020-16156` on the source package `perl`:

  ```bash
  $ curl -k \
    -u <USER> \
    -H 'Content-Type: application/json' \
    -X POST \
    -d \
  '{
    "id": "CVE-2020-16156",
    "packageName": "perl"
  }' \
    "https://<CONSOLE>/api/v<VERSION>/tags/Ignored/vuln"
  ```
  Refer to the following image that displays the tagged vulnerability:

  ![Tagged vulnerability in Ubuntu](https://cdn.twistlock.com/docs/api/Ubuntu-Vuln-Bin-Package-CVE-tagged-Ignored-Vuln.png)

- The RPM package lists CVEs on the available binary packages and not the source packages. 
  A CVE `CVE-2021-20305` found in only `gnutls` binary package in CentOS Linux Release 8.4.2105.

  ![Package information](https://cdn.twistlock.com/docs/api/CentOS-Vuln-Bin-Package-Info.png)

  Use the binary package name for tagging only when the source package is not available or NULL.

  ### cURL Request

  Refer to the following example cURL command that tags `Ignored` to the CVE `CVE-2021-20305` on the binary package `gnutls`:

  ```bash
  $ curl -k \
    -u <USER> \
    -H 'Content-Type: application/json' \
    -X POST \
    -d \
  '{
    "id": "CVE-2021-20305",
    "packageName": "gnutls"
  }' \
    "https://<CONSOLE>/api/v<VERSION>/tags/Ignored/vuln"
  ```
  Refer to the following image that displays the tagged vulnerability:
  
  ![Tagged vulnerability in CentOS](https://cdn.twistlock.com/docs/api/CentOS-Vuln-Bin-Package-CVE-tagged-Ignored-Vuln.png)

Consider the following scenarios when you want to tag a vulnerability to all packages and resources related to it:

- A CVE `CVE-2020-16156` is found in several packages such as `perl`, `perl-open`, `perl-macros`, `perl-libs`, and so on. You want to apply a tag `Ignored` to all the packages and resources.
 
 ![CVE information](https://cdn.twistlock.com/docs/api/Tagging-Only-Vulnerability.png)
 
  ### cURL Request

  Refer to the following example cURL command that tags `Ignored` to the CVE `CVE-2020-16156`:

  ```bash
  $ curl -k \
    -u <USER> \
    -H 'Content-Type: application/json' \
    -X POST \
    -d \
  '{
    "id": "CVE-2020-16156",
    "packageName": "*"
  }' \
    "https://<CONSOLE>/api/v<VERSION>/tags/Ignored/vuln"
  ```
  Refer to the following image that displays the tagged vulnerability:
  
  ![Tagged vulnerability](https://cdn.twistlock.com/docs/api/Tagged-Vulnerability.png)

- A CVE `CVE-2020-16156` is found in several packages such as `perl`, `perl-open`, `perl-macros`, `perl-libs`, and so on. You want to apply a tag `Ignored` to the resource type `image` but to all the packages and resources.

### cURL Request

  Refer to the following example cURL command that tags `Ignored` to the CVE `CVE-2020-16156` on the resource type `image` and to all the packages and resources.

  ```bash
  $ curl -k \
    -u <USER> \
    -H 'Content-Type: application/json' \
    -X POST \
    -d \
  '{
    "id": "CVE-2020-16156",
    "packageName": "*",
    "resourceType": "image",
    "resources": ["*"]
  }' \
    "https://<CONSOLE>/api/v<VERSION>/tags/Ignored/vuln"
  ```
- A CVE `CVE-2020-16156` is found in several packages such as `perl`, `perl-open`, `perl-macros`, `perl-libs`, and so on. You want to apply a tag `Ignored` to the resource type `host`and resource `servo-vmware71` but to all the packages.

### cURL Request

  Refer to the following example cURL command that tags `Ignored` to the CVE `CVE-2020-16156` on the resource type `host`, resource `servo-vmware71`, and to all the packages.

  ```bash
  $ curl -k \
    -u <USER> \
    -H 'Content-Type: application/json' \
    -X POST \
    -d \
  '{
    "id": "CVE-2020-16156",
    "packageName": "*",
    "resourceType": "host",
    "resources": ["servo-vmware71"]
  }' \
    "https://<CONSOLE>/api/v<VERSION>/tags/Ignored/vuln"
  ```

*Note:* A tag assignment is identified by the combination of the `id`, `packageName`, `resourceType`, and `tag` fields. Invoking the endpoint again for an existing tag assignment overrides the existing tag assignment for the resource. For example, invoking the endpoint consecutively with the following values:
1. `{"id":"CVE-1","packageName":"pkg","resourceType":"image","resources":["library/python:latest"],"tag":"In progress"}`
2. `{"id":"CVE-1","packageName":"pkg","resourceType":"image","resources":["library/python:latest"],"tag":"New Tag"}`
3. `{"id":"CVE-1","packageName":"pkg","resourceType":"host","resources":["devbox"],"tag":"New Tag"}`
4. `{"id":"CVE-1","packageName":"pkg","resourceType":"image","resources":["node:latest"],"tag":"New Tag"}`
Will result in the following tag assignments:
1. The first invocation creates the entry: "In progress", "CVE-1", "pkg", "image", "library/python:latest"
2. The second invocation creates a second (new) entry: "New Tag", "CVE-1", "pkg","image", "library/python:latest"
3. The third invocation creates a third (new) entry: "New Tag", "CVE-1", "pkg","host", "devbox"
4. The fourth invocation overrides the second entry with the following values: "New Tag", "CVE-1", "pkg", "image", "node:latest"

