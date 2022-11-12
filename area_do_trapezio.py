def areadotrapezio(basemaior, basemenor, altura):
    

    areat = float(basemaior+basemenor)*altura/2
    print(f'A area do trapézio é: {areat}')





base_maior = float(input("Digite a base maior: "))
base_menor = float(input("Digite a base menor: "))
h = float(input("Digite a altura: "))

areadotrapezio(base_maior, base_menor, h)