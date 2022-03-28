nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class MyIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.list = []
        for item in self.nested_list:
            self.list += item
        # print(self.list)
        return self

    def __next__(self):
        if len(self.list) == 0:
            raise StopIteration
        return self.list.pop()


my_iterator = MyIterator(nested_list)
for i in my_iterator:
    print(i)

flat_list = [item for item in my_iterator]
# print(flat_list)

flat_list_gen = (item for item in my_iterator)
# for item in flat_list_gen:
#     print(item)









