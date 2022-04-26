from typing import Any


class Node:
    def __init__(self, data: str, left_node: Any = None, right_node: Any = None) -> None:
        """
        ♦ Recebe o valor data e os nós esquerdos e direitos para ,posteriormente, estruturar a árvore
        :param data:
        :param left_node:
        :param right_node:
        """
        self.__data: str = data
        self.__left_node: Any = None
        self.__right_node: Any = None

    # métodos getters e setters, respectivamente
    @property
    def data(self) -> str: return self.__data

    @property
    def left_node(self) -> Any: return self.__left_node

    @property
    def right_node(self) -> Any: return self.__right_node

    @data.setter
    def data(self, new_data) -> None: self.__data = new_data

    @left_node.setter
    def left_node(self, new_data) -> None: self.__left_node = new_data

    @right_node.setter
    def right_node(self, new_data) -> None: self.__right_node = new_data

    # override
    def __str__(self) -> str:  # exibe o nó data, por padrão
        return self.__data
