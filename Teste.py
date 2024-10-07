import CalcNota
from Aluno import Aluno
from BancoDados import BancoDados

def main():
    aluno = Aluno()

    while True:
        print("1 - Adicionar aluno")
        print("2 - Listar aluno")
        print("3 - Remover aluno")
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
            alunos = aluno.ListarAlunos()
            if alunos:
                print("Lista de alunos:")
                for aluno_data in alunos:
                    print("Nome: {}, Média: {:.2f}, Situação: {}".format(
                        aluno_data[1], float(aluno_data[2]), aluno_data[3]
                    ))
            else:
                print("Nenhum aluno encontrado")
        elif op == 3:
            nome = input("Escreva o nome do aluno que deseja remover: ")
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
