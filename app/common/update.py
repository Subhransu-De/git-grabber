from typing import List

from model import Repository
from os import makedirs
from os.path import join, exists
from .pull import pull
from .clone import clone


def update(username: str, repos: List[Repository]) -> None:
    output_dir: str = join('output', username)
    makedirs(output_dir, exist_ok=True)
    for repo in repos:
        repo_path: str = join(output_dir, repo.name)
        pull(repo, repo_path) if exists(repo_path) else clone(repo, repo_path)
