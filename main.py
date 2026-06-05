from compiler import compile_code
from exceptions import (
    LexicalError,
    SemanticError,
    SyntaxCompilerError
)

codigo = """
x = 10;
y = x + 5;
z = y + 20;
"""

try:

    compiled, tokens = compile_code(codigo)

    print("\nTOKENS:\n")

    for token in tokens:
        print(token)

    print("\nCÓDIGO COMPILADO:\n")

    for line in compiled:
        print(line)

    print("\n✅ Compilação concluída com sucesso!")

except (
    LexicalError,
    SyntaxCompilerError,
    SemanticError
) as error:

    print(error)