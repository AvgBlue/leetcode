# Implement this class yourself
class Pair:
    def __init__(self,val):
        self.tree={'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None, 'j': None, 'k': None, 'l': None, 'm': None, 'n': None, 'o': None, 'p': None, 'q': None, 'r': None, 's': None, 't': None, 'u': None, 'v': None, 'w': None, 'x': None, 'y': None, 'z': None}
        self.val:int=val

class MapSum:
    def __init__(self):
        self.map={}
        self.head_pair=Pair(-1)

    def insert(self, key: str, val: int) -> None:
        is_exist=key in self.map
        old_val=0
        if is_exist:
            old_val=self.map[key]
        self.map[key]=val
        runner=self.head_pair
        for c in key:
            if runner.tree[c] is None:
                runner.tree[c]=Pair(val)
                runner=runner.tree[c]
                continue
            runner=runner.tree[c]
            runner.val+=val-old_val


    def sum(self, prefix: str) -> int:
        result=0
        runner=self.head_pair
        for c in prefix:
            if runner.tree[c] is None:
                return 0
            runner=runner.tree[c]
        result=runner.val
        return result



def run_tests():
    print("Test 1: LeetCode example")
    m = MapSum()

    m.insert("apple", 3)
    assert m.sum("ap") == 3

    m.insert("app", 2)
    assert m.sum("ap") == 5

    print("Passed Test 1")


    print("Test 2: Updating existing key")
    m = MapSum()

    m.insert("apple", 3)
    assert m.sum("ap") == 3

    m.insert("apple", 5)

    # apple should now be worth 5, not 3 + 5
    assert m.sum("ap") == 5

    print("Passed Test 2")


    print("Test 3: Multiple matching keys")
    m = MapSum()

    m.insert("apple", 3)
    m.insert("app", 2)
    m.insert("application", 5)
    m.insert("banana", 10)

    assert m.sum("ap") == 10
    assert m.sum("app") == 10
    assert m.sum("apple") == 3

    print("Passed Test 3")


    print("Test 4: Prefix with no matches")
    m = MapSum()

    m.insert("apple", 3)
    m.insert("banana", 5)

    assert m.sum("cat") == 0
    assert m.sum("z") == 0

    print("Passed Test 4")


    print("Test 5: One-character keys")
    m = MapSum()

    m.insert("a", 1)
    m.insert("ab", 2)
    m.insert("abc", 3)

    assert m.sum("a") == 6
    assert m.sum("ab") == 5
    assert m.sum("abc") == 3

    print("Passed Test 5")


    print("Test 6: Similar prefixes")
    m = MapSum()

    m.insert("car", 3)
    m.insert("card", 4)
    m.insert("cat", 5)
    m.insert("dog", 10)

    assert m.sum("ca") == 12
    assert m.sum("car") == 7
    assert m.sum("cat") == 5
    assert m.sum("do") == 10

    print("Passed Test 6")


    print("Test 7: Update affects prefix sums")
    m = MapSum()

    m.insert("car", 3)
    m.insert("card", 4)

    assert m.sum("car") == 7

    m.insert("car", 10)

    assert m.sum("car") == 14

    print("Passed Test 7")

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()
    # new_dict_level={}
    # for c in "abcdefghijklmnopqrstuvwxyz":
    #     new_dict_level[c]=None
    # print(new_dict_level)