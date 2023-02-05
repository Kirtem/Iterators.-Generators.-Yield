import types

class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_list = list_of_lists

    def __iter__(self):
        self.list_iter = iter(self.list_of_list)
        self.inner_list = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.inner_list) == self.cursor:
            self.inner_list = None
            self.cursor = 0
            while not self.inner_list:
                self.inner_list = next(self.list_iter)
        return self.inner_list[self.cursor]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def flat_generator(list_of_lists):
    for list in list_of_lists:
        for item in list:
            yield item

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

for a in flat_generator(lists):
    print(a)

if __name__ == '__main__':
    test_2()
    test_1()

