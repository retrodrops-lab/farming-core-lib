from datetime import datetime
from typing import Dict
from farming_core.models.semantic_activity import SemanticActivity

def infer_action_type(tx: Dict) -> str:
    fn = tx.get("function_name", "").lower()

    if "bridge" in fn:
        return "bridge"
    if "swap" in fn:
        return "swap"
    if "stake" in fn or "deposit" in fn:
        return "stake"
    if "mint" in fn:
        return "mint"

    # fallback: address or protocol
    to = tx.get("to", "").lower()
    if "orbiter" in tx.get("protocol", "").lower():
        return "bridge"
    if any(kw in to for kw in ["bridge", "orbiter", "layerzero", "hop", "stargate"]):
        return "bridge"

    return "unknown"

def infer_protocol(tx: Dict) -> str:
    to = tx.get("to", "").lower()
    if "13e46b2a8fb8560589fe3c2172" in to:
        return "Orbiter"
    if "stargate" in tx.get("function_name", "").lower():
        return "Stargate"
    return tx.get("protocol", "unknown")

def parse_tx_to_semantic(tx: Dict) -> SemanticActivity:
    return SemanticActivity(
        chain=tx.get("chain", "unknown"),
        protocol=infer_protocol(tx),
        action=infer_action_type(tx),
        tokens_in=["ETH"],  # TODO: parse logs
        tokens_out=["ETH"],
        tx_hash=tx["hash"],
        timestamp=datetime.strptime(tx["timestamp"], "%Y-%m-%dT%H:%M:%SZ"),
        metadata={
            "from": tx.get("source_chain", "unknown"),
            "to": tx.get("dest_chain", "unknown"),
            "bridge_contract": tx.get("to"),
            "recipient": tx.get("recipient")
        }
    )
