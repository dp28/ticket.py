from ticket.git.interface import repos

def get_current():
    return Repo(repos.get_current_repo_name())


class Repo():

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __eq__(self, other_repo):
        return isinstance(other_repo, Repo) and self.name == other_repo.name
