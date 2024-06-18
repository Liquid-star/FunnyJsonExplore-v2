from FunnyJsonExplore.styles.style_factory import ComponentFactory
from FunnyJsonExplore.styles.components.rectangle_container_leaf import RectangleContainer, RectangleLeaf


# ┌──📦oranges  ────────────────────────────────────────┐
# │   ├──📦mandarin  ───────────────────────────────────┤
# │   │   ├──📖clementine  ─────────────────────────────┤
# │   │   ├──📖tangerine cheap & juicy! ────────────────┤
# │   ├──📦mandarin1  ──────────────────────────────────┤
# │   │   ├──📖clementine  ─────────────────────────────┤
# │   │   ├──📖tangerine cheap & juicy! ────────────────┤
# ├──📦apples  ─────────────────────────────────────────┤
# │   ├──📖gala  ───────────────────────────────────────┤
# └───┴──📖pink lady  ──────────────────────────────────┘

# 矩形风格组件工厂
class RectangleComponentFactory(ComponentFactory):
    # 构造函数，初始化容器图标和叶子图标
    def __init__(self, container_icon="", leaf_icon=""):
        self.leaf_icon = leaf_icon
        self.container_icon = container_icon

    # 创建容器
    def create_container(self, name, is_root=False, is_first=False):
        return RectangleContainer(name, self.container_icon, is_root)

    # 创建叶子
    def create_leaf(self, name, value=None):
        return RectangleLeaf(name, self.leaf_icon, value)
