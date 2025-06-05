from .base import SemanticRule

KNOWN_BRIDGE_ADDRESSES = {
    "0x80c67432656d59144ceff962e8faf8926599bcf8": "orbiter",
    "0x13e46b2a8fb8560589fe3c21722b420f2c099c819": "orbiter",
    "0x1a2b3c4d5e6f7890abcdef1234567890abcdef12": "hop",
}


class BridgeRule(SemanticRule):
    def match(self, tx: dict) -> str | None:
        to_address = tx.get("to", "").lower()
        if to_address in KNOWN_BRIDGE_ADDRESSES:
            return "bridge"
        return None