import collections
    class Leaf:
        def _init_(self, key:str, value: int):
            self.key =key
            self.value = value
    class Node:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right
    class Haffman:
        data: list

        def _init_(self):
            self._code_table = dict()
            self._data = []
            self._real_str = ''

        def _make_list_(self, real_str):
            counter =dict(collections.Counter(real_str))
            counter = collections.OrderedDict(sorted(counter.items(), key=lambda k: k[1], reverse = True))
            for key, value in counter.items():
                self.data.append(Leaf(key, value))
            return True
        def _haffmans_tree_(self):
            while len(self.data)>2:
                b, a = self._data.pop(), self._data.pop()
                spam = Node(a.value+b.value, a, b)
                if spam.value > self._data[0].value:
                    self._data.insert(0, spam)
                elif spam.value < self.data[-1].value:
                    self._data.append(spam)
                else:
                    for i in range(i, len(self.data)):
                        if self._data(i-1).value >=spam.value>self._data[i].value:
                            self.data.insert(i,spam)
                            break
            self_data = Node(self._data[0].value + self._data[1].value, self._data[0], self._data[1])
        def _haffmans_recursion_(self, dta:Node, code=''):
            if isinstance(data, Node):
                self._haffmans_recursion(data.left, code=code + '0')
                self._haffmans_recursion(data.left, code=code + '1')
            elif isinstance(data, Leaf):
                self._code_table[data.key] = code
        def _encode(self):
            result = []
            for char in self._real_str:
                result.append(self._code_table[char])
                return ''.join(result)

        def encode(self, real_str):
            self._init_()
            self.real_str = real_str
            self.make_list(real_str)
            self.haffmans_tree()
            self.haffmans_recursion(self._data)
            code_str = self._encode()
            return code_str

        def decode(self, code_str, code_table=None):
            if _code_table:
                self._code_table = code_table
            decode_table = {value: key for key, value in self._code_table.items()}
            result = []

            i = 0
            while i< len(code_str):
               while code_str[i:j] not in decode_table.keys():
                  j+=i
               result.append(decode_table[code_str[i:j]])
               i=j
            real_str = ''.join(result)
            return real_str

        def get_table_code(self):
            if self._code_table:
                return self._code_table
            return False

        def get_real_string_code(self):
            if self._real_str:
                result = []
                for char in self.real_str:
                    result.append(bin(ord(char))[2:].zfill(8))
                return ''.join(result)
            return False


#if __name__ == '_main_':
    my_str = input('Введите строку: ')
    haf = Haffman()
    code_s = haf.encode(my_str)
    print(haf.get_real_string_code())
    print(code_s)
    table = haf.get_table_code()
    print(table)
    real_1 = haf.decode(code_s, table)
    real_2 = haf.decode(code_s)
    print(real_1)
    print(real_2)
