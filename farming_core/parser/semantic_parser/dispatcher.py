from .rules_bridge import BridgeRule
from .rules_swap import SwapRule

ALL_RULES = [BridgeRule(), SwapRule()]

def classify_transaction(tx: dict) -> str:
    for rule in ALL_RULES:
        result = rule.match(tx)
        if result:
            return result
    return "unknown"