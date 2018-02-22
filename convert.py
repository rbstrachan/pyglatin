play_again = True

suffix = "ay"

while play_again:
	original = raw_input("\nEnter a word to be converted into PygLatin: ")
	
	if len(original) > 0 and original.isalpha():
		word = original.lower()
		first_letter = word[0]
		slice = word[1:len(word)]
		final = slice + first_letter + suffix
		print "'" + original.title() + "'" + " in PygLatin is " + "'" + final.title() + "'"
		print
	else:
		print "Im sorry. That didn't work. Please enter a word consisting of only alpha [non-numeric] characters."
		print
	
	again = raw_input("Would you like to convert another word? ")
	if again.lower() == "no" or again.lower() == "n":
		play_again = False
