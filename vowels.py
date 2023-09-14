def removeAllVowels(string):
   vowels = ["a", "e", "i", "o", "u", "y"]
   for letter in string:
        if letter.lower() in vowels:
            string = string.replace(letter, "")
   return string