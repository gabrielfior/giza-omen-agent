# Giza Omen Agent

An automated betting tool for Omen prediction markets on the Gnosis Chain.

Next steps


| Task                           | Description                                                                                                                                                                                                                                                                                         | Status      |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Dependencies                   | Fix dependency resolution between giza-actions, giza-cli and PMAT                                                                                                                                                                                                                                   | Done        ||
| Basic functionality            | Implement basic functionality using tasks and actions from Giza SDK                                                                                                                                                                                                                                 | IN PROGRESS |
| Coinflip agent                 | Write simple agent that outputs yes/no (dummy model) based on random chance (coinflip)                                                                                                                                                                                                              | Done        |
| Deploy Coinflip agent          | Deploy coinflip agent using Giza                                                                                                                                                                                                                                                                    | ToDo        |
| Add Omen-specific logic        | Add Omen-specific logic into agent using Prediction-Market-Agent-Tooling existing functions                                                                                                                                                                                                         | Done        |
| Improve agent prediction logic | Extend agent's capabilities, from simple random prediction to possibly using LLMs for deciding which market to bet on / how much to bet on ([example](https://github.com/gnosis/prediction-market-agent/blob/main/prediction_market_agent/agents/think_thoroughly_agent/think_thoroughly_agent.py)) | ToDo        |
| Verifiable ML                  | Add verification of agent's prediction using Giza                                                                                                                                                                                                                                                   | ToDo        |
 
