from giza_actions.action import action
from giza_actions.task import task
from prediction_market_agent_tooling.markets.omen.omen import OmenCollateralTokenContract
from prediction_market_agent_tooling.tools.balances import get_balances
from web3 import Web3
from prediction_market_agent_tooling.markets.omen.omen_subgraph_handler import OmenSubgraphHandler


print ('start')
# Replicator
gnosis_agent_public_key = Web3.to_checksum_address("0x993DFcE14768e4dE4c366654bE57C21D9ba54748")
contract = OmenCollateralTokenContract()
wxdai_balance = contract.balanceOf(gnosis_agent_public_key)
print (f'wxDAI Balance of agent - {wxdai_balance}')

# Example market previously created by replicator
market_id = Web3.to_checksum_address("0x1ebb36703b1717a888573b53c1582feaebcc95a8")
market = OmenSubgraphHandler().get_omen_market_by_market_id(market_id)
print (f'market {market.title}')

# Additional functionality to be implemented - bet on market, redeem funds, etc
print ('end')