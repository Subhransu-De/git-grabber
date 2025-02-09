from typing import List

from colorama import Fore, Style
from git import Repo, RemoteProgress
from model import Repository
from os import makedirs
from os.path import join, exists


def clone(username: str, repos: List[Repository]) -> None:
    output_dir: str = join('output', username)
    makedirs(output_dir, exist_ok=True)
    for repo in repos:
        repo_path: str = join(output_dir, repo.name)
        if exists(repo_path):
            print(
                f'{Fore.YELLOW}Repository {Style.BRIGHT}{repo.name}{Style.RESET_ALL}{Fore.YELLOW} exists in {Style.BRIGHT}{repo_path}{Style.RESET_ALL}'
            )
        else:
            print(f'{Fore.BLUE}Cloning: {Style.RESET_ALL}{repo.name} into {repo_path}')
            Repo.clone_from(repo.url, repo_path, progress=CloneProgress())
            print('\r', end='')
            print(f'{Fore.GREEN}Cloned: {Style.RESET_ALL}{repo.name} into {repo_path}')


class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()

    def update(self, op_code, cur_count, max_count=None, message=''):
        print('\r', end='')
        till_completion: float = (cur_count / max_count) * 100 if max_count else 0
        print(f'{Fore.YELLOW}Cloning: {till_completion:.2f}%{Fore.RESET}', end='')
