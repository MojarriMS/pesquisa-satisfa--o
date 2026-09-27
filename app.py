# Programa de Pesquisa de Satisfação - Empresa TudoWeb
# Autora: Mojarri

# 1. Inicialização dos Contadores
excelente = 0
bom = 0
ruim = 0

# Defina 10 para os testes de validação e 50 para a entrega final
total_entrevistados = 10  

# 2. Processamento com Estrutura de Repetição (Loop FOR)
for i in range(1, total_entrevistados + 1):
    print(f"\n--- Entrevistado {i} de {total_entrevistados} ---")
    
    # Coleta de dados do entrevistado
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    
    # Exibição do Menu com as 3 opções da atividade
    print("\nQual a sua opinião sobre o atendimento?")
    print("1: EXCELENTE")
    print("2: BOM")
    print("3: RUIM")
    
    opiniao = int(input("Digite a sua opção (1, 2 ou 3): "))
    
    # Validação da opinião com ciclo WHILE (garante que digite 1, 2 ou 3)
    while opiniao < 1 or opiniao > 3:
        print("\n[ERRO] Opção inválida! Escolha entre 1, 2 ou 3.")
        print("1: EXCELENTE")
        print("2: BOM")
        print("3: RUIM")
        opiniao = int(input("Digite a sua opção: "))

    # Estrutura de Decisão (IF / ELIF) para verificar a opinião
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1

# 3. Saída de Dados
print("\n" + "=" * 40)
print("     RESULTADO FINAL DA PESQUISA     ")
print("=" * 40)
print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"b) Quantidade de respostas 'RUIM': {ruim}")

