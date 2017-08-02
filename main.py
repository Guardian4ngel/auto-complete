from trie import Trie
import time
import sys

accepted_languages = ["english", "french", "german", "spanish"]
def select_language():
	language = ""
	while language not in accepted_languages:
		print("Please select a language from the list of given choices:")
		print("English\nFrench\nGerman\nSpanish\n")
		language = input().lower()
	return language

def main():
	start = time.time()
	words = []
	print("Welcome to Word Jolt!")
	language = select_language()
	with open("languages/" + language + ".txt") as file:
		words = file.read().splitlines()
	t = Trie(words)
	print("Type in any word to generate a list of words that have a matching suffix.")
	print("Type \"quit!\" to quit the program.")
	while(True):
		word_input = input("Enter a word: ")
		if word_input == "quit!":
			sys.exit()
		for word in t.same_prefix(word_input):
			print(word)

if __name__ == "__main__":
	main()

