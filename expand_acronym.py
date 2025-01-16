import re

def extract_acronyms_and_expansions(text):
    """
    Extract acronyms and their expansions from a given text snippet.
    Returns a dictionary mapping acronyms to their expansions.
    """
    pattern = r'([A-Za-z\s]+?)\s*(?:\((?:Abbreviation:|commonly referred to as|[A-Za-z\s]*?)([A-Z]{2,})\))'
    matches = re.findall(pattern, text)
    
    # Store the acronym-expansion pairs
    acronyms_dict = {acronym.strip(): expansion.strip() for expansion, acronym in matches}
    
    # Also consider the case where the acronym is directly in parentheses
    pattern = r'([A-Za-z\s]+?)\s*\(([A-Z]{2,})\)'  # Match expansion (acronym) pattern
    matches = re.findall(pattern, text)
    
    for expansion, acronym in matches:
        acronyms_dict[acronym.strip()] = expansion.strip()
    
    return acronyms_dict

def main():
    # Input: Number of text snippets
    n = int(input().strip())
    acronyms = {}

    # Parse the text snippets and populate the acronym dictionary
    for _ in range(n):
        snippet = input().strip()
        acronyms.update(extract_acronyms_and_expansions(snippet))

    # Input: Acronyms to expand
    test_acronyms = [input().strip() for _ in range(n)]

    # Output: Expanded form of the acronyms
    for test in test_acronyms:
        print(acronyms.get(test, "Not Found"))

if __name__ == "__main__":
    main()
