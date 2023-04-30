from heap import Heap


def test_heap_init_binary():
    test = Heap([10, 5, 3, 3, 2, 1, 0, 0], 2)
    assert test.get_list() == [10, 5, 3, 3, 2, 1, 0, 0]
    assert test.get_airty() == 2
    assert test.get_root() == 10
    assert test.size() == 8
    assert test.get_children(0) == [1, 2]
    assert test.get_children(1) == [3, 4]
    assert test.get_children(2) == [5, 6]
    assert test.get_children(3) == [7]
    assert test.get_children(7) == []
    assert test.get_parent(1) == 0
    assert test.get_parent(2) == 0
    assert test.get_parent(3) == 1
    assert test.get_parent(4) == 1
    assert test.get_parent(5) == 2
    assert test.get_parent(6) == 2


def test_heap_init_triple():
    test = Heap([20, 15, 12, 13, 14, 12, 10, 10, 8, 10, 10, 5, 1, 1], 3)
    assert test.get_list() == [20, 15, 12, 13, 14, 12, 10,
                               10, 8, 10, 10, 5, 1, 1]
    assert test.get_airty() == 3
    assert test.get_root() == 20
    assert test.size() == 14
    assert test.get_children(0) == [1, 2, 3]
    assert test.get_children(1) == [4, 5, 6]
    assert test.get_children(2) == [7, 8, 9]
    assert test.get_children(3) == [10, 11, 12]
    assert test.get_children(4) == [13]
    assert test.get_parent(1) == 0
    assert test.get_parent(2) == 0
    assert test.get_parent(3) == 0
    assert test.get_parent(4) == 1
    assert test.get_parent(5) == 1
    assert test.get_parent(6) == 1
    assert test.get_parent(7) == 2
    assert test.get_parent(8) == 2
    assert test.get_parent(9) == 2
    assert test.get_parent(10) == 3
    assert test.get_parent(11) == 3
    assert test.get_parent(12) == 3

def test_insert_2_ary():
    test = Heap([10,20,30],2)

    assert test.get_list() == [30, 20, 10]

def test_remove_2_ary():
    test = Heap([10, 20, 30],2)
    test.remove_root()

    assert test.get_list() == [20, 10]

def test_insert_5_ary():
    test = Heap([10,20,30,40,50,60],5)

    assert test.get_list() == [60,20,30, 40, 50, 10]

def test_remove_5_ary():
    test = Heap([10, 20, 30, 40, 50, 60],5)
    test.remove_root()

    assert test.get_list() == [50,20,30, 40,10]