class Solution:

  def countCommas(self, n: int) -> int:
    total_commas = 0
    curr = 1000
    while curr <= n:
      total_commas += n - curr + 1
      curr *= 1000
    return total_commas
