import nltk
import textstat
from textblob import TextBlob
import re
from collections import Counter
import os

# Download required nltk data once
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
nltk.download('cmudict')

from nltk.corpus import cmudict
cmu_dict = cmudict.dict()

def get_rhyme_part(word):
    word = word.lower()
    if word not in cmu_dict:
        return None
    rhymes = []
    for pron in cmu_dict[word]:
        # find last stressed vowel and onwards
        for i in range(len(pron) - 1, -1, -1):
            if pron[i][-1].isdigit():
                rhyme_part = pron[i:]
                rhymes.append(tuple(rhyme_part))
                break
    return rhymes if rhymes else None

def rhymes(word1, word2):
    rhyme1 = get_rhyme_part(word1)
    rhyme2 = get_rhyme_part(word2)
    if not rhyme1 or not rhyme2:
        return False
    return any(r1 == r2 for r1 in rhyme1 for r2 in rhyme2)

def analyze_poem(file_path):
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    poem_text = "\n".join(lines)
    words = nltk.word_tokenize(poem_text.lower())
    total_words = len(words)
    unique_words = len(set(words))

    syllables_per_line = [textstat.syllable_count(line) for line in lines]
    total_syllables = sum(syllables_per_line)
    avg_syllables_per_word = round(total_syllables / total_words, 2) if total_words > 0 else 0

    vocab_richness = round(unique_words / total_words, 2) if total_words > 0 else 0

    sentiment_score = TextBlob(poem_text).sentiment.polarity
    if sentiment_score > 0.1:
        sentiment = "positive"
    elif sentiment_score < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    last_words = [line.split()[-1].lower() for line in lines if line.split()]
    rhyme_groups = {}
    scheme = ""
    current_letter = ord('A')

    for word in last_words:
        found = False
        for k, v in rhyme_groups.items():
            # check if current word rhymes with any word in group v
            if any(rhymes(word, w) for w in v):
                scheme += k
                rhyme_groups[k].add(word)
                found = True
                break
        if not found:
            new_letter = chr(current_letter)
            rhyme_groups[new_letter] = {word}
            scheme += new_letter
            current_letter += 1

    alliteration = []
    anaphora = []
    repetition = []

    line_start_words = []
    all_words = []
    for line in lines:
        words_in_line = nltk.word_tokenize(line.lower())
        if words_in_line:
            line_start_words.append(words_in_line[0])
            all_words.extend(words_in_line)
            for i in range(len(words_in_line) - 1):
                if words_in_line[i][0] == words_in_line[i + 1][0]:
                    phrase = f"{words_in_line[i]} {words_in_line[i + 1]}"
                    alliteration.append(phrase)

    counts = Counter(line_start_words)
    anaphora = [word for word, count in counts.items() if count > 1]

    word_counts = Counter(all_words)
    repetition = [word for word, count in word_counts.items() if count > 1 and len(word) > 3]

    return {
        "syllables_per_line": syllables_per_line,
        "avg_syllables_per_word": avg_syllables_per_word,
        "vocab_richness": vocab_richness,
        "sentiment": sentiment,
        "rhyme_scheme": scheme,
        "poetic_devices": {
            "alliteration": list(set(alliteration)),
            "anaphora": anaphora,
            "repetition": repetition
        }
    }

if __name__ == "__main__":
    result = analyze_poem("poem.txt")
    import json
    print(json.dumps(result, indent=2))
