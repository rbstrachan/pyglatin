suffix = "ay"
original = raw_input("Enter a word: ")
  
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first_letter = word[0]
  slice = word[1:len(word)]
  final = slice + first_letter + suffix
  print final
else:
  print "Im sorry. That didn't work. Please enter a word consisting of only alpha [non-numeric] characters."
