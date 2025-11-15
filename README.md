# Sistema de Gestão de Peças Industrial

## Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

### Descrição do Projeto

Este projeto é uma solução de automação digital desenvolvida em Python para auxiliar no controle de produção e qualidade de peças fabricadas em linhas de montagem industriais. O sistema automatiza o processo de inspeção que anteriormente era feito manualmente, eliminando atrasos, reduzindo falhas de conferência e diminuindo custos operacionais.

### Funcionalidades

O sistema oferece as seguintes funcionalidades através de um menu interativo:

1. **Cadastrar nova peça**: Registro de peças com validação automática de qualidade
2. **Listar peças aprovadas/reprovadas**: Visualização organizada das peças por status
3. **Remover peça cadastrada**: Remoção de peças do sistema por ID
4. **Listar caixas fechadas**: Visualização das caixas completas e suas peças
5. **Gerar relatório final**: Relatório consolidado com estatísticas completas

### Critérios de Qualidade

O sistema avalia automaticamente cada peça com base nos seguintes critérios:

- **Peso**: Entre 95g e 105g
- **Cor**: Azul ou Verde
- **Comprimento**: Entre 10cm e 20cm

Peças que não atendem a todos os critérios são automaticamente reprovadas com indicação dos motivos específicos.

### Sistema de Armazenamento

- Peças aprovadas são automaticamente armazenadas em caixas
- Capacidade de cada caixa: **10 peças**
- Quando uma caixa atinge a capacidade máxima, é automaticamente fechada
- Uma nova caixa é iniciada automaticamente quando necessário

### Estrutura do Projeto

```
industrial-parts-management/
│
├── part.py                 # Classe Part (peça)
├── box.py                  # Classe Box (caixa)
├── management_system.py    # Classe ManagementSystem (sistema de gestão)
├── main.py                 # Programa principal com menu
├── README.md              # Este arquivo
└── requirements.txt       # Dependências (vazio - Python puro)
```

### Como Executar o Programa

#### Pré-requisitos

- Python 3.6 ou superior instalado no sistema
- Sistema operacional: Windows, Linux ou macOS

#### Verificar instalação do Python

```bash
python --version
# ou
python3 --version
```

#### Passo a Passo para Executar

1. **Clone o projeto**
   ```bash
   git clone https://github.com/RenatoRJF/industrial-parts-management.git
   cd industrial-parts-management
   ```

2. **Execute o programa**
   ```bash
   python3 main.py
   ```

3. **Interaja com o menu**
   - Digite o número da opção desejada
   - Siga as instruções na tela
   - Para sair, digite `0`

### Exemplos de Uso

#### Exemplo 1: Cadastrar peça aprovada

```
Escolha uma opção: 1

--- CADASTRO DE NOVA PEÇA ---
Digite o peso (g): 100
Digite a cor: azul
Digite o comprimento (cm): 15

✓ Peça #1 APROVADA e armazenada com sucesso!
  → Nova caixa #1 criada
```

#### Exemplo 2: Cadastrar peça reprovada

```
Escolha uma opção: 1

--- CADASTRO DE NOVA PEÇA ---
Digite o peso (g): 110
Digite a cor: vermelho
Digite o comprimento (cm): 25

✗ Peça #2 REPROVADA!
  Motivos: Peso fora do padrão: 110.0g (esperado: 95g-105g); Cor inválida: vermelho (esperado: azul ou verde); Comprimento fora do padrão: 25.0cm (esperado: 10cm-20cm)
```

#### Exemplo 3: Relatório final

```
Escolha uma opção: 5

================================================================================
RELATÓRIO FINAL DO SISTEMA DE GESTÃO DE PEÇAS
================================================================================

TOTAL DE PEÇAS PROCESSADAS: 15

✓ PEÇAS APROVADAS: 10
  Percentual: 66.67%

✗ PEÇAS REPROVADAS: 5
  Percentual: 33.33%

  Detalhamento das reprovações:
    - Peso fora do padrão: 3 ocorrências
    - Cor inválida: 4 ocorrências
    - Comprimento fora do padrão: 2 ocorrências

📦 CAIXAS UTILIZADAS: 2
  - Caixas fechadas: 1
  - Caixas abertas: 1

  Eficiência de armazenamento: 50.00%

================================================================================
```

### Estrutura do Código

#### Classes Principais

**1. Classe `Part`** (part.py)
- Representa uma peça produzida
- Atributos: id, weight, color, length, approved, rejection_reasons
- Método `_validate_quality()`: Valida automaticamente os critérios de qualidade

**2. Classe `Box`** (box.py)
- Representa uma caixa de armazenamento
- Capacidade máxima: 10 peças
- Método `add_part()`: Adiciona peça e fecha caixa se atingir capacidade
- Método `close()`: Marca a caixa como fechada

**3. Classe `ManagementSystem`** (management_system.py)
- Sistema principal que gerencia peças e caixas
- Métodos principais:
  - `register_part()`: Cadastra e valida nova peça
  - `list_approved_parts()`: Lista peças aprovadas
  - `list_rejected_parts()`: Lista peças reprovadas
  - `remove_part()`: Remove peça por ID
  - `list_boxes()`: Lista caixas fechadas
  - `generate_report()`: Gera relatório consolidado

### Técnicas e Boas Práticas Aplicadas

1. **Programação Orientada a Objetos (POO)**
   - Encapsulamento de dados e comportamentos
   - Separação de responsabilidades entre classes
   - Métodos privados (prefixo `_`) para operações internas

2. **Separação de Módulos**
   - Cada classe em seu próprio arquivo
   - Importações claras e organizadas
   - Facilita manutenção e testes

3. **Validação de Dados**
   - Validação automática de qualidade das peças
   - Tratamento de entradas do usuário
   - Validação de intervalos numéricos

4. **Tratamento de Erros**
   - Try-except para capturar erros
   - Validação de entrada numérica
   - Mensagens de erro claras e descritivas

5. **Interface Amigável**
   - Menu interativo claro e organizado
   - Feedback visual com símbolos (✓, ✗, →, 📦)
   - Formatação consistente com separadores visuais

6. **Código Limpo**
   - Docstrings em todas as classes e funções
   - Nomes descritivos de variáveis e métodos em inglês
   - Interface do usuário em português
   - Formatação consistente

### Benefícios da Solução

- **Automação Completa**: Elimina inspeção manual de peças
- **Redução de Erros**: Validação automática e consistente
- **Rastreabilidade**: Cada peça tem um ID único
- **Relatórios Detalhados**: Estatísticas completas sobre produção e qualidade
- **Eficiência**: Armazenamento automático em caixas
- **Código Modular**: Fácil de manter e expandir

### Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Paradigma**: Programação Orientada a Objetos
- **Dependências**: Nenhuma (usa apenas bibliotecas padrão do Python)

### Autor

Projeto desenvolvido para a disciplina de **Algoritmos e Lógica de Programação** - UNIFECAF

---

**Importante**: Este é um protótipo educacional desenvolvido para demonstrar conceitos de programação e lógica aplicados a um cenário industrial real.
