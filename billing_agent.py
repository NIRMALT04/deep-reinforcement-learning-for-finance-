# agents/billing_agent.py

import ray
from ray.rllib.algorithms.ppo import PPO

class BillingAgent:
    def __init__(self, config):
        self.policy = PPO(config=config)

    def train(self):
        return self.policy.train()

    def get_action(self, observation):
        return self.policy.compute_action(observation)
