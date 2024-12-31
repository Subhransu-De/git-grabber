from typing import Dict, List, Optional
import requests
import argparse
import os
from git import Repo
from colorama import Fore, Style, init


def get_repos(username: str) -> Optional[List[Dict[str, str]]]:
    url: str = f'https://api.github.com/users/{username}/repos'
    response: requests.Response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        return [
            {'name': repo['name'], 'ssh_url': repo['ssh_url']}
            for repo in [repo for repo in repos if 'ssh_url' and 'name' in repo]
        ]
    else:
        return None


def clone_repos(username: str, repos: List[Dict[str, str]]) -> None:
    output_dir: str = os.path.join('output', username)
    os.makedirs(output_dir, exist_ok=True)

    for repo in repos:
        repo_url: str = repo['ssh_url']
        repo_name: str = repo['name']
        repo_path: str = os.path.join(output_dir, repo_name)
        if os.path.exists(repo_path):
            print(
                f'{Fore.YELLOW}Repository {Style.BRIGHT}{repo_name}{Style.RESET_ALL}{Fore.YELLOW} exists in {Style.BRIGHT}{repo_path}{Style.RESET_ALL}'
            )
        else:
            print(
                f'{Fore.GREEN}Cloning {Style.BRIGHT}{repo_name}{Style.RESET_ALL}{Fore.GREEN} into {Style.BRIGHT}{repo_path}{Style.RESET_ALL}'
            )
            Repo.clone_from(repo_url, repo_path)


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Get GitHub repositories of a user')
    parser.add_argument('username', type=str, help='GitHub username')
    args: argparse.Namespace = parser.parse_args()

    repos: Optional[List[Dict[str, str]]] = get_repos(args.username)
    if repos:
        clone_repos(args.username, repos)
    else:
        print('Failed to retrieve repositories')


if __name__ == '__main__':
    init(autoreset=True)
    main()
