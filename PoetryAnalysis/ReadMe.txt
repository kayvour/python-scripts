A Python script that analyzes a poem text file for various poetic features including syllable counts, vocabulary richness, sentiment, rhyme scheme, and common poetic devices such as alliteration, anaphora, and repetition.

Usage:
Run the script with:
python analyze_poem.py [path_to_poem_file]

-[path_to_poem_file] (optional): Path to the poem text file to analyze. If not provided, defaults to poem.txt in the current working directory.

Output:
JSON-formatted analysis printed to the console, containing:
- syllables_per_line: List of syllable counts for each line.
- avg_syllables_per_word: Average number of syllables per word.
- vocab_richness: Ratio of unique words to total words.
- sentiment: Overall sentiment of the poem (positive, neutral, or negative).
- rhyme_scheme: Detected rhyme scheme (letters representing rhyme groups).
- poetic_devices: Detected poetic devices:
-- alliteration: List of two-word phrases with repeated starting consonants.
-- anaphora: List of words repeated at the start of lines.
-- repetition: List of repeated words longer than 3 letters.

Additional Notes:
-The script automatically downloads required NLTK data packages (punkt, averaged_perceptron_tagger, vader_lexicon, cmudict) on first run.
-If the poem file is not found at the specified path, the script returns an error JSON: {"error": "File not found"}.
-Rhyme detection is based on phonetic matching using the CMU Pronouncing Dictionary (nltk.corpus.cmudict).

