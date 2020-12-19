class Actions:

    def __init__(self, dictionary):
        for _ in dictionary.items():
            setattr(self, _[0], _[1])

    def do(self, action):
        return getattr(self, action)()
