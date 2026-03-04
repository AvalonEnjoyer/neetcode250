# Solution 2 Dynamic Resizing hashmap
class MyHashMap:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0

    def _resize(self):
        old_bucket = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_bucket: # Rehash and move the items
            for key, value in bucket:
                self._insert_without_resize(key, value)

    def _insert_without_resize(self, key, value:int):
        bucket = self.buckets[self._hash(key)]
        bucket.append((key, value))
        self.count += 1

    def _hash(self, key:int):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]
        key_not_found = True
        for i, item in enumerate(bucket):
            if item[0] == key:
                key_not_found = False
                bucket[i]=(key,value)
                break
        if key_not_found:
            bucket.append((key,value))
            self.count += 1
        if self.count >= 0.75*self.size:
            self._resize()

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        for item in bucket:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for i,item in enumerate(bucket):
            if item[0] == key:
                bucket.pop(i)
                self.count -= 1
                return

# # Solution 1 - 100% runtime and 94.05% memory
# class MyHashMap:
#     def __init__(self, size=1000):
#         self.buckets = [[] for _ in range(size)]
#
#     def _hash(self, key:int):
#         return key % len(self.buckets)
#
#     def put(self, key: int, value: int) -> None:
#         bucket = self.buckets[self._hash(key)]
#         key_not_found = True
#         for i, item in enumerate(bucket):
#             if item[0] == key:
#                 key_not_found = False
#                 bucket[i]=(key,value)
#                 break
#         if key_not_found:
#             bucket.append((key,value))
#
#     def get(self, key: int) -> int:
#         bucket = self.buckets[self._hash(key)]
#         for item in bucket:
#             if item[0] == key:
#                 return item[1]
#         return -1
#
#     def remove(self, key: int) -> None:
#         bucket = self.buckets[self._hash(key)]
#         for i,item in enumerate(bucket):
#             if item[0] == key:
#                 bucket.pop(i)
#                 return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# ["MyHashMap","put","put","get","get","put","get","remove","get"]
# [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]

myhash = MyHashMap()

print(myhash.put(1,1))
print(myhash.put(2,2))
print(myhash.get(1))
print(myhash.get(3))
print(myhash.get(2))
print(myhash.put(2,1))
print(myhash.get(2))
