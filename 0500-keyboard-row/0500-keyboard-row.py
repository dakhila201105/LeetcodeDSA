class Solution:

  def findWords(self, words: list[str]) -> list[str]:
    # Define the three keyboard rows as sets of lowercase letters
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    result = []

    for word in words:
      # Convert the word to a lowercase set of its characters
      word_set = set(word.lower())

      # Check if the word's characters fit entirely within any single row
      if (
          word_set.issubset(row1)
          or word_set.issubset(row2)
          or word_set.issubset(row3)  
      ):
        result.append(word)

    return result
