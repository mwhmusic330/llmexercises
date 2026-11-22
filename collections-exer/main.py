"""You have a raw stream of user comments or log entries. You need to:

    1.Count how often specific keywords appear.
    2.Ignore common "stopwords" (like the, is, at) that clutter the analysis.
    3.Compare two different datasets using Counter subtraction/addition logic to see what changed between them."""





from collections import Counter, defaultdict


data_a = ["Hello World", "Is this the life?", "What is this thing?"]
data_b = ["Goodbye Earthling", "That is all for now", "The ball is red"]

stopwords_list = ['the', 'like', 'is', 'at']

def clean_text(texts):
    cleaned_tokens = []
    for raw_text in texts:
        if not isinstance(raw_text, str) or raw_text.strip() == "":
            continue
        
        lowered_str = raw_text.lower().strip()
        print(lowered_str)

        potential_words = lowered_str.split()
        print(potential_words)
        
        cleaned_tokens.extend([word.strip("?/!,;:'\"()")for word in potential_words])

    return cleaned_tokens




def main():
    tokens_a = clean_text(data_a)
    tokens_b = clean_text(data_b)

    counter_a = Counter(tokens_a)
    counter_b = Counter(tokens_b)

    combined_counter = counter_a + counter_b
    print(dict(counter_a))
    print(dict(counter_b))
    print(dict(combined_counter))


if __name__ == "__main__":
    main()
