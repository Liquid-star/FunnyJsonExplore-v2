import json
from FunnyJsonExplore.JsonNode import JsonNode


class JsonTree:
    def __init__(self):
        self.container = JsonNode("根容器", None, 0, is_last=False)

    def load(self, data):
        # 递归解析数据
        self._parse_data(data, self.container)

    # 从文件加载数据(对外接口)
    def load_from_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.load(data)

    # 递归解析数据，建树
    def _parse_data(self, data, parent):
        if isinstance(data, dict):
            # 遍历字典
            for key, value in data.items():
                if isinstance(value, dict):  # dict才给container，否则给leaf
                    container = JsonNode(key, value, parent.level + 1, is_last=False)
                    parent.add(container)
                    self._parse_data(value, container)
                else:
                    leaf = JsonNode(key, value, parent.level + 1, is_last=False, is_leaf=True)
                    parent.add(leaf)


    # 访问者模式
    def accept(self, visitor):
        visitor.visit(self.container)


if __name__ == "__main__":
    #模块测试
    explorer = JsonTree()
    explorer.load_from_file("data1.json")
    for node in explorer.container:
        print(f"{' ' * node.level * 2}{node.key}: {node.value}")

