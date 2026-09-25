from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        l_m = {}
        s_r, s_c = -1, -1
        
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    s_r, s_c = r, c
                elif cell == 'L':
                    l_m[(r, c)] = len(l_m)
                    
        t_l = len(l_m)
        target_mask = (1 << t_l) - 1
        if t_l == 0:
            return 0
            
        queue = deque([(s_r, s_c, energy, 0)])
        v = {}
        v[(s_r, s_c, 0)] = energy
        
        moves = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            for _ in range(len(queue)):
                r, c, e, mask = queue.popleft()
                if mask == target_mask:
                    return moves
                    
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                        next_energy = e - 1
                        if next_energy < 0:
                            continue
                            
                        next_mask = mask
                        cell_type = classroom[nr][nc]
                        
                        if cell_type == 'R':
                            next_energy = energy
                        elif cell_type == 'L':
                            litter_id = l_m[(nr, nc)]
                            next_mask |= (1 << litter_id)
                        state_key = (nr, nc, next_mask)
                        if state_key not in v or v[state_key] < next_energy:
                            v[state_key] = next_energy
                            queue.append((nr, nc, next_energy, next_mask))
                            
            moves += 1
            
        return -1
