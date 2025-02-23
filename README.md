# GitGrabber

GitGrabber is a tool designed to help you easily clone GitHub repositories.

## Features

- Clone all repositories of an github user or organization

## Installation



## Usage

To use GitGrabber, run the following command:

```sh
docker run --rm subhransude/gitgrabber --help
docker run --rm -v "$PWD/output:/app/output" subhransude/gitgrabber <username/organization_name>
```

```sh
uv run app <username/organization_name>
```

For a list of available commands, use:

```sh
uv run app --help
```

### Installation for development

To install GitGrabber for development, run the following command:

```sh
git clone git@github.com:Subhransu-De/git-grabber.git
cd git-grabber
uv sync --extra dev
```