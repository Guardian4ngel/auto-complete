# Word Jolt 
### A Multilingual Word Completer

Word Jolt is a lightweight word completion program, as seen on mobile phone keyboards. For those unfamiliar with auto-completion, this means that Word Jolt will take in any series of characters in the selected language, and return a list of all possible words that have the submitted word as a prefix. Currently, Word Jolt supports: English, French, German and Spanish

### Implementation Details
Word Jolt utilizes tries (https://en.wikipedia.org/wiki/Trie) to perform individual word lookups in O(k) time, where k is the length of the word. This is VERY fast. Because Word Jolt performs suffix look ups from the last character of the user submitted prefix (the root of the word) as opposed to the root of the trie, generating a list of suffixes can be done in O(n * s) time, where n is the amount of suffixes the word has, and s is the length of said suffixes, as opposed to O(n * k), where k is the length of the concatenated prefix and suffix.

### Installation and Usage

Requirements: Python 3

Usage: Simply execute main.py to run the program.