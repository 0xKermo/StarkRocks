import asyncio
import json

from starknet_py.contract import Contract
from starknet_py.net import AccountClient,KeyPair
from starknet_py.net.account.account import Account
from starknet_py.net.gateway_client import GatewayClient

# Local network
from starknet_py.net.models import StarknetChainId
from starknet_py.transactions.declare import make_declare_tx

async def setup_accounts():
    # local_network_client = GatewayClient("http://127.0.0.1:5050/")
    local_network_client = GatewayClient("https://alpha4.starknet.io")
    # Deploys an account on devnet and returns an instance
    account_client = Account(
        client=local_network_client,
        address="0x07A6A583344fbc4055619625d7FC6d1788C8B42653b8f9D659a47c6BcDb553C3",
        key_pair=KeyPair.from_private_key(),
        chain=StarknetChainId.TESTNET,
    )
    
    return local_network_client, account_client


async def declare_contract(admin_client, contract_src):
    declare_tx = make_declare_tx(compilation_source=[contract_src])
    return await admin_client.declare(declare_tx)


async def setup_contracts(network_client, admin_client):
    f = open("/Users/berkdehrioglu/git/StarkRocks/starki_compiled.json", "r")
    compiled = f.read()
    nonce = await admin_client.get_nonce()
    print(nonce)
    declare_result = await Contract.declare(account=admin_client,compiled_contract=compiled,max_fee=int(1e16))
    await declare_result.wait_for_acceptance()
    print(declare_result.hash)
    print(declare_result.class_hash)
    deployment_result = await declare_result.deploy(
        constructor_args={
            "name": 0x487562656C65,
            "symbol": 0x48626C,
            "owner": 0x07A6A583344fbc4055619625d7FC6d1788C8B42653b8f9D659a47c6BcDb553C3,
            "base_uri": [0x697066733a2f2f62616679626569647873706f726e776d6b6c70656e6c71,0x3269613575353473376f6b696f36647979686f786b707670717079667032,0x7a64776d37692f],
            "json_extension": 0x2E6A736F6E,
            "currency_address": 0x049D36570D4e46f48e99674bd3fcc84644DdD6b96F7C741B1562B82f9e004dC7,
            "mint_price": 0xE35FA931A0000,
            "public_mint_price": 0x1C6BF526340000,
            "root": 0x1235501611595dbcf1fe0633b91b3ddc8d53158c2174227540cfe2da079ea62
        },
        max_fee=int(1e16))
    # Wait for the transaction to be accepted
    print(deployment_result.hash)
    await deployment_result.wait_for_acceptance()
    erc721 = deployment_result.deployed_contract
    print("contract address",erc721.address)
    return erc721



async def main():
    local_network_client, account_client = await setup_accounts()
    erc721_contract = await setup_contracts(local_network_client, account_client)
    # (totalSupply,) = await erc721_contract.functions["totalSupply"].call()
    # print("total Supply", totalSupply)
    # (baseUri,) = await erc721_contract.functions["baseUri"].call()
    # print("base uri", baseUri)
    # (balance,) = await erc721_contract.functions["balanceOf"].call(0x737461726B526F636B73)
    # print("balance ", balance)
    # (balance1,) = await erc721_contract.functions["balanceOf"].call(0x73526B73)
    # print("balance1 ", balance1)
    # (balance2,) = await erc721_contract.functions["balanceOf"].call(0x73526B735)
    # print("balance2 ", balance2)
    # (owner,) = await erc721_contract.functions["ownerOf"].call(1)
    # print("owner ", owner)
    # (owner1,) = await erc721_contract.functions["ownerOf"].call(2)
    # print("owner ", owner1)
    # (owner2,) = await erc721_contract.functions["ownerOf"].call(3)
    # print("owner ", owner2)
    # (owner3,) = await erc721_contract.functions["ownerOf"].call(4)
    # print("owner ", owner3)
    # (owner4,) = await erc721_contract.functions["ownerOf"].call(5)
    # print("owner ", owner4)
    # (owner5,) = await erc721_contract.functions["ownerOf"].call(6)
    # print("owner ", owner5)
    # (baseuri2,) = await erc721_contract.functions["set_base_uri"].invoke([0x123,0x2312])
    # print("baseuri2",baseuri2)
if __name__ == "__main__":
    asyncio.run(main())