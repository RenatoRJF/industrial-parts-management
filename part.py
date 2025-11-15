"""
Módulo Part - Representa uma peça produzida
"""


class Part:
    """Classe que representa uma peça produzida"""

    def __init__(self, part_id, weight, color, length):
        self.id = part_id
        self.weight = weight
        self.color = color.lower()
        self.length = length
        self.approved = False
        self.rejection_reasons = []
        self._validate_quality()

    def _validate_quality(self):
        """Valida se a peça atende aos critérios de qualidade"""
        approved = True

        # Validar peso (95g a 105g)
        if not (95 <= self.weight <= 105):
            approved = False
            self.rejection_reasons.append(f"Peso fora do padrão: {self.weight}g (esperado: 95g-105g)")

        # Validar cor (azul ou verde)
        if self.color not in ['azul', 'verde']:
            approved = False
            self.rejection_reasons.append(f"Cor inválida: {self.color} (esperado: azul ou verde)")

        # Validar comprimento (10cm a 20cm)
        if not (10 <= self.length <= 20):
            approved = False
            self.rejection_reasons.append(f"Comprimento fora do padrão: {self.length}cm (esperado: 10cm-20cm)")

        self.approved = approved

    def __str__(self):
        status = "APROVADA" if self.approved else "REPROVADA"
        info = f"ID: {self.id} | Peso: {self.weight}g | Cor: {self.color} | Comprimento: {self.length}cm | Status: {status}"

        if not self.approved:
            info += f"\n  Motivos: {'; '.join(self.rejection_reasons)}"
        return info
