from typing import Dict, Any
from src.agents.base import BaseAgent
from src.schemas import ScoutReport 
# Note: In a real scenario, Analyst might output a different schema "AnalystReport", 
# but for simplicity we can reuse ScoutReport or create a specialized one. 
# For now, let's assume Analyst outputs a similar structure (Findings, Alerts, Recommendations).

from src.models import get_gemini_pro
from src.tools import deep_research
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from datetime import datetime

class AnalystAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name, role="Analyst")
        self.llm = get_gemini_pro()
        # Bind deep_research tool for the agent to use proactively if we were using a React loop.
        # However, for this structured pipeline, we might just inject the research results.
        # Let's define a chain: Research -> Synthesize
        self.structured_llm = self.llm.with_structured_output(ScoutReport)

    def run(self, input_data: Dict[str, Any]) -> ScoutReport:
        """
        1. Formulate search queries based on topic.
        2. Execute Deep Research (Tavily).
        3. Synthesize findings into a Report.
        """
        topic = input_data.get("topic")
        if not topic:
            raise ValueError("AnalystAgent requires a 'topic'")

        print(f"[{self.name}] Researching topic: {topic}")
        
        # 1. Deep Research
        # In a more advanced agent, the LLM would decide the query. 
        # Here we do a single-shot "Deep Research" call for reliability.
        research_context = deep_research.invoke(f"Current news and development updates regarding {topic}")
        
        # 2. Synthesis
        prompt = ChatPromptTemplate.from_template(
            """
            Role: {role}
            Mission: Analyze deep research findings to identify patterns, hidden connections, and strategic insights.
            
            Topic: {topic}
            
            RESEARCH FINDINGS:
            {context}
            
            ---
            Synthesize these findings into a detailed Intelligence Report.
            Focus on:
            1. New development activity
            2. Regulatory changes
            3. Hidden connections between entities
            """
        )
        
        chain = prompt | self.structured_llm
        
        result = chain.invoke({
            "role": "Alachua Civic Intelligence Analyst",
            "topic": topic,
            "context": research_context
        })
        
        return result
