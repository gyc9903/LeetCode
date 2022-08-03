"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：
1.读入字符串并丢弃无用的前导空格
2.检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
3.读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
4.将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
5.如果整数数超过 32 位有符号整数范围 [−2^31,  2^31 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −2^31 的整数应该被固定为 −2^31，
  大于 2^31 − 1 的整数应该被固定为 2^31 − 1 。
6.返回整数作为最终结果。

方法一：自动机
我们也可以用下面的表格来表示这个自动机：
	       ' '	    +/-	     number	   other
start	   start	signed	in_number	end
signed	    end	     end	in_number	end
in_number	end	     end	in_number	end
end	        end	     end	end	        end
"""
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    # 自动机
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0  # 存储当前数字
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans


num = ' -42'
so = Solution().myAtoi(num)
print(so)
