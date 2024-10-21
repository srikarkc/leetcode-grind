# Cracking the coding interview

## Arrays and Strings

### Problem 1: Unique Characters

Remember to check if its the characters are ASCII or Unicode.

ASCII is only 7-bits (0-127) with 1 bit reserved for parity checking.
Extended ASCII is 8-bits (1 byte / 0-255).
Unicode (UTF-8) is variable encoding 0-4 bytes.

If string length > the unique chars -> return False.
e.g. if using ASCII and string length > 128 -> return False

Using bitwise operations saves space by a factor of 8.

Remember bitwise AND (&), OR (|), LEFTSHIFT(<<)

### Problem 2: Check Permutation

Remember to ask about spaces and cases. 
If 'Hel' a permutation of 'leh' or 'hel  ' a permutation of 'leh'.

If length of strings are un-equal -> return False.

If using sorted method on Strings -> runtime O(nlogn) and space O(n) since the sorted method creates a new list.

Better to use character_count approach by saving in a dictionary.

Remember this shortcut:
`my_dictionary[key] = my_dictionary.get(key, 0) + 1`
This return 0 if my_dictionary does not have the specified key, if it does, adds 1 to the value.

### Problem 3: URLify

Remember in Python that the slicing syntax is inclusive of the first character and exclusive of the second.
string[:5] -> string[0] to string[4]

The .strip() method for strings removes leading and trailing spaces.

### Problem 4: Palindrome permutation

Remember that we need to have an even number of characters with at most 1 odd character (in the middle).
Also, make sure to ask about case - if not, convert everything to lowercase - lower()

There's also a bit operation solution that's a bit more challenging (no pun intended).
bit_vector & (bit_vector - 1) == 0 -> If there's only 1 value in bit_vector that is 1 (in binary)

### Problem 5: String - one operation away

Remember to use the .zip() method to get a zip of the 2 strings and use two iterators.
Can also do it with a single method.

### Problem 6: String Compression

Dictionary won't work since consecutive characters need to be counted separately.
Better to convert to list to use the append method.
