#Algorithm: Maintain a stack of key symbols. Push the opening key characters and pop when they get closed.
class Solution(object):

  #convert array of chars to string
  def convert(self, s):
    new = ""
    for x in s:
      new += x
    return new

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
    correctstr = []
    formatError = False

    for c in s:
        if c in openingkeychars:
            stk.append(c)
            correctstr.append(c)
        elif c in closingkeychars:
            if len(stk) == 0:
                correctstr.append(c)
                stk.append(c)
                formatError = True
            else:
                p = stk.pop()
                correctstr.append(c)
                if p != closingkeychars[c]:
                    formatError = True
                    stk.append(p)
                    stk.append(c)
        else:
            correctstr.append(c)
            continue

    #Detects if we have a matched open and closed key charactter. If we do, then there is problem. At this
    # point we cannot correct the string by appending at both ends if we encounter matched meta characters
    detection = {'(': False, ')': False, '{': False, '}' : False, '[': False, ']': True}
    if formatError:
        n = len(stk)
        for i in range(0, n):
            p = stk[i]
            if p in closingkeychars:
                if detection[closingkeychars[p]]:
                    return False
                detection[p] = True
                correctstr.insert(0, closingkeychars[p])
            elif p in openingkeychars:
                detection[p] = True
                correctstr.append(openingkeychars[p])
            else:
                continue

        return self.convert(correctstr)

    return True


sol = Solution()

ret = sol.test_nesting('{[d()d]}')

print(f'return is {ret}')

ret = sol.test_nesting(']-(')

print(f'return is {ret}')

ret = sol.test_nesting('({]]}')

print(f'return is {ret}')


ret = sol.test_nesting('} { [()] (()v()) } ])')

print(f'return is {ret}')

