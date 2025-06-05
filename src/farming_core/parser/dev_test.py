from .semantic_parser.dispatcher import classify_transaction

from pprint import pprint

tx = {
    "hash": "0xb3f8c36d45e9d4c609c3692b0842a6d9d6e4aca0856df092eef285a1066672b2",
    "timestamp": "2025-06-02T08:45:41Z",
    "to": "0x13E46b2a8fB8560589fE3C21722b420f2C099c819",  # Orbiter Bridge contract
    "function_name": "transfers",  # (не 'bridge', но мы можем его поймать через адрес)
    "recipient": "0x929d78d36d12be88168e4065dCe8ba55efC6dFeF",
    "chain": "Base",
    "protocol": "Orbiter",
    "source_chain": "zkSync Era",
    "dest_chain": "Base"
}

# activity = parse_tx_to_semantic(tx)
# pprint(activity)


action = classify_transaction(tx)
pprint(action)
