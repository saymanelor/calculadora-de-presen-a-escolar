#calculo da frequencia escolar

print("\nbem vindo à ferramenta de calculo de porcentagem do sistema PRESENÇA")


dias_letivos = int(input("quantos dias letivos teve no mês de referencia ?\n"))
#formula do calculo :
def calculo(dias_frequentados,dias_letivos):
    resultado = (dias_frequentados * 100) / dias_letivos
    print(f"a porcentagem da presença do aluno(a) é de {resultado:.0f}%")
    return resultado

def justificativa(idade,calculo):
    if idade <= 6 and chamada < 60:
        print("necessita de justificativa")
    elif 6 < idade <= 18 and chamada < 75:
        print("necessita de justificativa")
    else:
        print("não precisa de justificativa")

#laço da repetição
concluido = False
while not concluido:
    idade = int(input("quantos anos tem o aluno ? \n"))
    dias_frequentados = int(input("quantos dias o aluno(a) frequentou ?\n"))
    chamada = calculo(dias_frequentados=dias_frequentados,dias_letivos=dias_letivos)
    justificativa(idade,calculo)
    resposta = input("deseja calcular mais ? se sim, digite 'sim' se não, digite 'nao'\n ").lower()
    if resposta == "nao":
        concluido = True
    elif resposta == "sim":
        concluido = False
        alterar_dia_letivo = input("deseja alterar os dias letivos? \n").lower()
        if alterar_dia_letivo == "sim":
            dias_letivos = int(input("quantos dias letivos tem no mês de referencia \n"))
        elif alterar_dia_letivo != "sim":
            continue