import math

def calcular_tudo_poligono(n, **kwargs):
    """
    Calcula todas as propriedades métricas de um polígono regular de 'n' lados
    com base em APENAS UMA variável conhecida fornecida via kwargs.
    """
    if n < 3:
        print("\n❌ Erro: Um polígono deve ter pelo menos 3 lados.")
        return None

    # Ângulos fundamentais
    angulo_interno = ((n - 2) * 180) / n
    angulo_externo = 360 / n
    angulo_central = 360 / n
    alpha = math.radians(180 / n)  # Metade do ângulo central em radianos

    lado = None

    # Processa o input e deduz o lado do polígono
    if 'lado' in kwargs:
        lado = float(kwargs['lado'])
    elif 'apotema' in kwargs or 'raio_inscrito' in kwargs:
        # Apótema e raio inscrito são identidades geométricas em polígonos regulares
        apotema = float(kwargs.get('apotema') or kwargs.get('raio_inscrito'))
        lado = 2 * apotema * math.tan(alpha)
    elif 'raio_circunscrito' in kwargs:
        raio_c = float(kwargs['raio_circunscrito'])
        lado = 2 * raio_c * math.sin(alpha)
    elif 'area' in kwargs:
        area = float(kwargs['area'])
        lado = math.sqrt((4 * area * math.tan(alpha)) / n)
    elif 'perimetro' in kwargs:
        perimetro = float(kwargs['perimetro'])
        lado = perimetro / n
    elif 'diagonal_max' in kwargs:
        diag = float(kwargs['diagonal_max'])
        if n % 2 == 0:
            raio_c = diag / 2
            lado = 2 * raio_c * math.sin(alpha)
        else:
            lado = diag * math.sin(alpha) / math.cos(alpha / 2)
    else:
        print("\n⚠️ Nenhum valor numérico linear fornecido.")
        return None

    # Cálculo em cadeia de todas as propriedades físicas
    perimetro_calc = n * lado
    apotema_calc = lado / (2 * math.tan(alpha))
    raio_inscrito_calc = apotema_calc
    raio_circunscrito_calc = lado / (2 * math.sin(alpha))
    area_calc = (n * lado * apotema_calc) / 2
    num_diagonais = int(n * (n - 3) / 2)
    
    # Cálculo da maior diagonal
    if n % 2 == 0:
        diagonal_max_calc = 2 * raio_circunscrito_calc
    else:
        diagonal_max_calc = lado * math.cos(alpha / 2) / math.sin(alpha)

    # Definição Geométrica da Altura de um Polígono Regular:
    # Se PAR: Distância entre duas faces paralelas opostas (2x apótema)
    # Se ÍMPAR: Distância da base até o vértice oposto do topo (Raio Circunscrito + Apótema)
    if n % 2 == 0:
        altura = 2 * apotema_calc
    else:
        altura = raio_circunscrito_calc + apotema_calc

    # Exibição do relatório formatado
    print("\n" + "="*50)
    print(f"📐 RELATÓRIO DO POLÍGONO REGULAR DE {n} LADOS")
    print("="*50)
    print(f"📏 ALTURA TOTAL:           {altura:.4f}")
    print(f"🔹 Lado:                   {lado:.4f}")
    print(f"🔹 Apótema (R. Inscrito):  {apotema_calc:.4f}")
    print(f"🔹 Raio Circunscrito:      {raio_circunscrito_calc:.4f}")
    print(f"🔹 Perímetro:              {perimetro_calc:.4f}")
    print(f"🔹 Área:                   {area_calc:.4f}")
    print(f"🔹 Diagonal Máxima:        {diagonal_max_calc:.4f}")
    print(f"🔹 Total de Diagonais:     {num_diagonais}")
    print("-"*50)
    print(f"🔸 Ângulo Interno:         {angulo_interno:.2f}°")
    print(f"🔸 Ângulo Externo:         {angulo_externo:.2f}°")
    print(f"🔸 Ângulo Central:         {angulo_central:.2f}°")
    print("="*50 + "\n")


def menu_interativo():
    print("================================================")
    print("   🧮 CALCULADORA UNIVERSAL DE POLÍGONOS")
    print("================================================")
    
    try:
        n = int(input("Digite o número de lados do polígono (n >= 3): "))
        if n < 3:
            print("❌ O número de lados precisa ser maior ou igual a 3.")
            return
    except ValueError:
        print("❌ Digite um número inteiro válido.")
        return

    print("\nQual dado você possui para o cálculo?")
    print("1 - Lado")
    print("2 - Apótema (ou Raio da Circunferência Inscrita)")
    print("3 - Raio da Circunferência Circunscrita")
    print("4 - Área")
    print("5 - Perímetro")
    print("6 - Diagonal Máxima")
    
    opcao = input("\nEscolha uma opção (1-6): ").strip()
    
    if opcao not in ['1', '2', '3', '4', '5', '6']:
        print("❌ Opção inválida.")
        return

    try:
        valor = float(input("Digite o valor numérico dessa medida: "))
    except ValueError:
        print("❌ O valor inserido precisa ser um número real válido.")
        return

    # Mapeia as opções para os argumentos corretos da função
    if opcao == '1':
        calcular_tudo_poligono(n, lado=valor)
    elif opcao == '2':
        calcular_tudo_poligono(n, apotema=valor)
    elif opcao == '3':
        calcular_tudo_poligono(n, raio_circunscrito=valor)
    elif opcao == '4':
        calcular_tudo_poligono(n, area=valor)
    elif opcao == '5':
        calcular_tudo_poligono(n, perimetro=valor)
    elif opcao == '6':
        calcular_tudo_poligono(n, diagonal_max=valor)

if __name__ == "__main__":
    # Mantém o programa rodando até o usuário decidir fechar
    while True:
        menu_interativo()
        continuar = input("Deseja calcular outro polígono? (S/N): ").strip().upper()
        if continuar != 'S':
            print("\nObrigado por usar a calculadora! Encerrando...")
            break
        print("\n" + "-"*50 + "\n")
