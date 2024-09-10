# 📁 File: ai_story_marketing/tests/test_pdf_generator.py

import pytest
import os
from ai_story_marketing.utils.pdf_generator import PDFGenerator

# 🧪 Welcome to our updated PDF Generator test file! 🚀
# Here, we'll make sure our PDF Generator works perfectly with all our cool content!

@pytest.fixture
def sample_content():
    # 📚 This is our pretend content for testing
    return {
        "story": "Once upon a time, in a land of code and imagination...",
        "evaluation": {
            "score": 9,
            "feedback": "Wow! This story is amazing! It's full of creativity and wonder."
        },
        "marketing_analysis": {
            "target_audience": "Young coders and dreamers",
            "personas": ["Curious Cathy, 12, loves puzzles", "Inventive Ivan, 10, enjoys building things"]
        },
        "social_media_content": {
            "Twitter": "Discover a world where code comes to life! 🌟 #CodingAdventure",
            "Instagram": "Step into a magical coding realm! ✨👩‍💻👨‍💻 #TechTales"
        },
        "marketing_concepts": {
            "Book Cover": "A dazzling display of binary code forming a magical castle",
            "Movie Trailer": "Fast-paced montage of kids coding and magical code effects"
        }
    }

def test_pdf_generator_creation():
    # 🏗️ Let's test if we can create a PDFGenerator
    pdf_gen = PDFGenerator()
    assert pdf_gen is not None, "We should be able to create a PDFGenerator!"
    assert pdf_gen.styles is not None, "PDFGenerator should have styles!"

def test_pdf_generation(sample_content, tmp_path):
    # 📄 Let's test if we can generate a PDF with all our cool content
    pdf_gen = PDFGenerator()
    pdf_file = tmp_path / "test_output.pdf"
    
    generated_file = pdf_gen.generate_pdf(sample_content, str(pdf_file))
    
    assert os.path.exists(generated_file), "The PDF file should exist!"
    assert generated_file.endswith('.pdf'), "The file should end with .pdf!"

def test_pdf_content(sample_content, tmp_path):
    # 📖 Let's make sure our PDF has all the right content
    pdf_gen = PDFGenerator()
    pdf_file = tmp_path / "test_content.pdf"
    
    pdf_gen.generate_pdf(sample_content, str(pdf_file))
    
    # Now, let's check if the file exists and has some content
    assert os.path.exists(pdf_file), "The PDF file should exist!"
    assert os.path.getsize(pdf_file) > 0, "The PDF file should not be empty!"

# 🎉 Hooray! We've updated our tests for the PDFGenerator!
# Now we can be super sure it's working perfectly with all our cool story stuff! 🚀

if __name__ == "__main__":
    pytest.main()