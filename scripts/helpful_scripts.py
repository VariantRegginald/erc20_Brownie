from brownie import accounts, network, config, OurToken

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache",
    "hardhat",
    "local-ganache",
    "mainnet-fork"
]



def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])



##def get_account( index=None, id=None):
    #if index:
     #   return accounts[index]
    #if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
     #   print(accounts[0].balance())
      #  return accounts[0]
    #if id:
      #  return accounts.load(id)
    #if network.show_active() in config["networks"]:
      #  return accounts.add(config["wallets"]["from_key"])
    #return None


