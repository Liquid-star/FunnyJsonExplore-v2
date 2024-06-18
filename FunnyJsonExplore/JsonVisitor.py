from abc import ABC, abstractmethod


# 抽象visitor类, 用于访问者模式
class JsonVisitor(ABC):
    @abstractmethod
    def visit(self, obj): pass
