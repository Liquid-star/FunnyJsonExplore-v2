import json
from FunnyJsonExplore.JsonNode import JsonNode
from FunnyJsonExplore.JsonVisitor import JsonVisitor


class RenderVisitor(JsonVisitor):
    # 指定工厂即可完成初始化
    def __init__(self, factory):
        self.factory = factory
        self.container = self.factory.create_container("根容器", is_root=True)

    # 得到一个根结点，即为迭代器
    def visit(self, root):
        self.rebuild_tree(root)
        self.show()

    # 对结果进行展示
    def show(self):
        self.container.draw()

    # 利用JsonNode的dfs迭代器重建树,root的类型是JsonNode
    def rebuild_tree(self, root):
        # 用于存储每一层的最新节点
        node_map = {0: self.container}

        for node in root:
            if node.level == 0:
                continue  # 跳过根结点自身

            # 如果当前节点是叶子节点，那么创建一个叶子节点，否则创建一个容器节点
            if node.is_leaf:
                # print("find a leaf node")
                new_node = self.factory.create_leaf(node.key, node.value)
            else:
                # print("find a container node")
                new_node = self.factory.create_container(node.key)

            # 找到当前节点的父节点，然后将当前节点添加到父节点的子节点中
            parent_node = node_map[node.level - 1]
            parent_node.add(new_node)

            # 更新当前级别的最新节点
            node_map[node.level] = new_node
