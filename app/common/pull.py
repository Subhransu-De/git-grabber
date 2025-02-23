from colorama import Fore, Style
from git import GitCommandError, Repo, RemoteProgress
from model import Repository


def pull(repo: Repository, repo_path: str) -> None:
    try:
        git_repo = Repo(repo_path)
        current_branch = git_repo.active_branch.name
        origin = git_repo.remotes.origin
        old_commit = git_repo.head.commit
        has_stash: bool = False
        if git_repo.is_dirty(untracked_files=True):
            print(f'\rStashing changes in: {repo.name} 📦', end='', flush=True)
            git_repo.git.stash('save', 'Automatic stash before pull')
            has_stash = True
        git_repo.git.checkout(repo.default_branch)
        origin.pull(progress=CloneProgress(repo.name))
        new_commit = git_repo.head.commit
        commit_count = len(list(git_repo.iter_commits(f'{old_commit}..{new_commit}')))
        if current_branch != repo.default_branch:
            git_repo.git.checkout(current_branch)
        if has_stash:
            print(f'\rApplying stashed changes in: {repo.name} 📦', end='', flush=True)
            git_repo.git.stash('pop')
        print(f'\r{Fore.GREEN}Pulled: {Style.RESET_ALL}{repo.name} into {repo_path} ({commit_count} new commits)  ✅')
    except GitCommandError as gce:
        print(f'\n{Fore.RED}Failed to pull {Style.BRIGHT}{repo.name}{Style.RESET_ALL}{Fore.RED}: {gce}')


class CloneProgress(RemoteProgress):
    def __init__(self, repo_name: str):
        super().__init__()
        self.repo_name = repo_name

    def update(self, op_code, cur_count, max_count=None, message=''):
        print(f'\rCloning: {self.repo_name} ⌛️', end='', flush=True)
