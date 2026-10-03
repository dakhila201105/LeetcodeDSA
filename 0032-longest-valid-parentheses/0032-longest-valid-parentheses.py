class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to serve as a base boundary tracker
        st = [-1]
        m_length = 0
        
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                
                if not st:
                    st.append(i)
                else:
                    m_length = max(m_length, i - st[-1])
                    
        return m_length
