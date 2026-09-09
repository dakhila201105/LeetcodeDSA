from collections import Counter


class Solution:

  def originalDigits(self, s: str) -> str:
    # Count frequencies of all characters in the input string
    counts = Counter(s)

    # Array to store the frequency of each digit from 0 to 9
    digit_counts = [0] * 10

    # Step 1: Count unique identifiers
    digit_counts[0] = counts["z"]
    digit_counts[2] = counts["w"]
    digit_counts[4] = counts["u"]
    digit_counts[6] = counts["x"]
    digit_counts[8] = counts["g"]

    # Step 2: Deduce the remaining digits based on unique counts
    digit_counts[3] = counts["h"] - digit_counts[8]
    digit_counts[5] = counts["f"] - digit_counts[4]
    digit_counts[7] = counts["s"] - digit_counts[6]
    digit_counts[1] = (
        counts["o"] - digit_counts[0] - digit_counts[2] - digit_counts[4]
    )
    digit_counts[9] = (
        counts["i"] - digit_counts[5] - digit_counts[6] - digit_counts[8]
    )

    # Build the final sorted result string
    result = []
    for digit in range(10):
      result.append(str(digit) * digit_counts[digit])

    return "".join(result)
