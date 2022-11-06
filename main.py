from Agent import Agent

"""
    In this function i assumed that if option 1 and option 2 are the same for all players it returns False
    according to the lecture atleast one of the 'agents' needs to benefit from the second option for a pareto improvement
"""


def isParetoImprovement(agents: list[Agent], option1: int, option2: int) -> bool:
    count = 0
    for curr_agent in agents:
        if curr_agent.preference.get(option1) < curr_agent.preference.get(option2):
            return False
        elif curr_agent.preference.get(option1) == curr_agent.preference.get(option2):
            count += 1
    return count != len(agents)


"""
    In this function we need to check against all other options if there is a pareto improvement.
    If there is no pareto improvement then the option is pareto optimal and we'll return True.
    Note: in the loop there is no need to check if 'other_option' is the same option we're checking 
    because the pareto improvement function will return False if the options are the same.
"""


def isParetoOptimal(agents: list[Agent], option: int, allOptions: list[int]) -> bool:
    for other_option in allOptions:
        if isParetoImprovement(agents, other_option, option):
            return False
    return True


if __name__ == '__main__':
    # There are unittests for the functions
    pass
