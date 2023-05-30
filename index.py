def principal():
    qualprod = int(input('Insira o codigo do produto:'))
    qtdprodutos = int(input('Informe a quantidade do produto:'))
   
    if qualprod == 1001:
        return 1.50 * qtdprodutos

    if qualprod == 1002:
        return 2.50 * qtdprodutos

    if qualprod == 1003:
        return 3.50 * qtdprodutos

    if qualprod == 1004:
        return 4.50 * qtdprodutos

    if qualprod == 1005:
        return 5.50 * qtdprodutos
    else:
        print("codigo de produto invalido!")
    
    

resultadofinal = 0

typeprodut = int(input("Quantos tipos de produtos?"))

while typeprodut > 0:
    resultadofinal += principal()
    typeprodut = typeprodut - 1

print(f"Valor total: {resultadofinal:.2f}")
