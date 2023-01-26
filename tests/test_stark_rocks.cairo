%lang starknet
from starkware.cairo.common.uint256 import Uint256

@contract_interface
namespace IStarkRock {
    func royalityInfo(sale_price: Uint256) -> (receiver: felt, royalitytAmount: Uint256) {
    }

    func isWhitelistMintActive() -> (res: felt) {
    }

    func isPublicMintActive() -> (res: felt) {
    }

    func baseUri() -> (uri_len: felt, uri: felt*) {
    }

    func currencyAddress() -> (address: felt) {
    }

    func mintPrice() -> (price: Uint256) {
    }

    func totalSupply() -> (supply: felt) {
    }

    func merkleRoot() -> (root: felt) {
    }
    
    func _teamMint( index:felt, wallet_addresses_len:felt, wallet_addresses: felt*) -> () {
    }
}

@external
func test_stark_rock_contract{syscall_ptr: felt*, range_check_ptr}() {
    alloc_locals;

    local contract_address: felt;
    // We deploy contract and put its address into a local variable. Second argument is calldata array
    %{ ids.contract_address = deploy_contract("./src/starkRocks.cairo", 
 {
     "name": 0x737461726B526F636B73,
     "symbol": 0x73526B73,
     "owner": 0x1234,
     "base_uri":[0x1234,0x1235],
     "json_extension": 0x1212,
     "currency_address": 0x123456789,
     "mint_price":0x302E3035,
     "royality_address": 0x123,
     "royality_fee": 44,
     "root": 0x12345,
     "wallet_addresses":[0x737461726B526F636B73,0x73526B73],
      }
    ).contract_address %}

    let (receiver:felt, royalityAmount: Uint256) = IStarkRock.royalityInfo(contract_address,Uint256(1000000000000000000, 0));
    assert receiver = 0x123;

    let (totalSupply:felt) = IStarkRock.totalSupply(contract_address);
    let (root:felt) = IStarkRock.merkleRoot(contract_address);
    let (price:Uint256) = IStarkRock.mintPrice(contract_address);
    let (uri_len:felt, uri: felt*) = IStarkRock.baseUri(contract_address);
    let (price:Uint256) = IStarkRock.mintPrice(contract_address);

    %{
        print("receiver",ids.receiver);
        print("royalityAmount",ids.royalityAmount.low);
        print("supply",ids.totalSupply);
        print("root",ids.root);
        print("price",ids.price.low);
    %}


    return ();
}