"""
Approval API routes for Alachua Civic Intelligence System.

Provides human-in-the-loop endpoints for:
- GET /approvals/pending - List pending approvals
- GET /approvals/{id} - Get approval details
- POST /approvals/{id}/decide - Approve or reject
"""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/approvals", tags=["approvals"])


# =============================================================================
# MODELS
# =============================================================================

class ApprovalRequest(BaseModel):
    """Request to approve/reject a pending item."""
    decision: str = Field(..., description="approved or rejected")
    comments: Optional[str] = None


class ApprovalItem(BaseModel):
    """A pending approval item."""
    id: str
    agent: str
    created_at: datetime
    summary: str
    data: dict


class ApprovalDecision(BaseModel):
    """Result of an approval decision."""
    approval_id: str
    decision: str
    comments: Optional[str]
    item_summary: str
    decided_at: datetime


# =============================================================================
# IN-MEMORY STATE (Replace with Redis/DB in production)
# =============================================================================

pending_approvals: dict[str, ApprovalItem] = {}
decided_approvals: dict[str, ApprovalDecision] = {}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def add_pending_approval(
    approval_id: str,
    agent: str,
    summary: str,
    data: dict
) -> ApprovalItem:
    """Add a new pending approval item."""
    item = ApprovalItem(
        id=approval_id,
        agent=agent,
        created_at=datetime.now(),
        summary=summary,
        data=data
    )
    pending_approvals[approval_id] = item
    return item


# =============================================================================
# ROUTES
# =============================================================================

@router.get("/pending")
async def list_pending_approvals():
    """List all pending approval items."""
    return {
        "count": len(pending_approvals),
        "pending": [item.model_dump() for item in pending_approvals.values()]
    }


@router.get("/{approval_id}")
async def get_approval(approval_id: str):
    """Get details of a pending approval."""
    if approval_id in pending_approvals:
        return {
            "status": "pending",
            "item": pending_approvals[approval_id].model_dump()
        }
    elif approval_id in decided_approvals:
        return {
            "status": "decided",
            "decision": decided_approvals[approval_id].model_dump()
        }
    else:
        raise HTTPException(status_code=404, detail="Approval not found")


@router.post("/{approval_id}/decide", response_model=ApprovalDecision)
async def decide_approval(approval_id: str, request: ApprovalRequest):
    """
    Approve or reject a pending item.
    
    - **decision**: "approved" or "rejected"
    - **comments**: Optional reviewer comments
    """
    if approval_id not in pending_approvals:
        raise HTTPException(status_code=404, detail="Approval not found or already decided")
    
    if request.decision not in ["approved", "rejected"]:
        raise HTTPException(status_code=400, detail="Decision must be 'approved' or 'rejected'")
    
    item = pending_approvals.pop(approval_id)
    
    decision = ApprovalDecision(
        approval_id=approval_id,
        decision=request.decision,
        comments=request.comments,
        item_summary=item.summary,
        decided_at=datetime.now()
    )
    
    decided_approvals[approval_id] = decision
    
    # If approved, trigger downstream actions (e.g., publish, notify)
    if request.decision == "approved":
        # TODO: Trigger synthesizer or notification
        pass
    
    return decision


@router.get("/history")
async def list_decided_approvals(limit: int = 20):
    """List recently decided approvals."""
    sorted_decisions = sorted(
        decided_approvals.values(),
        key=lambda d: d.decided_at,
        reverse=True
    )
    return {
        "count": len(decided_approvals),
        "decisions": [d.model_dump() for d in sorted_decisions[:limit]]
    }
