# Textbook to PDF Converter

This script converts textbook page images to a PDF file using OCR (Optical Character Recognition) via the GPT-4 Vision API.

## Prerequisites

- Python 3.7 or higher
- OpenAI API key with access to GPT-4 Vision

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the same directory as the script with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the script:
```bash
python textbook_to_pdf.py
```

2. When prompted, enter:
   - The base URL for the textbook images (e.g., `https://example.com/textbook/page-`)
   - The start page number
   - The end page number
   - The desired output PDF filename

## Notes

- The script assumes the images are in JPG format
- The script adds a 1-second delay between processing pages to avoid rate limiting
- The output PDF will maintain the text formatting as much as possible
- Make sure your OpenAI API key has sufficient credits for the number of pages you want to process
- The script processes images directly from URLs without downloading them

## Error Handling

The script includes error handling for:
- OCR processing errors
- PDF creation issues

If any errors occur, they will be printed to the console, and the script will continue processing the remaining pages. 