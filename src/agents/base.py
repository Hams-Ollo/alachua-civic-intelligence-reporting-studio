from typing import Any, Dict
from abc import ABC, abstractmethod
from src.schemas import ScoutReport

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    def run(self, input_data: Dict[str, Any]) -> ScoutReport:
        """
        Executes the agent's logic.
        Must return a structured ScoutReport.
        """
        pass
