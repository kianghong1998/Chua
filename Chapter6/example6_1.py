def are_anagrams (wordl, word2):
	"""Return True, if words are anagrams."""
	#2 Sort the characters in the words
	wordl_sorted = sorted (wordl)   #sorted returns a sorted list
	word2_sorted = sorted (word2)


	#3 Check that the sorted words are identical.
	if wordl_sorted == word2_sorted: # compare sorted lists
		return True
	else:
		return False

	print(word1_sorted)
	print(word2_sorted)

def are_anagrams (word1, word2):
    """Return True, if words are anagrams"""
    word1_sorted = sorted (word1)
    word2_sorted = sorted (word2)

    if word1_sorted == word2_sorted:
        return True
    else:
        return False

print ("Anagram Test")

two_words = input ("Enter two seperated words: ")
word1,word2 = two_words.split() #split into a list of words

if are_anagrams(word1,word2):      #Return true or false
    print ("The words are anagrams.")
else:
    print("The words are not anagrams.")
