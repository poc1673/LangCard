# Laundry list for Adaptive Flash Cards.

1. Write function to extract 1 to 10 grams. Use it to extract the unique ngrams from the current corpus.
2. Write function to create **realistically** long sentences bounded by some number of character.
3. Map each of the sentences to the ngrams from step 1.






## Data pipeline for flash cards.

The purpose of this program is to aim to test the user with phrases from a corpus which will reinforce familiarity with phrases and vocabulary in the target language.

The core of the program is a set of ngrams each of which bears a score giving the user's familiarity with them. The idea is for this to be similar to the "Easy", "Good", "Hard", and "Repeat" method utilized by Anki, only in a continuous context. User familiarity scores (UFS) will be scored based on three factors:

1. The number of correct responses compared to the number of exposures that are given.
2. The time that it takes to translate the phrase.
3. The "correctness" of the result as measured by how the result compares to the translation that's available.

Each ngram and its USF is tied to a corpus of phrases containing it, or its stem.

For example, if we have the French verb *etudier*, with some score, *\alpha* will have a set of values linked to it:

* J'etudie la Francais.
* Ils

##
