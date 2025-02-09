from typing import List
import json
from urllib import request, error

from model import Repository


def fetch_repositories(username: str) -> List[Repository]:
    url = f'https://api.github.com/users/{username}/repos'
    try:
        with request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                repos = json.loads(data)
                return [
                    Repository(name=repo['name'], ssh=repo['ssh_url'])
                    for repo in [repo for repo in repos if 'ssh_url' and 'name' in repo]
                ]
            else:
                exit(f'Failed to retrieve repositories: {response.status}')
    except error.URLError as e:
        exit(f'Failed to retrieve repositories: {e}')
