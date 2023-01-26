import asyncio
import json

from starknet_py.contract import Contract
from starknet_py.net import AccountClient
from starknet_py.net.gateway_client import GatewayClient

# Local network
from starknet_py.net.models import StarknetChainId
from starknet_py.transactions.declare import make_declare_tx

async def setup_accounts():
    # local_network_client = GatewayClient("http://127.0.0.1:5050/")
    local_network_client = GatewayClient("https://alpha4.starknet.io")
    # Deploys an account on devnet and returns an instance
    account_client = await AccountClient.create_account(
        client=local_network_client, chain=StarknetChainId.TESTNET
    )
    return local_network_client, account_client


async def declare_contract(admin_client, contract_src):
    declare_tx = make_declare_tx(compilation_source=[contract_src])
    return await admin_client.declare(declare_tx)


async def setup_contracts(network_client, admin_client):

    deployment_result = await Contract.deploy(
        network_client,
        compilation_source=["src/contracts/starkRocks.cairo"],
        constructor_args=[
            0x487562656C65,
            0x48626C,
            0x07CB66E9ED0AF79cdA533c96221AE8E2651DD7D49A52bDC4d7c2c54f1b66901a,
            [0x697066733A2F2F71657271657866617861716572,0x716571776578686A6861686A786A6868616A77736478786164],
            0x2E6A736F6E,
            0x049D36570D4e46f48e99674bd3fcc84644DdD6b96F7C741B1562B82f9e004dC7,
            0x38D7EA4C68000,
            0x22a06e6dccc968c86e1a1068728b33ee120f00aa5c81e159677d6e4a06de10e,
            [
            0x073298A2CA8b06596D7bc85311c1C9d06458664A02a341655dEe4e663600aC53,
            0x007C60e6e6217eA0f34D9EcE7edC5b50223c434Db4f95260adC76c04c4cb417B,
            0x02b66c98bc96abe652b3655ee0d3affaaf57c1f9d882824a589df29e4636d88b,
            0x02Ad125d6B115d8259872847554dc54b5cf7dCdD62137450Aea179EBCE18003C,
            0x06Dc4E621706B0813db26437855Ed3AD00881B789a6bCe6413f7Dca9D0086BA4,
            0x06a03bCC0f6c48B4c897d41309133BB1C314a8adF2A86f6283a848966076ED89,
            0x016F204a08EB90b486cb9Bd938B13Da02B45F9cBB86Ee82816020ABC8208C491,
            0x015f1B483Ee529455928c7A165c571684Bc6e766A6Feb9061245fD3f19bb703f,
            0x03b041c0CbbA985989181c46C220A38715e541d8256C151dDB532AadA8380647,
            0x041D84F7BEB65b09F0ef88edd7f1192B960CF24a4e942d9a490DC14567120bB2,
            0x056f64B6f6552a54Ee79762b0abcE7BDCa6999F23Ea869a3f8718840A263617B,
            0x06733e297fE300F78F48c7106AD550626377Aa732CEF360867218C08a536ea5E,
            0x0734e0d13024764b8adca14964c69803a2a067f0491b9459265e846d095c3635,
            0x049e2ab78DE675841D06e838C0f55f6452e5CA08ea2eA2ba23A41414C3F847A9,
            0x02272a9320DCEcdc22e9F6A34A03ED07795a6B1045301bEef4dF65bFB3907a73,
            0x015D48c44B88463932B8DC1Fd5df64f71253251d3A46103b45C5D4c97f3d1051,
            0x020218CB44454d932B18D82Fb5CB60c6f5FB7B545f65aB3db8a62b0D65026eD0,
            0x0091460cA228a6e6b20469De1A876394b34c8457688252E743530E1051023848,
            0x06bbed09010B0082817536A08f1Fed5199560169a8AB16572cFCA9B67582221d,
            0x06a0e048d7d1039129c464656df218f09476068bdb4caabab935915b4372b8a5,
            0x0114111CE8BEee7DB55bC152A74AA62e77A475DecD8713D1cD12A5449838cBb9,
            0x07CB66E9ED0AF79cdA533c96221AE8E2651DD7D49A52bDC4d7c2c54f1b66901a
            ],
        ],
    )
    # Wait for the transaction to be accepted
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