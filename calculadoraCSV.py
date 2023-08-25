import tkinter as tk
import csv
#---------------------- Definição das funções ------------------------------


def contar_linhas():
    arquivo = entrada_arquivo.get()
    contador = 0

    with open(arquivo, 'r') as arquivo_csv:
        dados_csv = csv.reader(arquivo_csv)
        for dado in dados_csv:
            contador += 1

    #contador - 1 para desconsiderar os cabeçalhos
    resultado_label.configure(text=f"O arquivo tem {contador - 1} linhas.")



def listar_colunas():
    arquivo = entrada_arquivo.get()

    with open(arquivo, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        colunas = next(csv_reader)
        quantidade_colunas = len(colunas)
        nomes_colunas = ', '.join(colunas)

        resultado_label.configure(text=f"O arquivo tem {quantidade_colunas} colunas.\nNomes das colunas: {nomes_colunas}")





#---------------------------------------------------------------------------

# Criar janela
janela = tk.Tk()
janela.title("Análise de CSV")
janela.geometry("600x650")
janela.minsize(600,650)


label_titulo_principal = tk.Label(text="Análise de arquivos CSV", 
                                  font= ('Helvetica', 15, "bold"))
label_titulo_principal.pack(pady=10)

label_caminho = tk.Label(text="Caminho do arquivo",
                         font= ('Segoe UI', 10))
label_caminho.pack()

# Criar campo de entrada para o caminho do arquivo
entrada_arquivo = tk.Entry(janela, width=80, font= ('Segoe UI', 10))
entrada_arquivo.pack()

# Criar botão para contar linhas
botao_linhas = tk.Button(janela,
                        text="Contar Linhas",
                        font= ('arial', 12, "bold"),
                        bg ="#D9501E",
                        command=contar_linhas)
botao_linhas.pack(pady=10)

# Criar botão para listar colunas
botao_colunas = tk.Button(janela, text="Listar Colunas",
                        font= ('arial', 12, "bold"),
                        bg ="#DB691A",
                        command=listar_colunas)
botao_colunas.pack(pady=10 )

label_coluna= tk.Label(text="Nome da coluna",  font= ('Segoe UI', 10))
label_coluna.pack(pady=10)

# Criar entrada para obter nome da coluna
entrada_coluna = tk.Entry(janela,
                          font= ('Segoe UI', 10),
                          width=80)
entrada_coluna.pack(pady=10)

# Criar botão maximo, mínimo e média
botao_maximo = tk.Button(janela,
                        text="Exibir valor máximo",
                        font= ('arial', 12, "bold"),
                        bg ="#D98F07",
                        command= exibir_maximo_coluna)
botao_maximo.pack(pady=10)

botao_minimo = tk.Button(janela,
                        text="Exibir valor mínimo",
                        font= ('arial', 12, "bold"),
                        bg ="#D9A407",
                        command= exibir_minimo_coluna)
botao_minimo.pack(pady=10)

botao_media = tk.Button(janela,
                        text="Exibir média ",
                        font= ('arial', 12, "bold"),
                        bg ="#F2CB07",
                        command= exibir_media_coluna)
botao_media.pack(pady=10)

# Criar rótulo para exibir o resultado
resultado_label = tk.Label(janela,
                           text="",
                           font= ('Segoe UI', 10))
resultado_label.pack()

# Iniciar loop principal da janela
janela.mainloop()
