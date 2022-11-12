def soma_imposto(taxa_imposto, custo):
    taxa_imposto = taxa_imposto/100  #decobrir a % 0,2
    calcular_taxa = taxa_imposto*custo #valor da taxa    
    valorfinal = custo + calcular_taxa
    print (f'O valor final do produto com a taxa de imposto é: R$ {valorfinal}')

taxa = float(input('Digite o valor da taxa: '))
custo_produto = float(input('Digite o custo do produto: '))

soma_imposto(taxa, custo_produto)