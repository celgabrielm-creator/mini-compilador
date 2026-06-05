from exceptions import (
    SyntaxCompilerError,
    SemanticError
)


class Parser:

    def __init__(self, tokens, source_code):

        self.tokens = tokens
        self.source_lines = source_code.splitlines()

        self.pos = 0
        self.output = []
        self.symbols = {}

    def current(self):

        if self.pos < len(self.tokens):
            return self.tokens[self.pos]

        return None

    def error(self, token, message):

        line = token[2] if token else "EOF"

        source = ""

        if token and line - 1 < len(self.source_lines):
            source = self.source_lines[line - 1]

        raise SyntaxCompilerError(
            f"""
ERRO SINTÁTICO

Linha: {line}

Código:
{source}

Descrição:
{message}
"""
        )

    def eat(self, expected):

        token = self.current()

        if token and token[0] == expected:
            self.pos += 1
            return token

        self.error(
            token,
            f"Esperado '{expected}'"
        )

    def parse(self):

        while self.current():
            self.statement()

        return self.output

    def statement(self):

        variable = self.eat("ID")[1]

        self.eat("EQUAL")

        self.symbols[variable] = True

        expr = self.expr()

        self.eat("SEMICOLON")

        self.output.append(
            f"{variable} = {expr}"
        )

    def expr(self):

        result = self.term()

        while self.current() and self.current()[0] == "PLUS":

            self.eat("PLUS")

            if (
                self.current() is None or
                self.current()[0] == "SEMICOLON"
            ):

                self.error(
                    self.current(),
                    "Expressão incompleta após operador '+'"
                )

            result += " + " + self.term()

        return result

    def term(self):

        token = self.current()

        if token is None:

            self.error(
                token,
                "Fim inesperado do arquivo"
            )

        if token[0] == "NUMBER":
            return self.eat("NUMBER")[1]

        if token[0] == "ID":

            name = token[1]

            if name not in self.symbols:

                raise SemanticError(
                    f"""
ERRO SEMÂNTICO

Linha: {token[2]}

Código:
{self.source_lines[token[2]-1]}

Descrição:
Variável '{name}' não declarada.
"""
                )

            return self.eat("ID")[1]

        self.error(
            token,
            "Esperado NUMBER ou ID"
        )