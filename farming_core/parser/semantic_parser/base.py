from abc import ABC, abstractmethod

class SemanticRule(ABC):
    @abstractmethod
    def match(self, tx: dict) -> str | None:
        pass