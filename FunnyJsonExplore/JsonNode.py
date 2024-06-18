# JsonNode类，用于存储json数据的树形结构
class JsonNode:
    def __init__(self, key, value, level=0, is_last=False, is_leaf=False):
        self.key = key
        self.value = value
        self.level = level
        self.is_last = is_last
        self.is_leaf = is_leaf
        self.children = []

    # node的类型是JsonNode
    def add(self, node):
        self.children.append(node)

    # 重载__iter__方法，使JsonNode对象可以迭代
    def __iter__(self):
        return JsonNodeIterator(self)


# JsonNodeIterator类，用于实现JsonNode的迭代器
class JsonNodeIterator:
    def __init__(self, root):
        self._stack = [(root, -1)]

    def __iter__(self):
        return self

    def __next__(self):
        while self._stack:
            node, index = self._stack[-1]
            if index == -1:
                self._stack[-1] = (node, index + 1)
                return node
            if index < len(node.children):
                self._stack[-1] = (node, index + 1)
                self._stack.append((node.children[index], -1))
            else:
                self._stack.pop()
        raise StopIteration
