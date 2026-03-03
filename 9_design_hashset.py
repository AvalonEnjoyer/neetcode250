class MyHashSet:
    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashset else False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
# [[],[1],[2],[1],[3],[2],[2],[2],[2]]
# expected [null,null,null,true,false,null,true,null,false]