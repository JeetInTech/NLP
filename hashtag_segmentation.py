import re

# Load words from a file or a set of common words
def load_words():
    # Example of a small word list (you can replace with a bigger one or corpus)
    return {"we", "are", "the", "people", "mention", "your", "faves", "now", "playing", "the", "walking", "dead", "follow", "me"}

# Function to check if a word is valid (exists in the dictionary)
def is_valid_token(token, word_set):
    return token in word_set

# Recursive segmentation with memoization
def segment_string(s, word_set, memo):
    if s in memo:
        return memo[s]
    if not s:
        return []

    best_split = None
    for i in range(1, len(s) + 1):
        left = s[:i]
        if is_valid_token(left, word_set):
            right_split = segment_string(s[i:], word_set, memo)
            if right_split is not None:
                current_split = [left] + right_split
                if best_split is None or len(current_split) > len(best_split):
                    best_split = current_split

    memo[s] = best_split if best_split is not None else [s]
    return memo[s]

def process_hashtags(hashtags, word_set):
    results = []
    memo = {}
    for hashtag in hashtags:
        segmented = segment_string(hashtag, word_set, memo)
        results.append(' '.join(segmented))
    return results

def main():
    # Load the set of common words
    word_set = load_words()

    # Input: Number of hashtags
    n = int(input().strip())
    hashtags = [input().strip() for _ in range(n)]

    # Process the hashtags and print the results
    results = process_hashtags(hashtags, word_set)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
