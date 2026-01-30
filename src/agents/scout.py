import datetime
from typing import Dict, Any
from src.agents.base import BaseAgent
from src.schemas import ScoutReport
from src.models import get_gemini_pro
from src.tools import monitor_url  # This imports from src/tools.py module
from src.prompts import get_alachua_context


class ScoutAgent(BaseAgent):
    """
    Layer 1 Scout agent for monitoring government data sources.
    
    Uses domain context from prompt_library for enhanced analysis.
    Uses native google.genai SDK to avoid PyTorch/transformers dependencies.
    """
    
    def __init__(self, name: str, prompt_template: str = None):
        super().__init__(name, role="Scout")
        self.prompt_template = prompt_template
        self.llm = get_gemini_pro()
        self.structured_llm = self.llm.with_structured_output(ScoutReport)
        self.context = get_alachua_context()

    def _build_prompt(self, agent_id: str, date: str, url: str, content: str, keywords: str) -> str:
        """Build the analysis prompt with domain context."""
        return f"""You are a **Meeting Intelligence Scout** for the Alachua Civic Intelligence System.

{self.context.get_prompt_context()}

---
## CURRENT TASK

**Agent:** {agent_id}
**Current Date:** {date}
**Source URL:** {url}

### SOURCE CONTENT:
{content}

---

## INSTRUCTIONS

Analyze the content above and generate a ScoutReport with:
1. **report_id**: Format as "{agent_id}-{date}-001"
2. **period_covered**: The date range covered by this content
3. **executive_summary**: 2-3 sentences on most critical findings
4. **alerts**: List of UrgencyAlerts (RED/YELLOW/GREEN) with action items
5. **items**: List of MeetingItems with topics, related entities, and outcomes

**Priority Keywords to Flag:** {keywords}

Focus on items related to: Tara development, Mill Creek Sink, environmental protection, 
public hearings, zoning changes, and any entities from the watchlist.
"""

    def _execute(self, input_data: Dict[str, Any]) -> ScoutReport:
        """
        1. Identifies URL to monitor from input or registry.
        2. Fetches content using monitor_url tool.
        3. Passes content + domain context + Prompt to Gemini.
        4. Returns structured decision.
        """
        target_url = input_data.get("url")
        if not target_url:
            raise ValueError("ScoutAgent requires a 'url' in input_data")

        self.logger.info("Fetching URL content", url=target_url)
        
        # 1. Fetch Content
        page_content = monitor_url.invoke(target_url)
        
        # 2. Prepare Prompt with domain context
        current_date = datetime.date.today().isoformat()
        
        prompt = self._build_prompt(
            agent_id=self.name,
            date=current_date,
            url=target_url,
            content=page_content[:80000],
            keywords=self.context.get_keywords_string()
        )
        
        # 3. Execute with structured output
        result: ScoutReport = self.structured_llm.invoke(prompt)
        
        self.logger.info(
            "Scout analysis complete",
            items_found=len(result.items),
            alerts_count=len(result.alerts)
        )
        
        return result
