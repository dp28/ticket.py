class Branch():

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __eq__(self, other_branch):
        return (isinstance(other_branch, Branch)
            and self.name == other_branch.name)
