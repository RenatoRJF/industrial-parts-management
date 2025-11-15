"""
Módulo Box - Representa uma caixa de armazenamento
"""


class Box:
    """Classe que representa uma caixa de armazenamento"""

    MAX_CAPACITY = 10

    def __init__(self, number):
        self.number = number
        self.parts = []
        self.closed = False

    def add_part(self, part):
        """Adiciona uma peça à caixa se houver espaço"""
        if self.closed:
            return False

        if len(self.parts) < self.MAX_CAPACITY:
            self.parts.append(part)
            if len(self.parts) == self.MAX_CAPACITY:
                self.close()
            return True
        return False

    def close(self):
        """Fecha a caixa quando atingir capacidade máxima"""
        self.closed = True

    def __str__(self):
        status = "FECHADA" if self.closed else "ABERTA"
        return f"Caixa #{self.number} - {status} - Peças: {len(self.parts)}/{self.MAX_CAPACITY}"
