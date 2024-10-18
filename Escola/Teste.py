from tkinter import *
import CalcNota
#from Escola import Escola
#from Turma import Turma
from Aluno import Aluno
from BancoDados import BancoDados

def main():
    aluno = Aluno()
    #Isso é do dislay, o que vai aparecer na tela. Estou arrumando isso.
    display = Tk()

    largura_tela = display.winfo_screenwidth()
    altura_tela = display.winfo_screenheight()

    largura_janela = 700
    altura_janela = 500

    x = (largura_tela - largura_janela) / 2
    y = (altura_tela - altura_janela) / 2

    display.geometry(f"{largura_janela}x{altura_janela}+{int(x)}+{int(y)}")
    display.title("Gerenciador de tarefas")



    display.mainloop()  
    
"""
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
"""
if __name__ == '__main__':
    main()
