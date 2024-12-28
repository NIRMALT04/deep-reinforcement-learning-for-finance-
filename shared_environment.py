# environment/shared_environment.py

import gym
from gym import spaces

class SharedEnvironment(gym.Env):
    def __init__(self, config=None):
        super(SharedEnvironment, self).__init__()
        self.action_space = spaces.Discrete(10)  # Example: 10 discrete actions
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=float)  # Example observation space
        self.state = self.reset()

    def reset(self):
        self.state = self.initialize_state()
        return self.state

    def step(self, action):
        next_state = self.state  # Update your state here
        reward = self.calculate_reward(action)
        done = self.is_done()
        return next_state, reward, done, {}

    def initialize_state(self):
        return [0.0, 0.0, 0.0, 0.0]

    def calculate_reward(self, action):
        return 1.0  # Reward logic

    def is_done(self):
        return False  # Termination condition
