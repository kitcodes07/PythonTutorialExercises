from multiprocessing.context import assert_spawning


class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self,val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

_ls = Stack()
_as = Stack()
_fs = Stack()

_ls.push(1)
_as.push(_ls.pop() + 1)
_fs.push(_as.pop() - 2)

print(_fs.pop())
