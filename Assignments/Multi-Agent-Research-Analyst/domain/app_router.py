
from typing import Literal, TypedDict

class Router(TypedDict):
    next: Literal['research_supervisor', 'reporting_supervisor', 'FINSIH']  = "FINSIH"