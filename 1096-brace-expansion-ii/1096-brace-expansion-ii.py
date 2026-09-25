class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        st = [expression]
        v = set()
        r = set()
        
        while st:
            expr = st.pop()
            if '}' not in expr:
                r.add(expr)
                continue
            j = expr.find('}')
            i = expr.rfind('{', 0, j)
            before = expr[:i]
            after = expr[j+1:]
            options = expr[i+1:j].split(',')
            
            for option in options:
                next_expr = before + option + after
                if next_expr not in v:
                    v.add(next_expr)
                    st.append(next_expr)
                    
        return sorted(list(r))
