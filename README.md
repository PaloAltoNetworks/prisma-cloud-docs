![prisma_cloud_logo](https://user-images.githubusercontent.com/6518946/80754514-c7628f80-8af4-11ea-9e28-77b05d05bbaa.jpg)

# Prisma Cloud Compute Community Docs

Welcome to the docs project for [Prisma Cloud Compute](https://www.paloaltonetworks.com/prisma/cloud/compute-security).
Docs are a core part of the product and we build them just like we build the software in it - using modern collaboration platforms like GitHub and publishing them through a CI/CD pipeline with Jenkins.
As of May 2020, we've open sourced the docs so that anyone can contribute directly to them and see their work quickly go live for the whole community's benefit.
This repo is where that happens.

# Who?

Anyone can contribute the docs with simple pull requests.
All PRs are reviewed by product team members for accuracy and consistency and we'll collaborate with you on any questions or suggestions.
Because everything happens on GitHub, all your contributions are clearly visible and recognized.

# What?

PRs of any size or form are welcome, from simple clarifications of wording to entirely new how-to articles.
All content is in the open source [AsciiDoctor](https://asciidoctor.org/) format, which can be edited right in the GitHub browser IDE or any other text editor of your choice.

The Prisma Cloud Compute product team will continue to author docs for all new features and changes in each release.

# When?

We review PRs daily.
If there are no questions or further discussion, you'll see your changes live the next business day.
A Jenkins job runs nightly to publish the latest content.

# Where?

All Prisma Cloud Compute documentation is included in this repo.
Because the entire docs source is just text files in GitHub, it's easy to work with the way you want.
Docs are published in two places:

* Official docs: https://docs.paloaltonetworks.com/prisma/prisma-cloud.html
* Daily doc builds: https://docs.twistlock.com/docs/

# Why?

The best docs are written by people that really use and understand the technology.  While we on the product team are still intimately involved in creating and maintaining the docs, we know that everyone will benefit from the experiences and knowledge of the overall community.

# How?

1. Fork the repo.
2. Make your changes directly in the GitHub UI, or with your editor of choice and the git command line tool.
3. Submit your changes back to the repo as a pull request.

# Structure

Each guide has its own dedicated directory.
For example, the Administrator's Guide can be found in the top level `admin_guide/` dir.

Each guide has a topic map, written in YAML format.
Topic maps reference all the individual source files that make up a document.
They're also used to generate a document's navigation menu.

Source files are written in AsciiDoctor and have the `.adoc` extension.
Each source file holds one "article", which is rendered as a single page on the doc site.

Source for the Administrator's Guide uses conditional content to target either Compute Edition (self-hosted) or Enterprise Edition (SaaS).
Content that only applies to one or the other is fenced with AsciiDoctor's `ifdef` and `endif` directives.

For Compute Edition-specific content:

```
ifdef::compute_edition[]
Download and run Console in your own environment.
endif::compute_edition[]
```

For Enterprise Edition-specific content:

```
ifdef::prisma_cloud[]
Palo Alto Networks runs Console for you.
endif::prisma_cloud[]
```

# Building the site locally

The site uses a Red Hat project called [AsciiBinder](https://github.com/redhataccess/ascii_binder) in conjunction with our own package `ascii_binder_pan-0.0.00.1.gem`, located at the root of this repo.

As you create and edit content, we recommend making a local build to check the rendering.
To do so, complete the following steps.
Instructions are geared for macOS.

1. Ensure that Ruby is installed.

    ```bash
    ruby -v
    ```

1. If you haven't already installed pyenv and pyenv-virtualenv, go ahead and do so now.

    ```bash
    brew install pyenv
    brew install pyenv-virtualenv
    ```

1. Initialize pyenv and virtualenv.

    ```bash
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```

1. Use pyenv to install Python 3.7.4.

    ```bash
    pyenv install 3.7.4
    ```

1. Install Asciidoctor.

    ```bash
    brew install asciidoctor
    ````

1. Install `ascii_binder` v0.1.15.1.

    ```bash
    sudo gem install ascii_binder -v 0.1.15.1
    ```

1. Navigate into the `_build` directory and use the following command to install our custom `ascii_binder` package. 

    ```bash
    cd _build/
    sudo gem install -V ./ascii_binder_pan-0.0.00.1.gem
    ```

1. Return to the root directory and run the `build_site.sh` script as follows

    ```bash
    cd ..
    ./build_site.sh
    ```

1. Open the generated site using the following command.

    ```bash
    open output/_package/main/index.html
    ```
