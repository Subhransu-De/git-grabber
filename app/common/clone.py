from typing import List

from colorama import Fore, Style
from git import GitCommandError, Repo, RemoteProgress
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
            print(f'{Fore.BLUE}Cloning: {Style.RESET_ALL}{repo.name} into {repo_path}', end='')
            try:
                Repo.clone_from(repo.url, repo_path, branch=repo.default_branch, progress=CloneProgress(repo.name))
                print(f'\r{Fore.GREEN}Cloned: {Style.RESET_ALL}{repo.name} into {repo_path}  ✅')
            except GitCommandError as gce:
                print(f'\n{Fore.RED}Failed to clone {Style.BRIGHT}{repo.name}{Style.RESET_ALL}{Fore.RED}: {gce}')


class CloneProgress(RemoteProgress):
    def __init__(self, repo_name: str):
        super().__init__()
        self.repo_name = repo_name

    def update(self, op_code, cur_count, max_count=None, message=''):
        print(f'\rCloning: {self.repo_name} ⌛️', end='', flush=True)
