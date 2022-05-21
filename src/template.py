from typing import Optional, List

class Mapping:
    source_column: str
    target_column: str
    transform: Optional[str]

class Template:
    name: str
    source: str
    target: str
    mapping: List[Mapping]

