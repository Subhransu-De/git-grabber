# GitGrabber

[![CI/CD Pipeline](https://github.com/Subhransu-De/git-grabber/actions/workflows/docker-ci.yml/badge.svg?branch=main)](https://github.com/Subhransu-De/git-grabber/actions/workflows/docker-ci.yml)

GitGrabber is a tool designed to help you easily clone GitHub repositories.

## Features

- Effortlessly clone all repositories from a GitHub user or organization.

## Usage

To use GitGrabber, run the following command:

```sh
docker run --rm subhransude/gitgrabber --help
docker run --rm -v "$PWD:/app/output" subhransude/gitgrabber <username/organization_name>
```

## Installation

```sh
git clone git@github.com:Subhransu-De/git-grabber.git
cd git-grabber
uv sync --extra dev

uv run app --help
uv run app <username/organization_name>
```