from typing import List
import json
from urllib import request, error

from model import Repository


def fetch_repositories(username: str) -> List[Repository]:
    url = f'https://api.github.com/users/{username}/repos'
    try:
        with request.urlopen(url) as response:
            if response.status == 200:
                repos = json.loads(response.read())
                return [
                    Repository(name=repo['name'], url=repo['clone_url'], default_branch=repo['default_branch'])
                    for repo in [
                        repo
                        for repo in repos
                        if ('clone_url' and 'name' in repo) and (repo['fork'] is False) and (repo['size'] > 0)
                    ]
                ]
            else:
                exit(f'Failed to retrieve repositories: {response.status}')
    except error.URLError as e:
        exit(f'Failed to retrieve repositories: {e}')
