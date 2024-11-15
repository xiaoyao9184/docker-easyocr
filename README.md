# Docker EasyOCR

A Docker image built through GitHub Actions with Git commit version tags.

## Why

I discovered that EasyOCR provides a Dockerfile but does not offer a prebuilt Docker image for running demos.
Additionally, its models are hosted on GitHub Releases and downloaded at runtime, which makes offline mode challenging.
Hosting the models on HuggingFace Hub would enable local caching and leverage HuggingFace's self-hosted mirror for efficient downloads.

After reviewing the following resources:

- [tomofi/EasyOCR](https://huggingface.co/spaces/tomofi/EasyOCR)
- [felflare/EasyOCR-weights](https://huggingface.co/felflare/EasyOCR-weights/tree/main)
- [jhgmods/easyocr-models](https://huggingface.co/jhgmods/easyocr-models/tree/main)

This project uses GitHub Actions, Docker Hub, and HuggingFace Hub to build and publish Docker images and host models.
The goal is to maintain a clean and automated process without requiring custom configuration files.

## Tags

Docker images for this project are published on Docker Hub under the repository [xiaoyao9184/easyocr](https://hub.docker.com/r/xiaoyao9184/easyocr).

The dependent models are hosted on HuggingFace Hub at [xiaoyao9184/easyocr](https://huggingface.co/xiaoyao9184/easyocr).

Since this project references the EasyOCR project via a Git submodule,
it cannot monitor push events in the EasyOCR repository and therefore cannot automatically create images for every commit.
A practical workaround is to manually trigger the GitHub Action and tag the image with the commit ID.
For more details, see this article: [Set Dynamic Parameters in GitHub Workflows](https://damienaicheh.github.io/github/actions/2022/01/20/set-dynamic-parameters-github-workflows-en.html).

The default image naming format is `${DOCKERHUB_USERNAME}/easyocr`.

### Tagging Strategy

1. **Commit-Based Tagging**
   The tag uses the input parameter `commit_id`, which can be either a branch name or a commit ID.
   - When the [docker-image-tag-commit](./.github/workflows/docker-image-tag-commit.yml) job is manually triggered, you can specify the `commit_id`.
   - If the job is triggered by a submodule update push, the default branch name `master` will be used instead of the `commit_id`.
   - This job also generates a tag with the shortened commit ID.

2. **Version-Based Tagging**
   If the [docker-image-tag-version](./.github/workflows/docker-image-tag-version.yml) job is triggered with the `easyocr_version` parameter (set to a PyPI EasyOCR version),
   the build will use the EasyOCR package published on PyPI.
   The resulting image will be tagged with the `easyocr_version`.

Currently, only the `linux/amd64` platform is supported.

## Changes

You can fork this project and build your own Docker image. To do so, you need to provide the following variables:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

For more details, see [this guide](https://github.com/docker/login-action#docker-hub).

Additionally, you need to provide your own HuggingFace account for storing the models. The required variables are:
- `HF_USERNAME`
- `HF_TOKEN`
