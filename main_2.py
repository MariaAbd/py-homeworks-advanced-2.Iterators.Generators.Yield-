nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
    [
        [3, 9, True, [
            'false', 'not given', None
        ]]
    ]
]


class MyIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.list = []
        for item in self.nested_list:
            if type(item) is not list:
                print(item)
            else:
                item.__iter__()
        return self

    def __next__(self):
        if len(self.list) == 0:
            raise StopIteration
        return self.list.pop()


my_iterator = MyIterator(nested_list)
for i in my_iterator:
    print(i)

