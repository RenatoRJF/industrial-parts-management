"""
Módulo ManagementSystem - Sistema principal de gestão de peças
"""

from part import Part
from box import Box


class ManagementSystem:
    """Sistema principal de gestão de peças"""

    def __init__(self):
        self.approved_parts = []
        self.rejected_parts = []
        self.boxes = []
        self.current_box = None
        self.id_counter = 1
        self.box_counter = 1

    def register_part(self, peso, cor, comprimento):
        """Cadastra uma nova peça no sistema"""
        part = Part(self.id_counter, peso, cor, comprimento)
        self.id_counter += 1

        if part.approved:
            self.approved_parts.append(part)
            self._store_part(part)
            print(f"\n✓ Peça #{part.id} APROVADA e armazenada com sucesso!")
        else:
            self.rejected_parts.append(part)
            print(f"\n✗ Peça #{part.id} REPROVADA!")
            print(f"  Motivos: {'; '.join(part.rejection_reasons)}")

        return part

    def _store_part(self, part):
        """Armazena peça aprovada em caixa"""
        # Se não há caixa atual ou está fechada, criar nova
        if self.current_box is None or self.current_box.closed:
            self.current_box = Box(self.box_counter)
            self.boxes.append(self.current_box)
            self.box_counter += 1
            print(f"  → Nova caixa #{self.current_box.number} criada")

        # Adicionar peça à caixa
        self.current_box.add_part(part)

        # Verificar se caixa foi fechada
        if self.current_box.closed:
            print(f"  → Caixa #{self.current_box.number} FECHADA (capacidade máxima atingida)")

    def list_approved_parts(self):
        """Lista todas as peças aprovadas"""
        if not self.approved_parts:
            print("\nNenhuma peça aprovada cadastrada.")
            return

        print(f"\n{'='*80}")
        print(f"PEÇAS APROVADAS ({len(self.approved_parts)} total)")
        print(f"{'='*80}")
        for part in self.approved_parts:
            print(part)

    def list_rejected_parts(self):
        """Lista todas as peças reprovadas"""
        if not self.rejected_parts:
            print("\nNenhuma peça reprovada cadastrada.")
            return

        print(f"\n{'='*80}")
        print(f"PEÇAS REPROVADAS ({len(self.rejected_parts)} total)")
        print(f"{'='*80}")
        for part in self.rejected_parts:
            print(part)

    def remove_part(self, id_peca):
        """Remove uma peça do sistema pelo ID"""
        # Buscar em peças aprovadas
        for i, part in enumerate(self.approved_parts):
            if part.id == id_peca:
                removed_part = self.approved_parts.pop(i)
                # Remover também da caixa
                self._remove_part_from_box(removed_part)
                print(f"\n✓ Peça #{id_peca} (APROVADA) removida com sucesso!")
                return True

        # Buscar em peças reprovadas
        for i, part in enumerate(self.rejected_parts):
            if part.id == id_peca:
                self.rejected_parts.pop(i)
                print(f"\n✓ Peça #{id_peca} (REPROVADA) removida com sucesso!")
                return True

        print(f"\n✗ Peça #{id_peca} não encontrada!")
        return False

    def _remove_part_from_box(self, part):
        """Remove peça de uma caixa"""
        for box in self.boxes:
            if part in box.parts:
                box.parts.remove(part)
                # Se a caixa estava fechada e agora tem espaço, reabrir
                if box.closed and len(box.parts) < Box.MAX_CAPACITY:
                    box.closed = False
                break

    def list_boxes(self):
        """Lista todas as caixas fechadas"""
        closed_boxes = [c for c in self.boxes if c.closed]

        if not closed_boxes:
            print("\nNenhuma caixa fechada ainda.")
            return

        print(f"\n{'='*80}")
        print(f"CAIXAS FECHADAS ({len(closed_boxes)} total)")
        print(f"{'='*80}")
        for box in closed_boxes:
            print(f"\n{box}")
            print("Peças contidas:")
            for part in box.parts:
                print(f"  - ID: {part.id} | Peso: {part.weight}g | Cor: {part.color} | Comp: {part.length}cm")

    def generate_report(self):
        """Gera relatório consolidado do sistema"""
        print(f"\n{'='*80}")
        print("RELATÓRIO FINAL DO SISTEMA DE GESTÃO DE PEÇAS")
        print(f"{'='*80}")

        # Total de peças
        total_parts = len(self.approved_parts) + len(self.rejected_parts)
        print(f"\nTOTAL DE PEÇAS PROCESSADAS: {total_parts}")

        # Peças aprovadas
        print(f"\n✓ PEÇAS APROVADAS: {len(self.approved_parts)}")
        if total_parts > 0:
            approved_percentage = (len(self.approved_parts) / total_parts) * 100
            print(f"  Percentual: {approved_percentage:.2f}%")

        # Peças reprovadas
        print(f"\n✗ PEÇAS REPROVADAS: {len(self.rejected_parts)}")
        if total_parts > 0:
            rejected_percentage = (len(self.rejected_parts) / total_parts) * 100
            print(f"  Percentual: {rejected_percentage:.2f}%")

        # Motivos de reprovação (estatística)
        if self.rejected_parts:
            print("\n  Detalhamento das reprovações:")
            reasons = {}
            for part in self.rejected_parts:
                for motivo in part.rejection_reasons:
                    if "Peso" in motivo:
                        reasons['Peso fora do padrão'] = reasons.get('Peso fora do padrão', 0) + 1
                    elif "Cor" in motivo:
                        reasons['Cor inválida'] = reasons.get('Cor inválida', 0) + 1
                    elif "Comprimento" in motivo:
                        reasons['Comprimento fora do padrão'] = reasons.get('Comprimento fora do padrão', 0) + 1

            for reason, count in reasons.items():
                print(f"    - {reason}: {count} ocorrências")

        # Caixas
        closed_boxes = [c for c in self.boxes if c.closed]
        open_boxes = [c for c in self.boxes if not c.closed]

        print(f"\n📦 CAIXAS UTILIZADAS: {len(self.boxes)}")
        print(f"  - Caixas fechadas: {len(closed_boxes)}")
        print(f"  - Caixas abertas: {len(open_boxes)}")

        if open_boxes:
            for box in open_boxes:
                print(f"    {box}")

        # Eficiência de armazenamento
        if self.boxes:
            total_stored_parts = sum(len(c.parts) for c in self.boxes)
            total_capacity = len(self.boxes) * Box.MAX_CAPACITY
            efficiency = (total_stored_parts / total_capacity) * 100
            print(f"\n  Eficiência de armazenamento: {efficiency:.2f}%")

        print(f"\n{'='*80}")
