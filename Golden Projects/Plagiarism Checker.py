from difflib import SequenceMatcher

def calculate_plagiarism_percentage(text1, text2):
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    return similarity_ratio * 100

def check_plagiarism(text1, text2, threshold=0.8):
    similarity_percentage = calculate_plagiarism_percentage(text1, text2)
    if similarity_percentage >= threshold * 100:
        return True, similarity_percentage
    else:
        return False, similarity_percentage

# Example usage
document1 = "This is an example text for testing plagiarism detection."
document2 = "An example text for testing plagiarism detection is given here."

is_plagiarized, percentage = check_plagiarism(document1, document2)
if is_plagiarized:
    print(f"Plagiarism detected! Similarity: {percentage:.2f}%")
else:
    print(f"No plagiarism detected. Similarity: {percentage:.2f}%")
