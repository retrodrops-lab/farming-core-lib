from dataclasses import dataclass, field
from typing import List, Literal, Dict
from datetime import datetime

@dataclass
class SemanticActivity:
    chain: str
    protocol: str
    action: Literal["swap", "bridge", "mint", "stake", "claim", "vote", "liquidity", "unknown"]
    tokens_in: List[str]
    tokens_out: List[str]
    tx_hash: str
    timestamp: datetime
    metadata: Dict[str, str] = field(default_factory=dict)
