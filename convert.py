def rep():
  pyg = "ay"
  original = raw_input("Enter a word: ")
  
  if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    slice = word[1:len(word)]
    final = slice + first + pyg
    print final
  else:
    print "Im sorry. That didn't work. Please enter a word consisting of only alpha characters."

rep()
