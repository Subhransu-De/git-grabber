from colorama import Fore, Style
from git import GitCommandError, Repo, RemoteProgress
from model import Repository


def clone(repo: Repository, repo_path: str) -> None:
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
