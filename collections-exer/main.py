"""You have a raw stream of user comments or log entries. You need to:

    1.Count how often specific keywords appear.
    2.Ignore common "stopwords" (like the, is, at) that clutter the analysis.
    3.Compare two different datasets using Counter subtraction/addition logic to see what changed between them."""





from collections import Counter, defaultdict


data_a = ["Hello World", "Is this the life?", "What is this thing?"]
data_b = ["Goodbye Earthling", "Thart is all for now"]

stopwords_list = ['the', 'is', 'at']

def clean_text(texts):
    cleaned_tokens = []
    for raw_text in texts:
        if not isinstance(raw_text, str) or raw_text.strip() == "":
            continue
        
        lowered_str = raw_text.lower().strip()
        print(lowered_str)

        potential_words = lowered_str.split()
        print(potential_words)
        
        cleaned_tokens.extend([word for word in potential_words])

    print(cleaned_tokens)




def main():
    test = clean_text(data_a)


if __name__ == "__main__":
    main()
