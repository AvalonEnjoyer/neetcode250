# Solution 1- 100% runtime and 91.29% memory

class MyHashSet:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]
        return True if key in bucket else False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(1)
# obj.remove(0)
# param_3 = obj.contains(0)
# print(param_3)

# ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
# [[],[1],[2],[1],[3],[2],[2],[2],[2]]
# expected [null,null,null,true,false,null,true,null,false]

# set = MyHashSet()
# print(set)