class Branch():

    def __init__(self, ref):
        self.__ref = ref

    @property
    def ref(self):
        return self.__ref

    def __eq__(self, other_branch):
        return (isinstance(other_branch, Branch)
            and self.ref == other_branch.ref)
