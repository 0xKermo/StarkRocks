from merkle import address_to_leaf, merkle_proof, merkle_root,hash2

ALLOW_LIST = [
    *[
        int(address, 16)
        for address in [
            "0x00D021cB221FA3a37aF0f9ac915357990059D0379F3aD02C5D0B332D70453867",
            "0x0437D86aa7Ab69D30f05ED5d4F4A4ed937A3d7212934BE6976A95a04e091e44a",
            "0x00900643da0b6fd703e7abf13178cde7ce5bd6107cbc7fd33c6b9209306d1bdb",
            "0x03e4f8a18af47c89db295cbf718188137a3bd3b631c224b53840d402a354687b",
            "0x023bd08ba8badc1c3cd34564cbd1e0ce2e07de220320ad6e7a52d76e279c5248",
            "0x05b2E59D20b9f3e2b750a74EdB0244baaD33AA370e98a6aeb8a60C0e45b9e5a6",
            "0x07A6A583344fbc4055619625d7FC6d1788C8B42653b8f9D659a47c6BcDb553C3",
            "0x06e4e6437a3533c74339b3aa9c7bd7b11969d3601adcf19c6c0e3b23cf26b3d3"
        ]
    ],
]

LEAFS = [address_to_leaf(address) for address in ALLOW_LIST]
MERKLE_ROOT = merkle_root(LEAFS)

print(hex(MERKLE_ROOT))
proofs = merkle_proof(int("0x06e4e6437a3533c74339b3aa9c7bd7b11969d3601adcf19c6c0e3b23cf26b3d3",16),ALLOW_LIST)
print("proof")

for i in proofs:
    print(str(hex(i)))
