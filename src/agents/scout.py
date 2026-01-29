import datetime
from typing import Dict, Any
from src.agents.base import BaseAgent
from src.schemas import ScoutReport
from src.models import get_gemini_pro, get_gemini_flash
from src.tools import monitor_url
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

class ScoutAgent(BaseAgent):
    def __init__(self, name: str, prompt_template: str):
        super().__init__(name, role="Scout")
        self.prompt_template = prompt_template
        self.llm = get_gemini_pro() # Using Pro for the heavy lifting of synthesis
        # We bind the structured output schema to the model
        self.structured_llm = self.llm.with_structured_output(ScoutReport)

    def run(self, input_data: Dict[str, Any]) -> ScoutReport:
        """
        1. Identifies URL to monitor from input or registry.
        2. Fetches content using monitor_url tool.
        3. Passes content + Prompt to Gemini.
        4. Returns structured decision.
        """
        target_url = input_data.get("url")
        if not target_url:
            raise ValueError("ScoutAgent requires a 'url' in input_data")

        print(f"[{self.name}] Monitoring: {target_url}")
        
        # 1. Fetch Content
        page_content = monitor_url.invoke(target_url)
        
        # 2. Prepare Prompt
        # We inject the scraped content and the current date
        current_date = datetime.date.today().isoformat()
        
        final_prompt = ChatPromptTemplate.from_template(
            """
            Role: {role}
            Current Date: {date}
            
            Mission: {mission}
            
            ---
            TOPIC: {topic}
            SOURCE URL: {url}
            SOURCE CONTENT:
            {content}
            ---
            
            Based on the content above, generate a ScoutReport.
            """
        )
        
        chain = final_prompt | self.structured_llm
        
        # 3. Execute
        result: ScoutReport = chain.invoke({
            "role": "Alachua Civic Intelligence Scout",
            "date": current_date,
            "mission": "Monitor for environmental threats and democratic accountability issues.",
            "topic": self.name, # e.g. "A1 Meeting Scout"
            "url": target_url,
            "content": page_content[:100000] # Safe truncation for Gemini context
        })
        
        return result
