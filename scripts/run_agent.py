import os
import random
from dotenv import load_dotenv
load_dotenv()

import typer
from prediction_market_agent_tooling.deploy.agent import Answer, DeployableTraderAgent
from prediction_market_agent_tooling.gtypes import Probability
from prediction_market_agent_tooling.markets.agent_market import AgentMarket
from prediction_market_agent_tooling.markets.markets import MarketType
import typing as t



class DeployableCoinFlipAgent(DeployableTraderAgent):
    def pick_markets(self, markets: t.Sequence[AgentMarket]) -> t.Sequence[AgentMarket]:
        return random.sample(markets, 1)

    def answer_binary_market(self, market: AgentMarket) -> Answer | None:
        decision = random.choice([True, False])
        return Answer(
            decision=decision,
            confidence=0.5,
            p_yes=Probability(float(decision)),
            reasoning="I flipped a coin to decide.",
        )


def main():
    print ('start')
    agent = DeployableCoinFlipAgent()
    market_type = MarketType.OMEN
    agent.run(market_type)
    print ('end')

if __name__ == "__main__":
    typer.run(main)
