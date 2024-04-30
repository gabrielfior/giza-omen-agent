from prediction_market_agent_tooling.gtypes import xDai
from prediction_market_agent_tooling.tools.web3_utils import xdai_to_wei
from web3.types import Wei


class CoinflipAgent:
    # ToDo - Place Omen specific functions here
    # ToDo - Schedule this via Giza platform
    pass

class XGBoostAgent:

    def pick_market(self):
        # Todo - call LLM, call a registered model (e.g. xgboost) that was trained on a specific kind of question (for ex,
        #  "Will it rain in Berlin on May 24th" should be forwarded to a model that was trained on weather data)
        #  Non-verifiable for now as of 30.04.24
        pass

    def pick_outcome_of_market(self):
        # ToDo - Call model (for ex xgboost) and ask for a yes/no prediction.
        # verifiable
        pass

    def define_bet_amount(self) -> Wei:
        # keep it fixed in the beginning - this could be changed in the future and would affect the profitability of
        # the model (for ex, it should bet larger amounts if more certain and/or if market view deviates from agent's
        # view)
        return xdai_to_wei(xDai(0.01))