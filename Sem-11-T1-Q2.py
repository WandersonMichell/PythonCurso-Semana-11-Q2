# Função para calcular a média dos números fornecidos pelo usuário.
def calcular():
	
	divisao = 0  # Inicializa o contador de números diferentes de zero
	n = 0  # Inicializa a soma dos números

	while True:  # Loop infinito para receber entrada do usuário
		
		num = int(input("Digite um número (0 para encerrar): ").strip())  # Solicita um número ao usuário
		
		if num != 0:
			n += num  # Adiciona o número à soma
			divisao += 1  # Incrementa o contador de números diferentes de zero
			
		elif num == 0:
			break  # Sai do loop se o usuário digitar zero

	res = n / divisao  # Calcula a média
	print(f'A média dos números fornecidos é: {res:.2f}')

def main():
	
	calcular()  # Chama a função de cálculo da média
	
if __name__ == '__main__':
	main()
