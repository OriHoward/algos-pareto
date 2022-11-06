from unittest import TestCase
from Agent import Agent
from main import *


class Test(TestCase):
    def setUp(self) -> None:
        self.all_options = [1, 2, 3, 4, 5]
        self.ami = Agent({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
        self.tami = Agent({1: 3, 2: 1, 3: 2, 4: 5, 5: 4})
        self.rami = Agent({1: 3, 2: 5, 3: 5, 4: 1, 5: 1})
        self.agents = [self.ami, self.tami, self.rami]

    def test_is_pareto_improvement(self):
        self.assertFalse(isParetoImprovement(self.agents, 1, 1))
        self.assertFalse(isParetoImprovement(self.agents, 2, 2))
        self.assertFalse(isParetoImprovement(self.agents, 3, 3))
        self.assertFalse(isParetoImprovement(self.agents, 1, 2))
        self.assertFalse(isParetoImprovement(self.agents, 1, 3))
        self.assertFalse(isParetoImprovement(self.agents, 1, 4))
        self.assertFalse(isParetoImprovement(self.agents, 1, 5))
        self.assertFalse(isParetoImprovement(self.agents, 2, 1))
        self.assertFalse(isParetoImprovement(self.agents, 2, 3))
        self.assertFalse(isParetoImprovement(self.agents, 2, 4))
        self.assertFalse(isParetoImprovement(self.agents, 2, 5))
        self.assertFalse(isParetoImprovement(self.agents, 3, 1))
        self.assertTrue(isParetoImprovement(self.agents, 3, 2))
        self.assertFalse(isParetoImprovement(self.agents, 3, 4))
        self.assertFalse(isParetoImprovement(self.agents, 3, 5))
        self.assertFalse(isParetoImprovement(self.agents, 4, 1))
        self.assertFalse(isParetoImprovement(self.agents, 4, 2))
        self.assertFalse(isParetoImprovement(self.agents, 4, 3))
        self.assertFalse(isParetoImprovement(self.agents, 4, 5))
        self.assertFalse(isParetoImprovement(self.agents, 5, 1))
        self.assertFalse(isParetoImprovement(self.agents, 5, 2))
        self.assertFalse(isParetoImprovement(self.agents, 5, 3))
        self.assertFalse(isParetoImprovement(self.agents, 5, 4))

    def test_is_pareto_optimal(self):
        self.assertTrue(isParetoOptimal(self.agents,1,self.all_options))
        self.assertFalse(isParetoOptimal(self.agents,2,self.all_options))
        self.assertTrue(isParetoOptimal(self.agents,3,self.all_options))
        self.assertTrue(isParetoOptimal(self.agents,4,self.all_options))
        self.assertTrue(isParetoOptimal(self.agents,5,self.all_options))