from datetime import date, datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class UrgencyLevel(str, Enum):
    RED = "RED"       # Function-calling trigger: SMS/Email alert
    YELLOW = "YELLOW" # Monitor
    GREEN = "GREEN"   # Log

class UrgencyAlert(BaseModel):
    level: UrgencyLevel = Field(..., description="Urgency level based on immediate deadlines or threats")
    deadline: Optional[date] = Field(None, description="Specific deadline for action if applicable")
    action_item: str = Field(..., description="Specific action for citizens to take")
    context: str = Field(..., description="Context explaining why this is urgent")

class MeetingItem(BaseModel):
    agenda_id: Optional[str] = Field(None, description="Agenda item ID if available")
    topic: str = Field(..., description="Summary of the agenda topic")
    related_to: List[str] = Field(..., description="List of related entities or keywords (e.g., 'Tara Forest', 'Water')")
    outcome: Optional[str] = Field(None, description="Vote outcome or decision if meeting already occurred")

class ScoutReport(BaseModel):
    """Output from A1/A2 scouts"""
    report_id: str = Field(..., description="Unique ID for the report (e.g., A1-2026-01-28)")
    date_generated: datetime = Field(default_factory=datetime.now)
    period_covered: str = Field(..., description="Date range covered by the report")
    executive_summary: str = Field(..., description="Concise summary of the most critical findings")
    alerts: List[UrgencyAlert] = Field(default_factory=list, description="List of actionable alerts")
    items: List[MeetingItem] = Field(default_factory=list, description="List of relevant agenda items found")
    raw_markdown: Optional[str] = Field(None, description="The human-readable markdown version of this report")
