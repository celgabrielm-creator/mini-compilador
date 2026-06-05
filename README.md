# Mini Compiler

## 📖 Sobre o Projeto

O Mini Compiler é um compilador simplificado desenvolvido em Python com fins acadêmicos para demonstrar os principais conceitos da construção de compiladores.

O projeto implementa as etapas fundamentais de compilação:

* Análise Léxica
* Análise Sintática
* Análise Semântica
* Geração de Código Intermediário
* Tratamento de Erros

Seu objetivo é servir como ferramenta de aprendizado para disciplinas relacionadas à Linguagens Formais, Compiladores e Estruturas de Linguagens de Programação.

---

# 🚀 Funcionalidades

### Análise Léxica

Responsável por transformar o código-fonte em uma sequência de tokens.

Exemplo:

Entrada:

```txt
x = 10;
```

Saída:

```txt
(ID, x)
(EQUAL, =)
(NUMBER, 10)
(SEMICOLON, ;)
```

---

### Análise Sintática

Verifica se o código segue a gramática definida para a linguagem.

Exemplo:

```txt
x = 10;
y = x + 5;
```

---

### Análise Semântica

Valida regras semânticas da linguagem.

Exemplos de validação:

* Variáveis declaradas antes do uso
* Estruturas válidas de atribuição
* Consistência dos identificadores

---

### Tratamento de Erros

O compilador possui tratamento para:

#### Erros Léxicos

```txt
x = 10 @
```

#### Erros Sintáticos

```txt
x = ;
```

```txt
y = x + ;
```

#### Erros Semânticos

```txt
x = y + 5;
```

Quando a variável `y` não foi declarada.

---

# 🏗 Arquitetura do Projeto

```text
mini_compiler/
│
├── main.py
├── compiler.py
├── lexer.py
├── parser.py
├── exceptions.py
├── README.md
└── .gitignore
```

## Responsabilidades

### main.py

Ponto de entrada da aplicação.

Responsável por:

* Receber o código-fonte
* Executar o compilador
* Exibir resultados e mensagens de erro

---

### lexer.py

Implementa o analisador léxico.

Responsável por:

* Identificar tokens
* Ignorar espaços e quebras de linha
* Detectar caracteres inválidos

---

### parser.py

Implementa:

* Análise sintática
* Análise semântica
* Tabela de símbolos

---

### compiler.py

Coordena as etapas do processo de compilação.

Fluxo:

```text
Código Fonte
      ↓
Análise Léxica
      ↓
Análise Sintática
      ↓
Análise Semântica
      ↓
Código Intermediário
```

---

### exceptions.py

Centraliza todas as exceções do compilador.

Classes:

```python
CompilerError
LexicalError
SyntaxCompilerError
SemanticError
```

---

# 📚 Definição da Linguagem

A linguagem implementada suporta:

### Atribuição

```txt
x = 10;
```

### Soma

```txt
y = x + 5;
```

### Referência entre variáveis

```txt
total = valor + imposto;
```

---

# 📝 Gramática

Representação simplificada da gramática:

```bnf
program     ::= statement*

statement   ::= ID "=" expr ";"

expr        ::= term
              | expr "+" term

term        ::= NUMBER
              | ID
```

---

# 🔍 Exemplos

## Exemplo Válido

Entrada:

```txt
x = 10;
y = x + 5;
z = y + 20;
```

Saída:

```txt
x = 10
y = x + 5
z = y + 20
```

---

## Exemplo com Erro Léxico

Entrada:

```txt
x = 10 @
```

Saída:

```txt
ERRO LÉXICO
Caractere inválido '@'
```

---

## Exemplo com Erro Sintático

Entrada:

```txt
x = 10;
y = x + ;
```

Saída:

```txt
ERRO SINTÁTICO
Expressão incompleta
```

---

## Exemplo com Erro Semântico

Entrada:

```txt
x = y + 10;
```

Saída:

```txt
ERRO SEMÂNTICO
Variável 'y' não declarada
```

---

# ⚙️ Como Executar

## Pré-requisitos

* Python 3.10 ou superior

Verificar instalação:

```bash
python --version
```

---

## Executar o Projeto

```bash
python main.py
```

---

# 🎯 Conceitos Demonstrados

Este projeto demonstra os seguintes conceitos:

* Compiladores
* Linguagens Formais
* Expressões Regulares
* Parsing
* Gramáticas Livres de Contexto
* Tabela de Símbolos
* Tratamento de Erros
* Estruturas de Dados
* Programação Orientada a Objetos

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos e educacionais.

---

# 👨‍💻 Autor

Celso Gabriel Monteiro

Projeto desenvolvido como estudo dos fundamentos de compiladores utilizando Python.
