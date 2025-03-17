import random

def sorteio_aluno():
    alunos = ["josé", "ana", "pedro",
        "julia", "maria", "fabiana"]
    escolher = random.choice(alunos)
    print(f"o aluno escolhido foi: {escolher}")

sorteio_aluno()