from ticket.github.pull_request import PullRequest


def create_pull_request(ticket, repo):
    return PullRequest(ticket, repo)
