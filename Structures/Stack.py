from typing import Optional, Union, Generator


class StackObj:
    data: str
    pnext: Optional["StackObj"]

    def __init__(self, data: str):
        self.data = data
        self.pnext = None


class Stack:
    def __init__(self):
        self.top: Optional[StackObj] = None
        self.__size: int = 0

    def push_back(self, obj: StackObj) -> None:
        if not self.top:
            self.top = obj
        else:
            self.__get_stack_obj_by_index(self.__size-1).pnext = obj

        self.__size += 1

    def push_front(self, obj: StackObj) -> None:
        obj.pnext = self.top
        self.top = obj
        self.__size += 1

    def pop(self) -> Optional[StackObj]:
        self.__size -= 1
        if not self.top or not self.top.pnext:
            to_return = self.top
            self.top = None
            return to_return
        else:
            prev_last = self.__get_stack_obj_by_index(self.__size - 2)
            to_return = prev_last.pnext
            prev_last.pnext = None
            return to_return

    def validate_index(self, ind: int) -> None:
        if not (0 <= ind < self.__size):
            raise IndexError('неверный индекс')

    def __get_stack_obj_by_index(self, ind: int) -> StackObj:
        self.validate_index(ind)
        curr_obj = self.top
        for _ in range(ind):
            curr_obj = curr_obj.pnext
        return curr_obj

    def __getitem__(self, ind: int) -> str:
        return self.__get_stack_obj_by_index(ind).data

    def __setitem__(self, ind: int, value: str) -> None:
        self.__get_stack_obj_by_index(ind).data = value

    def __iter__(self) -> Union["Stack", Generator]:
        curr_obj: StackObj = self.top
        while curr_obj:
            yield curr_obj
            curr_obj = curr_obj.pnext

    def __len__(self) -> int:
        return self.__size
