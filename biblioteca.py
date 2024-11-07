from livro import Livro 
from usuario import Usuario

class Biblioteca:
    acervo:list[Livro] = []

    @staticmethod
    def emprestar (usuario: Usuario, Livro: list[Livro]):

        for item in Livro:
            if len (usuario.Livro) == usuario.MAX_EMPRESTIMO:
                return
            usuario.pegar_emprestado(item)
            item.emprestar_livro(usuario)