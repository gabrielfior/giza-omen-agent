import argparse
import os
import random

import numpy as np
from addresses import ADDRESSES
from dotenv import find_dotenv, load_dotenv
from giza.agents import AgentResult, GizaAgent
from logging import getLogger

from giza.agents import AgentResult, GizaAgent
from logging import getLogger

import typer
from prediction_market_agent_tooling.deploy.agent import Answer, DeployableTraderAgent
from prediction_market_agent_tooling.gtypes import Probability
from prediction_market_agent_tooling.markets.agent_market import AgentMarket
from prediction_market_agent_tooling.markets.markets import MarketType





load_dotenv(find_dotenv())



os.environ["OMEN-AGENT_PASSPHRASE"] = os.environ.get("DEV_PASSPHRASE")
GNOSIS_RPC_URL = os.environ.get("GNOSIS_RPC_URL")


def create_agent(
    agent_id: int,  chain: str, contracts: dict, account_alias: str
):

    agent = GizaAgent.from_id(
    id=agent_id,
    contracts=contracts,
    chain=chain,
    account=account_alias,
    )
    return agent




 #Altough prediction is not used, we still use the agent to do a prediction, which we append with the coinflip decision as output
def predict(agent: GizaAgent, X: np.ndarray):

    X = X.reshape(1, 7)
    prediction = agent.predict(input_feed={"input": X}, verifiable=True, job_size="XL")

    decision = random.choice([True, False])
    return Answer(
            decision=decision,
            confidence=0.5,
            p_yes=Probability(float(decision)),
            reasoning="I flipped a coin to decide.",
        ), prediction





def get_pred_val(prediction: AgentResult):

    # This will block the executon until the prediction has generated the proof
    # and the proof has been verified
    return prediction.value


# Create Action


def agent_logic(
    agent_id : int,
    input1 : float,
    account="omen-agent",
    chain="ethereum:mainnet_fork:foundry",
):
    
    ## Change the AGENT_PASSPHRASE to be {AGENT-NAME}_PASSPHRASE
    os.environ["OMEN-AGENT_PASSPHRASE"] = os.environ.get("DEV_PASSPHRASE")

    # Create logger
    logger = getLogger("giza-omen-agent")

    # Load the addresses
    #example_token = ADDRESSES["Example_Token"]
    #example_amm = ADDRESSES["Example_AMM"]

    market = random.sample(markets, 1)
    # Load the data, this can be changed to retrieve live data
    file_path = "model/dummy_data.npy"
    X = np.load(file_path)

    # Fill this contracts dictionary with the contract addresses that our agent will interact with
    contracts = {
        "token": example_token,
        "amm": example_amm,
    }
    # Create the agent
    agent = create_agent(
        agent_id=agent_id,
        chain=chain,
        contracts=contracts,
        account_alias=account,
    )
    result = predict(agent, X)

    # If you want to wait until the verification to continue, uncomment the two following lines
    #predicted_value = get_pred_val(result)
    #logger.info("Verification complete, executing contract")
    logger.info(f"Result: {result}")

    with agent.execute() as contracts:
        logger.info("Verification complete, executing contract")

        ## AGENT LOGIC GOES HERE
        
        


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--agent-id", metavar="A", type=int, help="model-id")
    parser.add_argument("--input1", metavar="W", type=float, help="example_agent_argument")



    # Parse arguments
    args = parser.parse_args()


    agent_id = args.agent_id
    input1 = args.input1



    agent_logic(agent_id, input1)
