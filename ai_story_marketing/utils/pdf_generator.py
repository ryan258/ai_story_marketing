# 📁 File: ai_story_marketing/ai_story_marketing/utils/pdf_generator.py

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

class PDFGenerator:
    """
    📄 This is our PDFGenerator class.
    It's like a magical printer that turns our story and marketing plan into a beautiful PDF!
    """

    def __init__(self):
        # 🎨 Let's set up our PDF styles
        self.styles = getSampleStyleSheet()
        self._setup_styles()

    def _setup_styles(self):
        # 🖌️ Update existing styles instead of creating new ones
        self.styles['Title'].fontSize = 24
        self.styles['Title'].alignment = 1  # Center alignment
        
        self.styles['Heading1'].fontSize = 18
        self.styles['Heading1'].spaceBefore = 12
        self.styles['Heading1'].spaceAfter = 6
        
        self.styles['BodyText'].fontSize = 12
        self.styles['BodyText'].spaceBefore = 6
        self.styles['BodyText'].spaceAfter = 6

    def generate_pdf(self, content, filename):
        """
        🪄 This is where the magic happens! We turn our content into a PDF.
        
        Args:
            content (dict): All the cool stuff we want in our PDF
            filename (str): What we want to call our PDF file
        
        Returns:
            str: The full path of our new PDF file
        """
        # 📜 Let's create our PDF document
        doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

        # 📚 This will hold all the parts of our document
        story = []

        # 📖 Add the story
        story.append(Paragraph("Your Amazing Story", self.styles['Title']))
        story.append(Spacer(1, 12))
        story.append(Paragraph(content['story'], self.styles['BodyText']))
        story.append(Spacer(1, 12))

        # 🧐 Add the evaluation
        story.append(Paragraph("Story Evaluation", self.styles['Heading1']))
        story.append(Paragraph(f"Score: {content['evaluation']['score']}/10", self.styles['BodyText']))
        story.append(Paragraph(f"Feedback: {content['evaluation']['feedback']}", self.styles['BodyText']))
        story.append(Spacer(1, 12))

        # 🎯 Add the marketing analysis
        story.append(Paragraph("Marketing Analysis", self.styles['Heading1']))
        story.append(Paragraph(f"Target Audience: {content['marketing_analysis']['target_audience']}", self.styles['BodyText']))
        for persona in content['marketing_analysis']['personas']:
            story.append(Paragraph(f"• {persona}", self.styles['BodyText']))
        story.append(Spacer(1, 12))

        # 📱 Add social media content
        story.append(Paragraph("Social Media Content", self.styles['Heading1']))
        for platform, post in content['social_media_content'].items():
            story.append(Paragraph(f"{platform}: {post}", self.styles['BodyText']))
        story.append(Spacer(1, 12))

        # 🎨 Add marketing concepts
        story.append(Paragraph("Marketing Concepts", self.styles['Heading1']))
        for concept, description in content['marketing_concepts'].items():
            story.append(Paragraph(f"{concept}: {description}", self.styles['BodyText']))

        # 🖨️ Now, let's create our PDF!
        doc.build(story)

        return filename

# 🎉 Hooray! We've fixed our PDFGenerator!
# Now it should create a beautiful PDF without any style conflicts! 🚀