from Trees.Tree import Tree
from multiprocessing import Process


class Main:
    @staticmethod
    def generateTree():
        """
        Inicia a árvore para chamada do método pretendido
        :return:
        """
        tree = Tree()  # pega apenas o primeiro texto, pois, ele já serve de referência
        tree.insert()
        tree.posOrder(tree.root) # processos criados só por frescura msm :D


if __name__ == '__main__':
    Main.generateTree()
