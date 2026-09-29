import math

def exibir_menu():
    print("=" * 60)
    print("      CALCULADORA DE LADO DE POLÍGONOS REGULARES")
    print("=" * 60)
    print("Escolha qual dado de entrada você possui:")
    print("1. Apótema (a)")
    print("2. Raio da circunferência circunscrita (R)")
    print("3. Raio da circunferência inscrita (r)")
    print("4. Diagonal que passa pelo centro (d) [Apenas para n par]")
    print("5. Altura do polígono (h)")
    print("6. Perímetro (P)")
    print("7. Área total (A)")
    print("8. Ângulo Interno (Ai) ou Ângulo Externo (Ae)")
    print("=" * 60)

def calcular_lado():
    try:
        n = int(input("Informe o número de lados do polígono (n >= 3): "))
        if n < 3:
            print("Erro: Um polígono precisa ter pelo menos 3 lados.")
            return

        exibir_menu()
        opcao = int(input("Digite a opção desejada (1-8): "))

        # Ângulo central sustentado por meio lado (theta = pi / n)
        theta = math.pi / n

        lado = None

        if opcao == 1:
            a = float(input("Digite o valor do apótema (a): "))
            # L = 2 * a * tan(pi / n)
            lado = 2 * a * math.tan(theta)

        elif opcao == 2:
            r_circ = float(input("Digite o raio da circunferência circunscrita (R): "))
            # L = 2 * R * sin(pi / n)
            lado = 2 * r_circ * math.sin(theta)

        elif opcao == 3:
            r_in = float(input("Digite o raio da circunferência inscrita (r): "))
            # O raio da circunferência inscrita é o próprio apótema
            # L = 2 * r * tan(pi / n)
            lado = 2 * r_in * math.tan(theta)

        elif opcao == 4:
            if n % 2 != 0:
                print("\nErro: A diagonal que passa pelo centro só existe em polígonos com número PAR de lados.")
                return
            d = float(input("Digite o valor da diagonal principal (passa pelo centro): "))
            # A diagonal principal é o diâmetro da circunferência circunscrita (d = 2R)
            # L = d * sin(pi / n)
            lado = d * math.sin(theta)

        elif opcao == 5:
            h = float(input("Digite a altura do polígono (h): "))
            if n % 2 == 0:
                # Para n par: h = 2 * apótema  =>  a = h / 2
                a = h / 2
                lado = 2 * a * math.tan(theta)
            else:
                # Para n ímpar: h = a * (1 + 1 / cos(pi/n))
                a = h / (1 + (1 / math.cos(theta)))
                lado = 2 * a * math.tan(theta)

        elif opcao == 6:
            p = float(input("Digite o perímetro (P): "))
            # L = P / n
            lado = p / n

        elif opcao == 7:
            area = float(input("Digite a área do polígono (A): "))
            # Área = (n * L^2) / (4 * tan(pi/n))  =>  L = sqrt((4 * A * tan(pi/n)) / n)
            lado = math.sqrt((4 * area * math.tan(theta)) / n)

        elif opcao == 8:
            ang_interno = ((n - 2) * 180) / n
            ang_externo = 360 / n
            print("\nInformação Geométrica:")
            print(f"Para um polígono de {n} lados:")
            print(f" - Ângulo Interno: {ang_interno:.2f}°")
            print(f" - Ângulo Externo: {ang_externo:.2f}°")
            print("\nNota: O ângulo define apenas a forma do polígono, não seu tamanho.")
            val_ref = float(input("Por favor, informe a medida do Apótema (a) para escalar o tamanho: "))
            lado = 2 * val_ref * math.tan(theta)

        else:
            print("Opção inválida!")
            return

        print("\n" + "-" * 40)
        print(f"RESULTADO: O Lado do polígono de {n} lados é: {lado:.4f}")
        print("-" * 40)

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    calcular_lado()