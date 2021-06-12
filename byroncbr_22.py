"""
Name: byroncbr_22.py
Author: bangrenc
Time: 18/10/2020 10:33 AM
"""

def generateParenthesis(n):
    result = []
    def searchParenthesis(value, open, close, N):
        # 假如总共的value字符串长度是maxN*2，那就记录下来！
        if (len(value) == N*2):
            result.append(value)
            return

        # "（"个数不超过maxN
        if open < N:
            searchParenthesis(value + "(", open+1, close, N)
        # 假如现存的"（"也就是open个数大于 close，那就说明缺少"）"，假如open小于等于close，那就说明close "）"够了！
        # close从0开始，所以小于open就可以！
        if close < open:
            searchParenthesis(value + ")", open, close+1, N)

    searchParenthesis("", 0, 0, n)
    print(result)
    return result

if __name__ == '__main__':
    n = 3
    result = generateParenthesis(n)





