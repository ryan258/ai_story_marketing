# 📁 File: ai_story_marketing/ai_story_marketing/agents/marketing_expert.py

from .base_agent import BaseAgent
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MarketingExpert(BaseAgent):
    def __init__(self, model):
        super().__init__(model)
        self.personas = []
        self.target_audience = ""

    def process(self, story):
        prompt = self.format_prompt(
            "Analyze the following story and create 3 marketing personas. "
            "Also provide a brief description of the target audience. "
            "Format your response as follows:\n"
            "TARGET AUDIENCE: [Description of target audience]\n"
            "PERSONAS:\n"
            "1. [Persona 1 description]\n"
            "2. [Persona 2 description]\n"
            "3. [Persona 3 description]\n"
            "Story: {story}",
            story=story
        )
        
        try:
            analysis = self.generate_text(prompt)
            logger.info(f"Raw analysis: {analysis}")
            
            if analysis:
                parts = analysis.split("TARGET AUDIENCE:", 1)
                if len(parts) == 2:
                    target_audience, personas_part = parts[1].split("PERSONAS:", 1)
                    self.target_audience = target_audience.strip()
                    self.personas = [p.strip() for p in personas_part.split("\n") if p.strip() and not p.strip().isdigit()]
                else:
                    raise ValueError("Unexpected format in the analysis")
            else:
                raise ValueError("Empty analysis received")

            # Ensure we have exactly 3 personas
            if len(self.personas) < 3:
                self.personas.extend(["Generic persona"] * (3 - len(self.personas)))
            elif len(self.personas) > 3:
                self.personas = self.personas[:3]

        except Exception as e:
            logger.error(f"Error processing analysis: {str(e)}")
            logger.error(f"Analysis content: {analysis}")
            self.target_audience = "Young to middle-aged adults interested in this type of story"
            self.personas = [
                "Emily, 28, urban professional who loves quirky stories and DIY projects",
                "Michael, 35, tech enthusiast with a secret passion for tidying up",
                "Sarah, 42, busy mom fascinated by both family stories and organization"
            ]
        
        self.update_context({
            "marketing_analysis": {
                "personas": self.personas,
                "target_audience": self.target_audience
            }
        })
        
        return {
            "personas": self.personas,
            "target_audience": self.target_audience
        }

    def get_personas(self):
        return self.personas

    def get_target_audience(self):
        return self.target_audience