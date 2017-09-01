import requests
from ticket import config


def save(pull_request):
    response = _post(pull_request.repo, dict(
        title=pull_request.title,
        body=pull_request.body,
        head=pull_request.head_branch.name,
        base=pull_request.base_branch.name
    ))
    print(response)
    pull_request.url = response.get('url')


def _post(repo, data):
    url = _build_url(repo.name)
    headers = _build_headers()
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    print(response)
    print(response.json())
    return response.json()


def _build_url(repo_name):
    return 'https://api.github.com/repos/{owner}/{repo}/pulls'.format(
        owner=config.GITHUB_REPO_OWNER,
        repo=repo_name
    )


def _build_headers():
    return dict(
        Accept='application/vnd.github.v3+json',
        Authorization='token {}'.format(config.GITHUB_API_KEY)
    )
