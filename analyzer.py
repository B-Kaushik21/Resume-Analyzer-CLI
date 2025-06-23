def load_keywords(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"[ERROR] Keywords file '{filepath}' not found.")
        return []

def analyze_resume(text, keywords):
    word_freq = {}
    lower_text = text.lower()

    for keyword in keywords:
        count = lower_text.count(keyword.lower())
        word_freq[keyword] = count

    return word_freq

def suggest_improvements(word_freq):
    missing = [k for k, v in word_freq.items() if v == 0]
    low_freq = [k for k, v in word_freq.items() if v == 1]

    suggestions = []

    if missing:
        suggestions.append(f"Missing important keywords: {', '.join(missing)}")
    if low_freq:
        suggestions.append(f"Use these keywords more frequently: {', '.join(low_freq)}")

    if not suggestions:
        suggestions.append("Great! All essential keywords are well covered.")
    
    return suggestions
