class Solution(object):
    def test_nesting(self, s):
        openingkeychars = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        closingkeychars = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stk = []
        for c in s:
            if c in openingkeychars:
                stk.append(c)
            elif c in closingkeychars:
                p = stk.pop()
                if p != closingkeychars[c]:
                    return 0
            else:
                continue

        if not stk:
            return 1
        else:
            return 0


sol = Solution()


ret = sol.test_nesting('{[d()d]}')

print(f'return is {ret}')

ret = sol.test_nesting('{[d()d}')

print(f'return is {ret}')
ret = sol.test_nesting('{[d(d]')

print(f'return is {ret}')

ret = sol.test_nesting('{[d(dd)d]}')
print(f'return is {ret}')

ret = sol.test_nesting('{[d(dd])d}')
print(f'return is {ret}')
