import CalcNota
from Aluno import Aluno

def main():
    aluno = Aluno()

    while True:
        print("1 - Adicionar aluno")
        print("2 - Listar aluno")
        print("4 - Remover aluno")
        print("0 - Sair")

        op = int(input("Escolha uma opção: "))

        if op == 1:
            nome = input("Escreva o nome do Aluno: ")
            nota1 = float(input("Escreva a primeira nota: "))
            nota2 = float(input("Escreva a segunda nota: "))
            nota3 = float(input("Escreva a terceira nota: "))
            aluno.AdicionarAluno(nome, nota1, nota2, nota3)
            print("Aluno adicionado com sucesso")

        elif op == 2:
            aluno.ListarAlunos()

        elif op == 4:
            nome = input("Escreva o nome do Aluno que deseja remover: ")
            aluno.DeletarAluno(nome)
            print("Aluno removido com sucesso")

        elif op == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida")
            break

if __name__ == '__main__':
    main()
