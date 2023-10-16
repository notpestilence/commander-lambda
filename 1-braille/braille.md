# 1.1. Braille Translation

Write a function `solution(s)` that takes a string parameter and returns a string of 1’s and 0’s representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

---

# Explanation

This was fairly straightforward. One might need to look up Braille alphabet representations to (manually) initialise a dictionary containing all alphabets and all occurences of capitalisations and spaces. In other words, each alphabet would correspond to 6-digit Braille representations in the form of:
```
1 4
2 5
3 6
```
For a start, [here's a pointer](https://www.researchgate.net/publication/343406954/figure/fig1/AS:923337496727556@1597152222940/Braille-Alphabet-and-Numbers.png).

As an example, the alphabet 'e' (lowercase E) in Braille is:
```
DOT  NIL
NIL  DOT
NIL  NIL
```
Therefore its Braille representation would be `100010`.

It is worth noting that in Braille, words with capitalised first letter (e.g., "Google" and "Code") have different capital initialisations compared to words with all capitalisations (e.g., "GOOGLE" and "CODE"). Hence, it may be necessary to handle edge cases where words may be in all caps instead of only their first letter.