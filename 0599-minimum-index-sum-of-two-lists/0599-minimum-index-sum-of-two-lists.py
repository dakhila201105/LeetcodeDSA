class Solution:

  def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
    # Ensure list1 is always the shorter list to optimize space
    if len(list1) > len(list2):
      return self.findRestaurant(list2, list1)

    # Map the shorter list
    short_map = {string: i for i, string in enumerate(list1)}

    result = []
    min_sum = float("inf")

    # Iterate through the longer list
    for j, string in enumerate(list2):
      if string in short_map:
        current_sum = short_map[string] + j

        if current_sum < min_sum:
          min_sum = current_sum
          result = [string]
        elif current_sum == min_sum:
          result.append(string)

    return result
