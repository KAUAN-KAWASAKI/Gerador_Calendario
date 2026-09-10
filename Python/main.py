# Gerador de Calendário em Python

# Biblioteca calendar do Python
import calendar

# Função para gerar o calendário de um mês específico
def gerar_calendario_mes():
    print("📅 GERADOR DE CALENDÁRIO 📅")

    mes = int(input("Digite o Número do mês (1-12): "))
    ano = int(input("Digite o Ano: "))

    if mes < 1 or mes > 12:
        print("❌ Mês inválido! Por favor, insira um número entre 1 e 12.")
    else:
        # Gerando o calendário do mês e ano especificados
        print("\n📅 SEU CALENDÁRIO:\n")
        calendario = calendar.month(ano, mes)
        print(calendario)

# Função principal
def main():
    gerar_calendario_mes()

if __name__ == "__main__":
    main()