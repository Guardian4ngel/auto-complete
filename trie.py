import string
import sys
END = '_END_' # A constant representing the end of a word. All leaves are equal to '_END_'

class Trie:
    """
    A data structure that will be used to find the suffixes of user submited words.
    """
    def __init__(self, words):
        """
        Construct a trie from a list of words.
        """
        self.root = dict()
        # Add each letter of each word self.root. This will create a very large series of nested dictionaries.
        for word in words:
            current_prefix = self.root
            for letter in word:
                # Creates a new dictionary if one at that letter does not exist. Does nothing otherwise.
                current_prefix = current_prefix.setdefault(letter, {})
            current_prefix[END] = END

    def same_prefix(self, prefix):
        current_dict = self.root
        # Get the location of the end of the prefix from the trie.
        # If the prefix does not exist in the trie, return an empty list.
        for letter in prefix:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return []

        suffixes = self.find_suffixes(current_dict)
        result = []
        for suffix in suffixes:
            result.append(prefix + suffix)
        return result

    def find_suffixes(self, trie):
        """
        Find all of the words that start at a given point in a trie.
        """
        my_list = []
        for key,value in trie.items():
            if key != END:
                for letter in self.find_suffixes(value):              
                    my_list.append(key + letter)
            else:
                my_list.append('')

        return my_list