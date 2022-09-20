taxa = 50
diarias= float (input("informe a quantidade de diárias:"))

if diarias < 15:
    print (f" o número de diarias é {diarias} e o valor a ser pago pelo cliente é de: {diarias * 1.5 + 50}")

elif diarias == 15:
    print(f"o número de diarias é {diarias} e o valor a ser pago pelo cliente é de {diarias * 1 + 50}")

elif diarias > 15:
    print(f"o mumerdo de diárias é {diarias} e o valor a ser pago pelo cliente é {diarias * 0.5 + 50}")    