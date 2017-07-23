from trie import Trie
import time
def main():
	start = time.time()
	words = []
	with open("languages/english.txt") as file:
		words = file.read().splitlines()
	t = Trie(words)
	start = time.time()
	print(t.same_prefix("cat")[:10])
	print(time.time() - start)

main()