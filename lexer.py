import re
from exceptions import LexicalError

TOKENS = [
    ('NUMBER', r'\d+'),
    ('ID', r'[a-zA-Z_]\w*'),
    ('PLUS', r'\+'),
    ('EQUAL', r'='),
    ('SEMICOLON', r';'),
    ('SKIP', r'[ \t]+'),
    ('NEWLINE', r'\n'),
    ('MISMATCH', r'.')
]


def lexer(code):

    tokens = []
    line = 1

    regex = '|'.join(
        f'(?P<{name}>{pattern})'
        for name, pattern in TOKENS
    )

    for match in re.finditer(regex, code):

        kind = match.lastgroup
        value = match.group()

        if kind == 'NEWLINE':
            line += 1

        elif kind == 'SKIP':
            continue

        elif kind == 'MISMATCH':

            raise LexicalError(
                f"\nERRO LÉXICO\nLinha {line}\nCaractere inválido: '{value}'"
            )

        else:
            tokens.append((kind, value, line))

    return tokens