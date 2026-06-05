class CompilerError(Exception):
    pass


class LexicalError(CompilerError):
    pass


class SyntaxCompilerError(CompilerError):
    pass


class SemanticError(CompilerError):
    pass