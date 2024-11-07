from database import Database
from livro import Livro

class ControllerLivro:
    def cadastrarLivro(self):
        bd = Database("localhost", "root", "", "biblioteca")
        bd.conectar()

        livro = livro("Dom Casmurro", "Machado de Assis", "Suspense",123)
        bd.cursor.execute(livro.create())
        bd.conexao.commit()
        bd.desconectar()

        def procurarLivro(self):
            bd = Database("localhost", "root")

        def atualizarLivro(self):
            pass
        def excluirLivro(self):
            pass

