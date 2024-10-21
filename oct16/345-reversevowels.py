class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        vowel_indices = []
        vowel_chars = []

        for i in range(len(s)):
            if s[i] in vowels:
                vowel_indices.append(i)
                vowel_chars.append(s[i])

        vowel_chars.reverse()

        for i, index in enumerate(vowel_indices):
            s_list[index] = vowel_chars[i]

        return ''.join(s_list) 