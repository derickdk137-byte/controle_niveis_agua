# 💧 Controle de Níveis de Água

🦆 Programa de monitoramento dos níveis de água de um reservatório pelo terminal, desenvolvido em **Python** com a biblioteca **Colorama**.

## 🎯 Objetivo

Exibir a situação do reservatório com mensagens coloridas, facilitando a identificação de níveis críticos, baixos, médios, altos e muito altos.

## 🚦 Níveis do reservatório

| Nível | Situação | Cor no terminal |
|:---:|---|:---:|
| 1 | 🚨 Muito baixo (crítico) | 🔴 Vermelho |
| 2 | ⚠️ Baixo | 🟡 Amarelo |
| 3 | ✅ Médio | 🟢 Verde |
| 4 | 💧 Alto | Ciano |
| 5 | 🌊 Muito alto (alerta) | 🔵 Azul |

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-2E8B57?style=for-the-badge)

## 📁 Estrutura do projeto

```text
Derick_Prado_Ag11_DS/
├── controle_niveis_agua.py
└── README.md
```

## ⚙️ Funcionamento

O programa armazena as cinco situações do reservatório em uma **lista**, organizada do nível mais baixo ao mais alto.

A função **`definir_cor()`** recebe o número do nível e utiliza as estruturas condicionais **`if`** e **`elif`** para retornar a cor correspondente.

Um laço **`for`** percorre os cinco níveis. Em cada etapa, o programa consulta a situação na lista e exibe uma mensagem colorida utilizando **`print()`** e **f-strings**.

Após cada mensagem, **`Style.RESET_ALL`** restaura o estilo padrão do terminal.

> 💡 Os níveis são definidos no código, sem necessidade de entrada de dados durante a execução.

## 🚀 Como executar

### 1️⃣ Criar e ativar o ambiente virtual

Com o Python 3 instalado, abra o terminal na pasta do projeto e execute:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2️⃣ Instalar a biblioteca Colorama

```bash
python -m pip install colorama
```

### 3️⃣ Executar o programa

```bash
python controle_niveis_agua.py
```

> 💡 Ao abrir um novo terminal, ative novamente o ambiente virtual antes de executar o programa.

## 🖥️ Exemplo de saída

```text
Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)
```

Cada mensagem é exibida no terminal com a cor indicada na tabela de níveis.

## 🧪 Como testar

1. Execute o arquivo `controle_niveis_agua.py`.
2. Verifique se aparecem as cinco mensagens na ordem correta.
3. Confira se as cores correspondem às situações da tabela.
4. Após a execução, digite:

```bash
echo "Teste de cor padrão"
```

✅ O texto deve aparecer na cor padrão do terminal, confirmando a restauração do estilo.

## 📚 Conceitos aplicados

- **Listas:** armazenamento das situações do reservatório.
- **Bibliotecas:** utilização dos recursos da Colorama.
- **Funções:** organização da lógica de escolha das cores.
- **Condicionais:** associação de cada nível à sua cor.
- **Laços de repetição:** apresentação dos cinco níveis.
- **Variáveis:** armazenamento dos valores utilizados.
- **Índices:** acesso às situações armazenadas na lista.
- **F-strings:** formatação das mensagens exibidas.

## 🎓 Contexto acadêmico

Atividade do curso de **Desenvolvimento de Sistemas — ETEC**, voltada à aplicação de listas, funções, estruturas condicionais, repetição e bibliotecas em Python.

## 👨‍💻 Autor

**Derick Prado**
