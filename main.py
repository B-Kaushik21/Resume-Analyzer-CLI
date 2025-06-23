import sys
import os
from extractor import extract_text_from_pdf
from analyzer import load_keywords, analyze_resume, suggest_improvements

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <resume.pdf> <role>")
        print("Available roles: web_developer, data_scientist, devops_engineer, mobile_developer, software_engineer, cloud_engineer")
        return

    pdf_path = sys.argv[1]
    role = sys.argv[2]
    keyword_file = f"keywords/{role}.txt"

    if not os.path.exists(pdf_path):
        print(f"[ERROR] Resume file '{pdf_path}' not found.")
        return

    if not os.path.exists(keyword_file):
        print(f"[ERROR] Keywords file for role '{role}' not found.")
        return

    print("Extracting text from resume...")
    text = extract_text_from_pdf(pdf_path)

    print("Text extracted. Analyzing...\n")
    keywords = load_keywords(keyword_file)
    result = analyze_resume(text, keywords)

    print("Keyword Frequency:")
    for k, v in result.items():
        print(f"  {k}: {v}")

    print("\n Suggestions:")
    for s in suggest_improvements(result):
        print(" ", s)

if __name__ == "__main__":
    main()
