from time import sleep

print("-="*25)
print(r"""
 ██████╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██║████╗  ██║██╔════╝
██║     ██║   ██║██║██╔██╗ ██║███████╗
██║     ██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
                           Fase BETA
                                 Powered by Fonso
""")
print("-="*25)

#adimn


#Perguntas variaveis
Perguntas_certas = 0

#Sistema de moedas
Saldo = 0
preçol1 = 100

# inventario variaveis
pulos_fase = 0
mostrar_resposta = False
dicas = 0

print("Olá se bem vindo, ao Coins, o Coins é um jogo de trivia bem divertido com moedas, o Coins esta em fase BETA, pode ter alguns erros e pode não ter muita coisa ainda!")
sleep(11)
print("")
print("Qual é o planeta mais perto do Sol?")
operador = input("1: Terra\n2: Mercúrio\n3: Jupiter\n0pção:")

if operador == "2":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["1", "3"]:
    print("Resposta errada.Fica para a próxima.")
sleep(2)
print("")
print("Qual é o maior oceano do mundo? ") #pacifico
operador = input("1: Pacífico\n2: Atlântico\n3: Mediterrâneo\n0pção:")
if operador == "1":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["2", "3"]:
    print("Resposta errada.Fica para a próxima.")
sleep(2)
print("")
print("Deseja usar na Loja. ")
operador = input("S: Sim\nN: Não\n0pção:")
if operador == "S":
    print("")
    print("Coins Loja")
    print(f"Seu Saldo Atual: {Saldo} ")
    operador = input("1: 200€: Saltar 1 fase\n2: 150€: Mostrar Resposta\n3: 100€: Dica\n0pção:")
if operador == "1":
    if Saldo >= 200:
        Saldo -= 200
        pulos_fase += 1
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")

elif operador == "2":
    if Saldo >= 150:
        Saldo -= 150
        mostrar_resposta = True
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")

elif operador == "3":
    if Saldo >= 100:
        Saldo -= 100
        dicas += 1
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")
elif operador in ["N"]:
    print("Por favor,aguarde... ")
sleep(2)
print("")
print("Qual foi o primeiro Rei de Portugal")
operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
if operador == "3":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["1", "2"]:
    print("Resposta errada.Fica para a próxima.")
elif operador == "4":
    print("")
    print("Usar inventario?")
    operador = input("S: Sim\nN: Não\n0pção:")
    if operador == "S":
        print("")
        print("Qual item queres usar")
        print("")
        print("Inventario")
        operador = input(f"1: Pulos de fase:{pulos_fase}\n2: Mostrar resposta:{mostrar_resposta}\n3: Dicas:{dicas}\n0pção: ")
if operador == "1":
    if pulos_fase >= 1:
        pulos_fase -= 1
        Perguntas_certas += 1
        Saldo += 100
        print("Fase pulada, por favor aguarde...")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "2":
    if mostrar_resposta >= 1:
        mostrar_resposta -= 1
        print("A resposta é: 3")
        sleep(3)
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem respostas o suficiente!")
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "3":
    if dicas >= 1:
        dicas -= 1
        print("A primeira letra do seu nome é A.")
        sleep(3)
        print("Você não tem pulos de fase suficientes!")
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
elif operador == "N":
    print("")
    print("Por favor,aguarde... ")
    print("")
    print("Qual foi o primeiro Rei de Portugal")
    operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n0pção:")
    if operador == "3":
        print("Resposta certa!Ganhaste 100 moedas!")
        Saldo += 100
        Perguntas_certas += 1
    elif operador in ["1", "2"]:
        print("Resposta errada.Fica para a próxima.")
        print("")
print("")
print("Qual planeta é conhecido como o Planeta Vermelho?")
operador = input("1: Terra\n2: Marte\n3: Saturno\n\n4: Usar item da loja\n0pção:")
if operador == "2":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["1", "3"]:
    print("Resposta errada.Fica para a próxima.")

elif operador == "4":
    print("")
    print("Usar inventario?")
    operador = input("S: Sim\nN: Não\n0pção:")
if operador == "S":
    print("")
    print("Qual item queres usar")
    print("")
    print("Inventario")
    operador = input(f"1: Pulos de fase:{pulos_fase}\n2: Mostrar resposta:{mostrar_resposta}\n3: Dicas:{dicas}\n0pção: ")
if operador == "1":
    if pulos_fase >= 1:
        pulos_fase -= 1
        Perguntas_certas += 1
        print("Fase pulada, por favor aguarde...")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual planeta é conhecido como o Planeta Vermelho?")  # Pensar em pergunta 🪐 Qual planeta é conhecido como o Planeta Vermelho?
        operador = input("1: Terra\n2: Saturno\n3: Marte\n\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "2":
    if mostrar_resposta >= 1:
        mostrar_resposta -= 1
        print("A resposta é: 3")
        sleep(3)
        print("Qual planeta é conhecido como o Planeta Vermelho?")
        operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
        else:
            print("Você não tem respostas o suficiente!")
            print("Qual planeta é conhecido como o Planeta Vermelho?")
            operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
            if operador == "2":
                print("Resposta certa!Ganhaste 100 moedas!")
                Saldo += 100
                Perguntas_certas += 1
            elif operador in ["1", "3"]:
                print("Resposta errada.Fica para a próxima.")
if operador == "3":
    if dicas >= 1:
        dicas -= 1
        print("É o 4.º planeta a contar do Sol.")
        sleep(3)
        print("Você não tem pulos de fase suficientes!")
        print("Qual planeta é conhecido como o Planeta Vermelho?")
        operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual planeta é conhecido como o Planeta Vermelho?")
        operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
elif operador == "N":
    print("")
    print("Por favor,aguarde...")
    print("")
    print("Qual planeta é conhecido como o Planeta Vermelho?")
    operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
    if operador == "2":
        print("Resposta certa!Ganhaste 100 moedas!")
        Saldo += 100
        Perguntas_certas += 1
    elif operador in ["1", "3"]:
        print("Resposta errada.Fica para a próxima.")

sleep(2)
print("")
print("Deseja usar na Loja. ")
operador = input("S: Sim\nN: Não\n0pção:")
if operador == "S":
    print("")
    print("Coins Loja")
    print(f"Seu Saldo Atual: {Saldo} ")
    operador = input("1: 200€: Saltar 1 fase\n2: 150€: Mostrar Resposta\n3: 100€: Dica\n0pção:")
if operador == "1":
    if Saldo >= 200:
        Saldo -= 200
        pulos_fase += 1
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")

elif operador == "2":
    if Saldo >= 150:
        Saldo -= 150
        mostrar_resposta = True
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")

elif operador == "3":
    if Saldo >= 100:
        Saldo -= 100
        dicas += 1
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")
elif operador in ["N"]:
    print("Por favor,aguarde... ")
sleep(2) # 9. 🌎 Qual é o maior país do mundo em área? A) Canadá B) China C) Rússia
print("")
print("Qual é o maior país do mundo")
operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
if operador == "2":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["1", "3"]:
    print("Resposta errada.Fica para a próxima.")
elif operador == "4":
    print("")
    print("Usar inventario?")
    operador = input("S: Sim\nN: Não\n0pção:")
    if operador == "S":
        print("")
        print("Qual item queres usar")
        print("")
        print("Inventario")
        operador = input(f"1: Pulos de fase:{pulos_fase}\n2: Mostrar resposta:{mostrar_resposta}\n3: Dicas:{dicas}\n0pção: ")
if operador == "1":
    if pulos_fase >= 1:
        pulos_fase -= 1
        Perguntas_certas += 1
        print("Fase pulada, por favor aguarde...")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "2":
    if mostrar_resposta >= 1:
        mostrar_resposta -= 1
        print("A resposta é: 3")
        sleep(3)
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem respostas o suficiente!")
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "3":
    if dicas >= 1:
        dicas -= 1
        print("É um dos países mais frios do mundo e tem uma bandeira com três cores")
        sleep(3)
        print("Você não tem pulos de fase suficientes!")
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
elif operador == "N":
    print("")
    print("Por favor,aguarde... ")
    print("")
    print("Qual é o maior país do mundo")
    operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
    if operador == "2":
        print("Resposta certa!Ganhaste 100 moedas!")
        Saldo += 100
        Perguntas_certas += 1
    elif operador in ["1", "3"]:
        print("Resposta errada.Fica para a próxima.")
        print("")
print("")
print("Qual é o estado da água quando se transforma em gelo??")
operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
if operador == "1":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["2", "3"]:
    print("Resposta errada.Fica para a próxima.")

elif operador == "4":
    print("")
    print("Usar inventario?")
    operador = input("S: Sim\nN: Não\n0pção:")
if operador == "S":
    print("")
    print("Qual item queres usar")
    print("")
    print("Inventario")
    operador = input(f"1: Pulos de fase:{pulos_fase}\n2: Mostrar resposta:{mostrar_resposta}\n3: Dicas:{dicas}\n0pção: ")
    if operador == "1":
        if pulos_fase >= 1:
            pulos_fase -= 1
            Perguntas_certas += 1
            print("Fase pulada, por favor aguarde...")
        else:
            print("Você não tem pulos de fase suficientes!")
            print("Qual é o estado da água quando se transforma em gelo??")
            operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
            if operador == "1":
                print("Resposta certa!Ganhaste 100 moedas!")
                Saldo += 100
                Perguntas_certas += 1
            elif operador in ["2", "3"]:
                print("Resposta errada.Fica para a próxima.")
if operador == "2":
    if mostrar_resposta >= 1:
        mostrar_resposta -= 1
        print("A resposta é: 3")
        sleep(3)
        print("Qual é o estado da água quando se transforma em gelo??")
        operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
        if operador == "1":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["2", "3"]:
            print("Resposta errada.Fica para a próxima.")
        else:
            print("Você não tem respostas o suficiente!")
            print("Qual é o estado da água quando se transforma em gelo??")
            operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
            if operador == "1":
                print("Resposta certa!Ganhaste 100 moedas!")
                Saldo += 100
                Perguntas_certas += 1
            elif operador in ["2", "3"]:
                print("Resposta errada.Fica para a próxima.")
if operador == "3":
    if dicas >= 1:
        dicas -= 1
        print("Começa pela letra S!")
        sleep(3)
        print("Você não tem dicas suficientes!")
        print("Qual é o estado da água quando se transforma em gelo??")
        operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
        if operador == "1":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["3", "2"]:
            print("Resposta errada.Fica para a próxima.")
        else:
            print("Você não tem pulos de fase suficientes!")
            print("Qual é o estado da água quando se transforma em gelo??")
            operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
            if operador == "1":
                print("Resposta certa!Ganhaste 100 moedas!")
                Saldo += 100
                Perguntas_certas += 1
            elif operador in ["3", "2"]:
                print("Resposta errada.Fica para a próxima.")
elif operador == "N":
    print("")
    print("Por favor,aguarde...")
    print("")
    print("Qual é o estado da água quando se transforma em gelo??")
    operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
    if operador == "1":
        print("Resposta certa!Ganhaste 100 moedas!")
        Saldo += 100
        Perguntas_certas += 1
    elif operador in ["2", "3"]:
        print("Resposta errada.Fica para a próxima.")

print("")
Perguntas_certas
if Perguntas_certas >= 6:
    print(f"Parabens foste muito bem tens 7/{Perguntas_certas} perguntas certas!")from time import sleep

print("-="*25)
print(r"""
 ██████╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██║████╗  ██║██╔════╝
██║     ██║   ██║██║██╔██╗ ██║███████╗
██║     ██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
                           Fase BETA
                                 Powered by Fonso
""")
print("-="*25)

#adimn


#Perguntas variaveis
Perguntas_certas = 0

#Sistema de moedas
Saldo = 0
preçol1 = 100

# inventario variaveis
pulos_fase = 0
mostrar_resposta = False
dicas = 0

print("Olá se bem vindo, ao Coins, o Coins é um jogo de trivia bem divertido com moedas, o Coins esta em fase BETA, pode ter alguns erros e pode não ter muita coisa ainda!")
sleep(11)
print("")
print("Qual é o planeta mais perto do Sol?")
operador = input("1: Terra\n2: Mercúrio\n3: Jupiter\n0pção:")

if operador == "2":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["1", "3"]:
    print("Resposta errada.Fica para a próxima.")
sleep(2)
print("")
print("Qual é o maior oceano do mundo? ") #pacifico
operador = input("1: Pacífico\n2: Atlântico\n3: Mediterrâneo\n0pção:")
if operador == "1":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["2", "3"]:
    print("Resposta errada.Fica para a próxima.")
sleep(2)
print("")
print("Deseja usar na Loja. ")
operador = input("S: Sim\nN: Não\n0pção:")
if operador == "S":
    print("")
    print("Coins Loja")
    print(f"Seu Saldo Atual: {Saldo} ")
    operador = input("1: 200€: Saltar 1 fase\n2: 150€: Mostrar Resposta\n3: 100€: Dica\n0pção:")
if operador == "1":
    if Saldo >= 200:
        Saldo -= 200
        pulos_fase += 1
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")

elif operador == "2":
    if Saldo >= 150:
        Saldo -= 150
        mostrar_resposta = True
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")

elif operador == "3":
    if Saldo >= 100:
        Saldo -= 100
        dicas += 1
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")
elif operador in ["N"]:
    print("Por favor,aguarde... ")
sleep(2)
print("")
print("Qual foi o primeiro Rei de Portugal")
operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
if operador == "3":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["1", "2"]:
    print("Resposta errada.Fica para a próxima.")
elif operador == "4":
    print("")
    print("Usar inventario?")
    operador = input("S: Sim\nN: Não\n0pção:")
    if operador == "S":
        print("")
        print("Qual item queres usar")
        print("")
        print("Inventario")
        operador = input(f"1: Pulos de fase:{pulos_fase}\n2: Mostrar resposta:{mostrar_resposta}\n3: Dicas:{dicas}\n0pção: ")
if operador == "1":
    if pulos_fase >= 1:
        pulos_fase -= 1
        Perguntas_certas += 1
        Saldo += 100
        print("Fase pulada, por favor aguarde...")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "2":
    if mostrar_resposta >= 1:
        mostrar_resposta -= 1
        print("A resposta é: 3")
        sleep(3)
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem respostas o suficiente!")
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "3":
    if dicas >= 1:
        dicas -= 1
        print("A primeira letra do seu nome é A.")
        sleep(3)
        print("Você não tem pulos de fase suficientes!")
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual foi o primeiro Rei de Portugal")
        operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
elif operador == "N":
    print("")
    print("Por favor,aguarde... ")
    print("")
    print("Qual foi o primeiro Rei de Portugal")
    operador = input("1: D. João II\n2: D. Manuel I\n3: D. Afonso Henriques\n\n0pção:")
    if operador == "3":
        print("Resposta certa!Ganhaste 100 moedas!")
        Saldo += 100
        Perguntas_certas += 1
    elif operador in ["1", "2"]:
        print("Resposta errada.Fica para a próxima.")
        print("")
print("")
print("Qual planeta é conhecido como o Planeta Vermelho?")
operador = input("1: Terra\n2: Marte\n3: Saturno\n\n4: Usar item da loja\n0pção:")
if operador == "2":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["1", "3"]:
    print("Resposta errada.Fica para a próxima.")

elif operador == "4":
    print("")
    print("Usar inventario?")
    operador = input("S: Sim\nN: Não\n0pção:")
if operador == "S":
    print("")
    print("Qual item queres usar")
    print("")
    print("Inventario")
    operador = input(f"1: Pulos de fase:{pulos_fase}\n2: Mostrar resposta:{mostrar_resposta}\n3: Dicas:{dicas}\n0pção: ")
if operador == "1":
    if pulos_fase >= 1:
        pulos_fase -= 1
        Perguntas_certas += 1
        print("Fase pulada, por favor aguarde...")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual planeta é conhecido como o Planeta Vermelho?")  # Pensar em pergunta 🪐 Qual planeta é conhecido como o Planeta Vermelho?
        operador = input("1: Terra\n2: Saturno\n3: Marte\n\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "2":
    if mostrar_resposta >= 1:
        mostrar_resposta -= 1
        print("A resposta é: 3")
        sleep(3)
        print("Qual planeta é conhecido como o Planeta Vermelho?")
        operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
        else:
            print("Você não tem respostas o suficiente!")
            print("Qual planeta é conhecido como o Planeta Vermelho?")
            operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
            if operador == "2":
                print("Resposta certa!Ganhaste 100 moedas!")
                Saldo += 100
                Perguntas_certas += 1
            elif operador in ["1", "3"]:
                print("Resposta errada.Fica para a próxima.")
if operador == "3":
    if dicas >= 1:
        dicas -= 1
        print("É o 4.º planeta a contar do Sol.")
        sleep(3)
        print("Você não tem pulos de fase suficientes!")
        print("Qual planeta é conhecido como o Planeta Vermelho?")
        operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual planeta é conhecido como o Planeta Vermelho?")
        operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
elif operador == "N":
    print("")
    print("Por favor,aguarde...")
    print("")
    print("Qual planeta é conhecido como o Planeta Vermelho?")
    operador = input("1: Terra\n2: Marte\n3: Saturno\n\n0pção:")
    if operador == "2":
        print("Resposta certa!Ganhaste 100 moedas!")
        Saldo += 100
        Perguntas_certas += 1
    elif operador in ["1", "3"]:
        print("Resposta errada.Fica para a próxima.")

sleep(2)
print("")
print("Deseja usar na Loja. ")
operador = input("S: Sim\nN: Não\n0pção:")
if operador == "S":
    print("")
    print("Coins Loja")
    print(f"Seu Saldo Atual: {Saldo} ")
    operador = input("1: 200€: Saltar 1 fase\n2: 150€: Mostrar Resposta\n3: 100€: Dica\n0pção:")
if operador == "1":
    if Saldo >= 200:
        Saldo -= 200
        pulos_fase += 1
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")

elif operador == "2":
    if Saldo >= 150:
        Saldo -= 150
        mostrar_resposta = True
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")

elif operador == "3":
    if Saldo >= 100:
        Saldo -= 100
        dicas += 1
        print("Compra bem sucedida! Seu saldo atual é:", Saldo)
    else:
        print("Saldo insuficiente!")
elif operador in ["N"]:
    print("Por favor,aguarde... ")
sleep(2) # 9. 🌎 Qual é o maior país do mundo em área? A) Canadá B) China C) Rússia
print("")
print("Qual é o maior país do mundo")
operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
if operador == "2":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["1", "3"]:
    print("Resposta errada.Fica para a próxima.")
elif operador == "4":
    print("")
    print("Usar inventario?")
    operador = input("S: Sim\nN: Não\n0pção:")
    if operador == "S":
        print("")
        print("Qual item queres usar")
        print("")
        print("Inventario")
        operador = input(f"1: Pulos de fase:{pulos_fase}\n2: Mostrar resposta:{mostrar_resposta}\n3: Dicas:{dicas}\n0pção: ")
if operador == "1":
    if pulos_fase >= 1:
        pulos_fase -= 1
        Perguntas_certas += 1
        print("Fase pulada, por favor aguarde...")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "3":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "2"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "2":
    if mostrar_resposta >= 1:
        mostrar_resposta -= 1
        print("A resposta é: 3")
        sleep(3)
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem respostas o suficiente!")
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
if operador == "3":
    if dicas >= 1:
        dicas -= 1
        print("É um dos países mais frios do mundo e tem uma bandeira com três cores")
        sleep(3)
        print("Você não tem pulos de fase suficientes!")
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
    else:
        print("Você não tem pulos de fase suficientes!")
        print("Qual é o maior país do mundo")
        operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
        if operador == "2":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["1", "3"]:
            print("Resposta errada.Fica para a próxima.")
elif operador == "N":
    print("")
    print("Por favor,aguarde... ")
    print("")
    print("Qual é o maior país do mundo")
    operador = input("1: Canadá\n2: Rússia\n3: China\n\n4: Usar item da loja\n0pção:")
    if operador == "2":
        print("Resposta certa!Ganhaste 100 moedas!")
        Saldo += 100
        Perguntas_certas += 1
    elif operador in ["1", "3"]:
        print("Resposta errada.Fica para a próxima.")
        print("")
print("")
print("Qual é o estado da água quando se transforma em gelo??")
operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
if operador == "1":
    print("Resposta certa!Ganhaste 100 moedas!")
    Saldo += 100
    Perguntas_certas += 1
elif operador in ["2", "3"]:
    print("Resposta errada.Fica para a próxima.")

elif operador == "4":
    print("")
    print("Usar inventario?")
    operador = input("S: Sim\nN: Não\n0pção:")
if operador == "S":
    print("")
    print("Qual item queres usar")
    print("")
    print("Inventario")
    operador = input(f"1: Pulos de fase:{pulos_fase}\n2: Mostrar resposta:{mostrar_resposta}\n3: Dicas:{dicas}\n0pção: ")
    if operador == "1":
        if pulos_fase >= 1:
            pulos_fase -= 1
            Perguntas_certas += 1
            print("Fase pulada, por favor aguarde...")
        else:
            print("Você não tem pulos de fase suficientes!")
            print("Qual é o estado da água quando se transforma em gelo??")
            operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
            if operador == "1":
                print("Resposta certa!Ganhaste 100 moedas!")
                Saldo += 100
                Perguntas_certas += 1
            elif operador in ["2", "3"]:
                print("Resposta errada.Fica para a próxima.")
if operador == "2":
    if mostrar_resposta >= 1:
        mostrar_resposta -= 1
        print("A resposta é: 3")
        sleep(3)
        print("Qual é o estado da água quando se transforma em gelo??")
        operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
        if operador == "1":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["2", "3"]:
            print("Resposta errada.Fica para a próxima.")
        else:
            print("Você não tem respostas o suficiente!")
            print("Qual é o estado da água quando se transforma em gelo??")
            operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
            if operador == "1":
                print("Resposta certa!Ganhaste 100 moedas!")
                Saldo += 100
                Perguntas_certas += 1
            elif operador in ["2", "3"]:
                print("Resposta errada.Fica para a próxima.")
if operador == "3":
    if dicas >= 1:
        dicas -= 1
        print("Começa pela letra S!")
        sleep(3)
        print("Você não tem dicas suficientes!")
        print("Qual é o estado da água quando se transforma em gelo??")
        operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
        if operador == "1":
            print("Resposta certa!Ganhaste 100 moedas!")
            Saldo += 100
            Perguntas_certas += 1
        elif operador in ["3", "2"]:
            print("Resposta errada.Fica para a próxima.")
        else:
            print("Você não tem pulos de fase suficientes!")
            print("Qual é o estado da água quando se transforma em gelo??")
            operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
            if operador == "1":
                print("Resposta certa!Ganhaste 100 moedas!")
                Saldo += 100
                Perguntas_certas += 1
            elif operador in ["3", "2"]:
                print("Resposta errada.Fica para a próxima.")
elif operador == "N":
    print("")
    print("Por favor,aguarde...")
    print("")
    print("Qual é o estado da água quando se transforma em gelo??")
    operador = input("1: Solido\n2: Gasoso\n3: Liquido\n\n4: Usar item da loja\n0pção:")
    if operador == "1":
        print("Resposta certa!Ganhaste 100 moedas!")
        Saldo += 100
        Perguntas_certas += 1
    elif operador in ["2", "3"]:
        print("Resposta errada.Fica para a próxima.")

print("")
Perguntas_certas
if Perguntas_certas >= 6:
    print(f"Parabens foste muito bem tens 7/{Perguntas_certas} perguntas certas!")
