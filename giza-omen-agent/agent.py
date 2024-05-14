import argparse
import os


import numpy as np
from addresses import ADDRESSES
from dotenv import find_dotenv, load_dotenv
from giza_actions.action import action
from giza_actions.agent import AgentResult, GizaAgent
from giza_actions.task import task
from prefect import get_run_logger



load_dotenv(find_dotenv())



os.environ["CARBONABLE-AGENT_PASSPHRASE"] = os.environ.get("DEV_PASSPHRASE")





@task(name="Create a Giza agent using Agent_ID")
def create_agent(
    agent_id: int,  chain: str, contracts: dict, account_alias: str
):
    """
    Create a Giza agent for the Pendle protocol
    """
    agent = GizaAgent.from_id(
    id=agent_id,
    contracts=contracts,
    chain=chain,
    account=account_alias,
    )
    return agent



## Change to reflect the input data dimensions, currently fit for dummy_model
@task(name="Run the model")
def predict(agent: GizaAgent, X: np.ndarray):
    """
    Predict the APR one week later.

    Args:
        X (np.ndarray): Input to the model.

    Returns:
        int: Predicted value.
    """
    X = X.reshape(1, 7)
    prediction = agent.predict(input_feed={"input": X}, verifiable=True, job_size="XL")

    return prediction


@task(name="Verify the inference proof and return the predicted value")
def get_pred_val(prediction: AgentResult):
    """
    Get the value from the prediction.

    Args:
        prediction (dict): Prediction from the model.

    Returns:
        int: Predicted value.
    """
    # This will block the executon until the prediction has generated the proof
    # and the proof has been verified
    return prediction.value


# Create Action
@action(log_prints=True)
def agent_logic(
    agent_id : int,
    input1 : float,
    account="carbonable-agent",
    chain="ethereum:mainnet_fork:foundry",
):
    
    ## Change the AGENT_PASSPHRASE to be {AGENT-NAME}_PASSPHRASE
    os.environ["OMEN-AGENT_PASSPHRASE"] = os.environ.get("DEV_PASSPHRASE")

    # Create logger
    logger = get_run_logger()

    # Load the addresses
    example_token = ADDRESSES["Example_Token"]
    example_amm = ADDRESSES["Example_AMM"]


    # Load the data, this can be changed to retrieve live data
    file_path = "model/data_array.npy"
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