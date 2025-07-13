from google import genai

# ✅ You must import `types` from google.genai if you want to use `GenerateContentConfig`
from google.genai import types

client = genai.Client()

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}.\n"
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.\n"
    "3. **Empty Response:** If no information matches the description, return an empty string ('').\n"
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_Gemini(dom_chunks, parse_description):
    parsed_results = []
    for i, chunk in enumerate(dom_chunks, start=1):
        try:
            prompt = template.format(dom_content=chunk, parse_description=parse_description)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                generation_config=types.GenerationConfig(
                    temperature=0
                ),
                system_instruction=(
                    "You are a precise data extractor. "
                    "Your role is to extract only the information that exactly matches the provided description, "
                    "returning it without any additional text, comments, or explanations. "
                    "If no information matches, return an empty string."
                )
            )
            parsed_results.append(response.text)
            print(f"Parsed batch {i} of {len(dom_chunks)}")
        except Exception as e:
            print(f"Error in batch {i}: {e}")
            parsed_results.append("")

    # ✅ Always return your results
    return "\n".join(parsed_results)
