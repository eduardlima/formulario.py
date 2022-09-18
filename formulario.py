resposta1 = []
resposta2 = []
resposta3 = []
resposta4 = []
print("Vamos ver se você esta com fome")
print("---------------------------------")
opt = input("\ndigite aqui: ").upper()
resposta = "S"

if opt == "S":
    print("SIM então vamos para o formulario")
else:
    print("Você vai ficar magrinha ")
while resposta=="S":
 print("\nSim esqueci qual e seu nome mesmo ?")
 print("---------------------------------")
 resposta1.append(input("\ndigite aqui: "))
 
 print("\nNâo foi comer porque está com preguisa?")
 print("---------------------------------")
 resposta2.append(input("\ndigite aqui: ").upper())
 if resposta2 == "Sim":
    print("eu até iria mas estou com preguiça tambem")

 print("\nVocê quer um refri?")
 print("---------------------------------")
 resposta3.append(input("\ndigite aqui: ").upper())
 if resposta3 == "Sim":
     print("então vai comprar kkkkkkkkk")

 print("\noque vc quer comer ?")
 print("---------------------------------")
 resposta4.append(input("\ndigite aqui: "))

 resposta=input("digite \"S\" para continuar: ").upper()

 for i in range(len(resposta1)):
      print("\nresultado 1: ",resposta1[i])
      print("resultado 2: ",resposta2[i])
      print("resultado 3: ",resposta3[i])
      print("resultado 4: ", resposta4[i])
