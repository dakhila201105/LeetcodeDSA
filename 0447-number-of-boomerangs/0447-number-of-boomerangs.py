class Solution:

  def numberOfBoomerangs(self, points: list[list[int]]) -> int:
    total_boomerangs = 0

    for p1 in points:
      distance_map = {}

      for p2 in points:
        # Calculate squared Euclidean distance: (x1 - x2)^2 + (y1 - y2)^2
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        dist = dx * dx + dy * dy

        # Update the frequency of this distance
        distance_map[dist] = distance_map.get(dist, 0) + 1

      # Calculate permutations for each distance group
      for count in distance_map.values():
        if count > 1:
          total_boomerangs += count * (count - 1)

    return total_boomerangs
