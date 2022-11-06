class Agent:

    # The key represents the option number
    def __init__(self, preference: dict[int, float]):
        self.preference: dict[int, float] = preference

    def value(self, option: int) -> float:
        return self.preference[option]
