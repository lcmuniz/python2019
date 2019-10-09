class Disciplina:
    codigo = None
    nome = None


class Pessoa:
    nome = None
    data_de_nascimento = None

class Professor(Pessoa):
    titulacao = None

class Aluno(Pessoa):
    matricula = None

class Turma:
    codigo = None
    data_de_inicio = None
    data_de_fim = None
    disciplina = None
    professor = None
    alunos = None

