# File: ai_story_marketing/ai_story_marketing/utils/output_generator.py

from fpdf import FPDF  # We'll use fpdf for PDF generation

class OutputGenerator:
    def __init__(self):
        self.content = {
            "story": None,
            "evaluation": None,
            "marketing_persona": None,
            "social_media_content": None,
            "marketing_materials": None
        }

    def add_content(self, content_type, data):
        """
        Add content to the output generator.
        """
        if content_type in self.content:
            self.content[content_type] = data
        else:
            raise ValueError(f"Invalid content type: {content_type}")

    def generate_output(self):
        """
        Generate a comprehensive output document.
        """
        output = []
        for section, content in self.content.items():
            if content:
                output.append(f"--- {section.upper()} ---")
                output.append(content)
                output.append("\n")
        return "\n".join(output)

    def generate_pdf(self, filename="output.pdf"):
        """
        Generate a PDF version of the output.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for section, content in self.content.items():
            if content:
                pdf.cell(200, 10, txt=f"--- {section.upper()} ---", ln=True, align='C')
                pdf.multi_cell(0, 10, txt=content)
                pdf.ln(10)

        pdf.output(filename)

    def clear_content(self):
        """
        Clear all content from the output generator.
        """
        for key in self.content:
            self.content[key] = None

    def get_content(self, content_type):
        """
        Retrieve specific content by type.
        """
        return self.content.get(content_type)