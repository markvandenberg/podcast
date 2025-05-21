import os
import openai
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

def extract_text_from_image_url(image_url):
    """Extract text from image using GPT-4 Vision API."""
    try:
        # Call ChatGPT API with direct image URL
        response = openai.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract all text from this image. Preserve the formatting as much as possible."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ],
            max_tokens=4096
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""

def create_pdf(texts, output_filename):
    """Create PDF from extracted texts."""
    try:
        c = canvas.Canvas(output_filename, pagesize=A4)
        width, height = A4
        
        # Set font
        c.setFont("Helvetica", 12)
        
        # Add texts to PDF
        y = height - 50  # Start from top with margin
        for text in texts:
            # Split text into lines
            lines = text.split('\n')
            for line in lines:
                if y < 50:  # If we're near the bottom, create new page
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y = height - 50
                
                c.drawString(50, y, line)
                y -= 15  # Move down for next line
            
            # Add page break between different pages
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50
        
        c.save()
        print(f"PDF created successfully: {output_filename}")
    except Exception as e:
        print(f"Error creating PDF: {e}")

def process_textbook(base_url, start_page, end_page, output_filename):
    """Process textbook pages and create PDF."""
    texts = []
    
    for page_num in range(start_page, end_page + 1):
        # Construct image URL
        image_url = f"{base_url}{page_num}.jpg"
        print(f"Processing page {page_num}...")
        
        # Extract text directly from image URL
        text = extract_text_from_image_url(image_url)
        texts.append(text)
        
        # Add delay to avoid rate limiting
        time.sleep(1)
    
    # Create PDF
    create_pdf(texts, output_filename)

if __name__ == "__main__":
    # Example usage
    base_url = input("Enter the base URL for the textbook images: ")
    start_page = int(input("Enter the start page number: "))
    end_page = int(input("Enter the end page number: "))
    output_filename = input("Enter the output PDF filename (e.g., textbook.pdf): ")
    
    process_textbook(base_url, start_page, end_page, output_filename) 