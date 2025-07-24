# Programação Dinâmica

def dp_coin_change(s, v):
    dp = [v] * (v + 1)
    dp[0] = 0

    for i in range(1, v + 1):
        for coin in s:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[-1] if dp[-1] != v else None

# Abordagem Gulosa

def greedy_coin_change(s, v):
    k = 0

    for i in range(len(s) - 1, -1, -1): 
        while v >= s[i]: 
            v -= s[i] 
            k += 1  

    return k if v == 0 else None

# Demonstração dos Algoritmos

coins_input = input("\nInsira um conjunto de moedas ordenado crescentemente, separando os valores por vírgulas (Ex: 1, 2, 5, 10): ")
targets_input = input("Insira um conjunto de valores alvos a serem antigos, separando os valores alvo por vírgulas (Ex: 12, 129, 324): ")

coins = [int(coin.strip()) for coin in coins_input.split(",")]
targets = [int(target.strip()) for target in targets_input.split(",")]

print(f"\nConjunto de Moedas (s): {coins} \nValores Alvo (v): {targets}")

for target in targets:
    print(f"\n- Valor Alvo {target}:")
    print(f"\nProgramação Dinâmica: k = {dp_coin_change(coins,target)} \nAbordagem Gulosa: k = {greedy_coin_change(coins, target)} ")