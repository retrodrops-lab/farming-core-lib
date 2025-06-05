from .base import SemanticRule

class SwapRule(SemanticRule):
    def match(self, tx: dict) -> str | None:
        fn = tx.get("function_name", "").lower()
        if "swap" in fn:
            return "swap"
        return None