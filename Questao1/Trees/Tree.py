from Questao1.Nodes.Node import Node


class Tree:
    """
    • Recebe dados na forma de percurso preOrder e inOrder e retorna o posOrder
    """
    def __init__(self) -> None:
        self.__root = None

    # método get e setter
    @property
    def root(self) -> Node: return self.__root

    @root.setter
    def root(self, new_data) -> None: self.__root = new_data

    def insert(self) -> None:
        """
        Insere na árvore já pré-definida no exercício:
        • montagem manual da árvore
        :return:
        """
        data = input().split()[0]
        f = Node('F')
        e = Node('E')
        c = Node('C')
        d = Node('D')
        b = Node('B')
        a = Node('A')
        a.left_node = b
        a.right_node = d
        b.left_node = c
        d.left_node = e
        d.right_node = f
        self.root = a
        list_: list[Node] = [a, b, c, d, e, f]
        length: int = len(data)
        for index, char in enumerate(data):  # substitui o valor presente no nó pelo inserido
            list_[index].data = char
        for nodes in list_[length:]:  # removo aqui a impressão dos valores já existentes na árvore, se esta,
            nodes.data = ''           # por sua vez, não for, totalmente, preenchida

    def posOrder(self, node: Node) -> None:
        """
        • Retorna a impressão por meio do percurso em post order!
        :param node:
        :return:
        """
        if node is None: node = self.root
        if node.left_node: self.posOrder(node.left_node)
        if node.right_node: self.posOrder(node.right_node)
        print(node.data, end='')
