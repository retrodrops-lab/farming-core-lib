def get_explorer_url(chain: str, tx_hash: str) -> str:
    if chain.lower() == "ethereum":
        return f"https://etherscan.io/tx/{tx_hash}"
    elif chain.lower() == "zksync":
        return f"https://explorer.zksync.io/tx/{tx_hash}"
    elif chain.lower() == "monad":
        return f"https://monadscan.org/tx/{tx_hash}"
    else:
        return f"https://unknown-chain.io/tx/{tx_hash}"
