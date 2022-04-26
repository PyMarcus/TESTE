def parenthesisChecker(expression: str) -> None:
    """
    •   Primeiramente, verifica se a quantidade de pontos da primeira lista é menor que a segunda(o que indica
        posições anteriores de fechamento ou n.
        Feito isso, olha se a quantidade é igual,pois, se o for, está batendo.
    :param: expression : String
    :return: None
    """
    entry: list[int] = [index for index, char in enumerate(expression) if char == "("]
    close: list[int] = [index for index, char in enumerate(expression) if char == ")"]
    if sum(entry) < sum(close):
        if expression.count("(") == expression.count(")"): print("Está correto")
        else: print("Não está correto")
    else: print("Não está correto")


if __name__ == '__main__':
    parenthesisChecker(input())
