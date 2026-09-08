# Gerador_Calendario
Script em Python que gera e exibe o calendário visual de qualquer mês e ano fornecidos pelo usuário via terminal, utilizando a biblioteca nativa calendar e validação de dados.

# Projeto
# 📅 Gerador de Calendário em Python

Um utilitário simples em Python que gera o calendário visual de qualquer mês e ano fornecidos pelo usuário, utilizando a biblioteca nativa `calendar`.

##  Funcionalidades

- Entrada interativa via terminal.
- Validação de dados (garante que o mês inserido esteja entre 1 e 12).
- Exibição limpa do calendário no terminal.

##  Tecnologias Utilizadas

- **Python 3** (módulo nativo `calendar`)

##  Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/KAUAN-KAWASAKI/Gerador_Calendario.git](https://github.com/KAUAN-KAWASAKI/Gerador_Calendario.git)
---

### 3. Melhoria Opcional no Código (Loop para Repetição)

Se quiser deixar a experiência do usuário ainda melhor no terminal, você pode adicionar um loop `while` para permitir que a pessoa consulte vários meses sem precisar reexecutar o programa toda hora:

```python
import calendar

def gerar_calendario_mes():
    print("=" * 30)
    print("📅 GERADOR DE CALENDÁRIO 📅")
    print("=" * 30)

    try:
        mes = int(input("\nDigite o número do mês (1-12): "))
        ano = int(input("Digite o ano: "))

        if mes < 1 or mes > 12:
            print("❌ Mês inválido! Insira um número entre 1 e 12.")
        else:
            print("\n" + calendar.month(ano, mes))
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números inteiros.")

def main():
    while True:
        gerar_calendario_mes()
        continuar = input("Deseja consultar outro mês? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nAté logo! 👋")
            break

if __name__ == "__main__":
    main()
