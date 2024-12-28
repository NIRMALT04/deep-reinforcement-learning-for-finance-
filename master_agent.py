# master_agent/master_agent.py

import ray
from agents.billing_agent import BillingAgent
from agents.tax_agent import TaxAgent
from agents.partner_performance_agent import PartnerPerformanceAgent
from agents.client_summary_agent import ClientSummaryAgent
from environmentt.shared_environment import SharedEnvironment

class MasterAgent:
    def __init__(self, config):
        self.agents = {
            "billing": BillingAgent(config),
            "tax": TaxAgent(config),
            "partner_performance": PartnerPerformanceAgent(config),
            "client_summary": ClientSummaryAgent(config),
        }
        self.environment = SharedEnvironment(config)

    def train_all_agents(self):
        for agent in self.agents.values():
            agent.train()

    def get_actions(self, observations):
        actions = {}
        for name, agent in self.agents.items():
            actions[name] = agent.get_action(observations[name])
        return actions
