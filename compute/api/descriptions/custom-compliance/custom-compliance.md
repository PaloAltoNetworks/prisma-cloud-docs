Custom image checks give you a way to write and run your own compliance checks to assess, measure, and enforce security baselines in your environment.
Although Prisma Cloud Compute supports OpenSCAP and XCCDF, these frameworks are complicated, and they can be overkill when all you want to do is run a simple check.
Prisma Cloud Compute lets you implement your own custom image checks with simple scripts.

A custom image check consists of a single script.
The script’s exit code determines the result of the check, where 0 is pass and 1 is fail.
Scripts are executed in the container’s default shell.
For many Linux container images, the default shell is bash, but that’s not always the case.
For Windows container images, the default shell is `cmd.exe`.
