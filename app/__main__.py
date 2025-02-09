import argparse
from colorama import init

from github import fetch_repositories as gh_fetch_repo
from common import clone


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Get GitHub repositories of a user')
    parser.add_argument('username', type=str, help='GitHub username')
    args: argparse.Namespace = parser.parse_args()
    [
        clone(args.username, repos)
        if len(repos := gh_fetch_repo(args.username)) > 0
        else print('No public repositories found!')
    ]


if __name__ == '__main__':
    init(autoreset=True)
    main()
