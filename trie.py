import string
import sys
END = '_END_'

class Trie:

    def __init__(self, words):
        self.stack_depth = 0
        self.root = dict()
        for word in words:
            current_dict = self.root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[END] = END

    def in_trie(self, word):
        current_dict = self.root
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        else:
            if END in current_dict:
                return True
            else:
                return False

    def same_prefix(self, prefix):
        current_dict = self.root

        for letter in prefix:
            if letter in current_dict:
                current_dict = current_dict[letter]

        suffixes = self.find_suffixes(current_dict, prefix)
        result = []
        for suffix in suffixes:
            result.append(prefix + suffix)
        return result
        
    def find_suffixes(self, trie, prefix):

        my_list = []
        for k,v in trie.items():
            if k != END:
                for el in self.find_suffixes(v, prefix):              
                    my_list.append(k+el)
            else:
                my_list.append('')

        return my_list