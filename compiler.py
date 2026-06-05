from lexer import lexer
from parser import Parser


def compile_code(code):

    tokens = lexer(code)

    parser = Parser(tokens, code)

    return parser.parse(), tokens