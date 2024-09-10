# 📁 File: ai_story_marketing/ai_story_marketing/utils/output_generator.py

import json
import pdfkit
from jinja2 import Environment, FileSystemLoader

class OutputGenerator:
    """
    📦 Our magical OutputGenerator! It puts all our story pieces together!
    """

    def __init__(self):
        # 🎭 Let's set up our magic box to hold all the cool stuff we make
        self.content = {
            "story": None,
            "evaluation": None,
            "marketing_analysis": None,
            "social_media_content": None,
            "marketing_concepts": None
        }

    def add_content(self, content_type, data):
        """
        🧙‍♂️ This is how we add new things to our magic box!
        """
        if content_type in self.content:
            self.content[content_type] = data
        else:
            raise ValueError(f"Oops! We don't have a spot for {content_type} in our magic box!")

    def generate_output(self):
        """
        ✨ This is where we make all our content look pretty!
        """
        output = {}
        for section, content in self.content.items():
            if content:
                # 🧠 Let's make sure we can handle different types of content
                if isinstance(content, dict):
                    output[section] = content
                else:
                    output[section] = str(content)
        return output

    def generate_pdf(self, template_path, output_path):
        """
        📜 This is where we make a fancy PDF of our story and marketing plan!
        """
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(template_path)
        
        html_out = template.render(result=self.content)
        
        # Now, let's turn our HTML into a beautiful PDF!
        pdfkit.from_string(html_out, output_path)

    def clear_content(self):
        """
        🧹 This helps us clean out our magic box when we're done!
        """
        for key in self.content:
            self.content[key] = None

    def get_content(self, content_type):
        """
        🔍 This lets us peek inside our magic box at a specific thing!
        """
        return self.content.get(content_type)

# 🧪 Let's test our OutputGenerator!
def test_output_generator():
    generator = OutputGenerator()
    
    # Add some test content
    generator.add_content("story", "Once upon a time...")
    generator.add_content("evaluation", {"score": 8, "feedback": "Great story!"})
    generator.add_content("marketing_analysis", {"target_audience": "Kids", "personas": ["Curious Carl", "Adventurous Anna"]})
    
    # Generate output
    output = generator.generate_output()
    
    # Check if our output looks right
    assert isinstance(output, dict), "Output should be a dictionary"
    assert "story" in output, "Output should contain the story"
    assert isinstance(output["evaluation"], dict), "Evaluation should be a dictionary"
    assert isinstance(output["marketing_analysis"], dict), "Marketing analysis should be a dictionary"
    
    print("🎉 Yay! Our OutputGenerator is working great!")

if __name__ == "__main__":
    test_output_generator()