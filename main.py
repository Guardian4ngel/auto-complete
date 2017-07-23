from trie import Trie
import time
import sys
def main():
	start = time.time()
	words = []
	with open("languages/english.txt") as file:
		words = file.read().splitlines()
	t = Trie(words)

	print("Type \"exit()\" to quit the program.")
	while(True):
		word_input = input("Enter a word: ")
		if word_input == "exit()":
			sys.exit()
		for word in t.same_prefix(word_input):
			print(word)
main()