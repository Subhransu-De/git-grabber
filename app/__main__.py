import argparse
from os import system
from colorama import init

from github import fetch_repositories as gh_fetch_repo
from common import update


def setup() -> None:
    # https://git-scm.com/docs/git-config#Documentation/git-config.txt-safedirectory
    system('git config --global --add safe.directory "*"')


def main() -> None:
    try:
        parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Get GitHub repositories of a user')
        parser.add_argument('username', type=str, help='GitHub username')
        args: argparse.Namespace = parser.parse_args()
        [
            update(args.username, repos)
            if len(repos := gh_fetch_repo(args.username)) > 0
            else print('No public repositories found!')
        ]
    except KeyboardInterrupt:
        print('\nGitgrabber interrupted. Exiting gracefully.')
        exit(0)


if __name__ == '__main__':
    init(autoreset=True)
    setup()
    main()
