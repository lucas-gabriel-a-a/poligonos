import math

def exibir_menu():
    print("=" * 50)
    print("      CALCULADORA DE APÓTEMA DE POLÍGONOS REGULARES")
    print("=" * 50)
    print("Escolha qual dado de entrada você possui:")
    print("1. Lado (L)")
    print("2. Raio da circunferência circunscrita (R)")
    print("3. Raio da circunferência inscrita (r)")
    print("4. Diagonal que passa pelo centro (d) [Apenas para n par]")
    print("5. Altura do polígono (h)")
    print("6. Perímetro (P)")
    print("7. Área total (A)")
    print("8. Ângulo Interno (Ai) ou Ângulo Externo (Ae)")
    print("=" * 50)

def calcular_apotema():
    try:
        n = int(input("Informe o número de lados do polígono (n >= 3): "))
        if n < 3:
            print("Erro: Um polígono precisa ter pelo menos 3 lados.")
            return

        exibir_menu()
        opcao = int(input("Digite a opção desejada (1-8): "))

        # Ângulo central sustentado por meio lado (theta = pi / n)
        theta = math.pi / n

        apotema = None

        if opcao == 1:
            l = float(input("Digite a medida do lado (L): "))
            # a = L / (2 * tan(pi/n))
            apotema = l / (2 * math.tan(theta))

        elif opcao == 2:
            r_circ = float(input("Digite o raio da circunferência circunscrita (R): "))
            # a = R * cos(pi/n)
            apotema = r_circ * math.cos(theta)

        elif opcao == 3:
            r_in = float(input("Digite o raio da circunferência inscrita (r): "))
            # O raio da circunferência inscrita É o próprio apótema
            apotema = r_in

        elif opcao == 4:
            if n % 2 != 0:
                print("\nErro: A diagonal que passa exatamente pelo centro só existe em polígonos com número PAR de lados.")
                return
            d = float(input("Digite o valor da diagonal principal (passa pelo centro): "))
            # A diagonal principal é o diâmetro da circunferência circunscrita (d = 2R)
            r_circ = d / 2
            apotema = r_circ * math.cos(theta)

        elif opcao == 5:
            h = float(input("Digite a altura do polígono (h): "))
            if n % 2 == 0:
                # Para n par, a altura é a distância entre lados opostos (h = 2 * apótema)
                apotema = h / 2
            else:
                # Para n ímpar, h = apótema + R = a + a / cos(pi/n) = a * (1 + 1 / cos(pi/n))
                apotema = h / (1 + (1 / math.cos(theta)))

        elif opcao == 6:
            p = float(input("Digite o perímetro (P): "))
            l = p / n
            apotema = l / (2 * math.tan(theta))

        elif opcao == 7:
            area = float(input("Digite a área do polígono (A): "))
            # Área = n * a^2 * tan(pi/n)  =>  a = sqrt(Área / (n * tan(pi/n)))
            apotema = math.sqrt(area / (n * math.tan(theta)))

        elif opcao == 8:
            print("\nInformação Geométrica:")
            ang_interno = ((n - 2) * 180) / n
            ang_externo = 360 / n
            print(f"Para um polígono de {n} lados:")
            print(f" - Ângulo Interno: {ang_interno:.2f}°")
            print(f" - Ângulo Externo: {ang_externo:.2f}°")
            print("\nNota: O apótema determina a escala geométrica do polígono.")
            l = float(input("Por favor, informe a medida de um lado (L) para definir o tamanho: "))
            apotema = l / (2 * math.tan(theta))

        else:
            print("Opção inválida!")
            return

        print("\n" + "-" * 40)
        print(f"RESULTADO: O Apótema do polígono de {n} lados é: {apotema:.4f}")
        print("-" * 40)

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    calcular_apotema()