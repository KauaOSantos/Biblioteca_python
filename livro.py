class Livro():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro

        self.status = "Disponível"

        def create():
            return 'INSERT INTO livro (titulo, autor, genero, cod_livro) VALUES("{self.titulo}","{self.autor}","{self.genero}","{self.cod_livro}");'
        
        def read():
            return 'SELECT * FROM livro where cod_livro = {self.cod_livro};'
        
        def update():
            return 'UPDATE livro SET titulo = "{self.titulo}", autor = "{self.autor}", genero = "{self.genero}" WHERE cod_livro = {self.cod_livro};'
        
        def deletar():
            return 'DELETE FROM livro where cod_livro = {self.cod_livro};' 