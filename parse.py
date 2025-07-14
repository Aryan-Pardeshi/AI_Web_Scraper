from google import genai

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Verify GEMINI_API_KEY is set
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY environment variable not found. Please set it in .env or system environment.")

# No need for genai.configure() since GEMINI_API_KEY is auto-detected
client = genai.Client()

template = (
    "You are an information extractor.\n\n"
    "Your task is to extract only the information that matches the description below from the provided text content.\n\n"
    "## TEXT CONTENT ##\n"
    "{dom_content}\n\n"
    "## EXTRACTION TASK ##\n"
    "{parse_description}\n\n"
    "## OUTPUT FORMAT ##\n"
    "- Do not add any extra text, titles or explanations.\n"
    "- You can use Tables, lists, paragraphs to format the content.\n"
    "- Output only the result.\n"
    "- If there is no match, return **'NO_MATCH_FOUND'** exactly.\n"
    "- If no matches are found, return exactly: 'NO_MATCH_FOUND'.\n"
)


def parse_with_Gemini(dom_chunks, parse_description):
    parsed_results = []
    for i, chunk in enumerate(dom_chunks, start=1):
        try:
            prompt = template.format(dom_content=chunk, parse_description=parse_description)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            text = response.text
            if text is None:
                print(f"Batch {i} returned None.")
                text = ""  # Safe fallback
            parsed_results.append(text)
            print(f"Parsed batch {i} of {len(dom_chunks)}")
        except Exception as e:
            print(f"Error in batch {i}: {e}")
            parsed_results.append("")
    return "\n".join(parsed_results)
