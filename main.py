#print("Hello World!")
#print("Sejam Bem-Vindos")

#media_final = int(input("Digite sua média final: "))
#if media_final >= 70:
#    print("APROVADO!")
#else:
#    print("REPROVADO!")

vel_car = int(input("Digite a velocidade do seu carro em km/h: " ))
multa = int(vel_car - 80) * 5
if vel_car > 80:
    print(f"Você foi multado! R$ {multa:.2f}.")
else:
    print("Sai pra lá vovó!")
