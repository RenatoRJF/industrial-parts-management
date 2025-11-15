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
gestao-pecas-industrial/
│
├── main.py                 # Código principal do sistema
├── README.md              # Este arquivo
├── requirements.txt       # Dependências do projeto (vazio - Python puro)
└── examples.md            # Exemplos de uso
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

1. **Clone ou baixe o projeto**
   ```bash
   cd gestao-pecas-industrial
   ```

2. **Execute o programa**
   ```bash
   python main.py
   # ou, dependendo da configuração do seu sistema:
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

#### Exemplo 3: Listar peças aprovadas

```
Escolha uma opção: 2
--- LISTAGEM DE PEÇAS ---

1. Listar peças aprovadas
2. Listar peças reprovadas
3. Listar ambas

Escolha uma opção: 1

================================================================================
PEÇAS APROVADAS (5 total)
================================================================================
ID: 1 | Peso: 100.0g | Cor: azul | Comprimento: 15.0cm | Status: APROVADA
ID: 3 | Peso: 98.0g | Cor: verde | Comprimento: 12.0cm | Status: APROVADA
ID: 4 | Peso: 102.0g | Cor: azul | Comprimento: 18.0cm | Status: APROVADA
ID: 6 | Peso: 95.0g | Cor: verde | Comprimento: 10.0cm | Status: APROVADA
ID: 7 | Peso: 105.0g | Cor: azul | Comprimento: 20.0cm | Status: APROVADA
```

#### Exemplo 4: Caixa fechada automaticamente

```
Após cadastrar 10 peças aprovadas:

✓ Peça #10 APROVADA e armazenada com sucesso!
  → Caixa #1 FECHADA (capacidade máxima atingida)

✓ Peça #11 APROVADA e armazenada com sucesso!
  → Nova caixa #2 criada
```

#### Exemplo 5: Relatório final

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
    Caixa #2 - ABERTA - Peças: 0/10

  Eficiência de armazenamento: 50.00%

================================================================================
```

### Estrutura do Código

#### Classes Principais

**1. Classe `Peca`**
- Representa uma peça produzida
- Atributos: id, peso, cor, comprimento, aprovada, motivos_reprovacao
- Método `_validar_qualidade()`: Valida automaticamente os critérios de qualidade

**2. Classe `Caixa`**
- Representa uma caixa de armazenamento
- Capacidade máxima: 10 peças
- Método `adicionar_peca()`: Adiciona peça e fecha caixa se atingir capacidade
- Método `fechar()`: Marca a caixa como fechada

**3. Classe `SistemaGestao`**
- Sistema principal que gerencia peças e caixas
- Métodos principais:
  - `cadastrar_peca()`: Cadastra e valida nova peça
  - `listar_pecas_aprovadas()`: Lista peças aprovadas
  - `listar_pecas_reprovadas()`: Lista peças reprovadas
  - `remover_peca()`: Remove peça por ID
  - `listar_caixas()`: Lista caixas fechadas
  - `gerar_relatorio()`: Gera relatório consolidado

### Técnicas e Boas Práticas Aplicadas

1. **Programação Orientada a Objetos (POO)**
   - Encapsulamento de dados e comportamentos
   - Separação de responsabilidades entre classes
   - Métodos privados (prefixo `_`) para operações internas

2. **Validação de Dados**
   - Validação automática de qualidade das peças
   - Tratamento de entradas do usuário
   - Validação de intervalos numéricos

3. **Tratamento de Erros**
   - Try-except para capturar erros
   - Validação de entrada numérica
   - Mensagens de erro claras e descritivas

4. **Interface Amigável**
   - Menu interativo claro e organizado
   - Feedback visual com símbolos (✓, ✗, →, 📦)
   - Formatação consistente com separadores visuais

5. **Código Limpo**
   - Docstrings em todas as classes e funções
   - Nomes descritivos de variáveis e métodos
   - Comentários explicativos quando necessário
   - Formatação consistente

6. **Estruturas de Dados**
   - Listas para armazenamento dinâmico
   - Dicionários para contagem de motivos de reprovação
   - Uso eficiente de estruturas Python

7. **Modularização**
   - Funções específicas para cada operação
   - Reutilização de código
   - Facilidade de manutenção e expansão

### Benefícios da Solução

- **Automação Completa**: Elimina inspeção manual de peças
- **Redução de Erros**: Validação automática e consistente
- **Rastreabilidade**: Cada peça tem um ID único
- **Relatórios Detalhados**: Estatísticas completas sobre produção e qualidade
- **Eficiência**: Armazenamento automático em caixas
- **Escalabilidade**: Fácil de expandir com novas funcionalidades

### Possíveis Expansões Futuras

Este protótipo pode ser expandido para um cenário industrial real com:

1. **Integração com Sensores IoT**
   - Leitura automática de peso, cor e comprimento via sensores
   - Conexão com balanças digitais
   - Câmeras para reconhecimento de cor
   - Sensores laser para medição de comprimento

2. **Banco de Dados**
   - Persistência de dados em PostgreSQL ou MongoDB
   - Histórico completo de produção
   - Consultas avançadas e análises

3. **Interface Web**
   - Dashboard com gráficos em tempo real
   - Interface responsiva usando Flask ou Django
   - Visualização de métricas de produção

4. **Inteligência Artificial**
   - Machine Learning para prever falhas de qualidade
   - Análise preditiva de tendências de produção
   - Otimização automática de parâmetros

5. **Integração Industrial**
   - Conexão com sistemas MES (Manufacturing Execution System)
   - Comunicação com CLPs (Controladores Lógicos Programáveis)
   - Protocolo OPC UA para comunicação industrial

6. **Relatórios Avançados**
   - Exportação para PDF e Excel
   - Gráficos de tendências
   - Análise de Pareto de defeitos

7. **Notificações**
   - Alertas automáticos por email ou SMS
   - Notificações quando caixas são fechadas
   - Avisos de taxa alta de reprovação

8. **Múltiplos Usuários**
   - Sistema de autenticação
   - Controle de permissões por função
   - Auditoria de operações

### Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Paradigma**: Programação Orientada a Objetos
- **Bibliotecas**: Apenas bibliotecas padrão do Python (sem dependências externas)

### Autor

Projeto desenvolvido para a disciplina de **Algoritmos e Lógica de Programação** - UNIFECAF

### Licença

Este projeto é de uso educacional.

---

**Importante**: Este é um protótipo educacional desenvolvido para demonstrar conceitos de programação e lógica aplicados a um cenário industrial real.
