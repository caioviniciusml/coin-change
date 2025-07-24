# Problema do Troco Ótimo

O problema do "Troco Ótimo" é um problema clássico de otimização combinatória, consistindo em dado um conjunto de moedas com diferentes denominações (valores) e um valor alvo específico, determinar a quantidade mínima de moedas necessária para compor esse valor requerido. Neste repositório, iremos abordar especificamente as soluções que utilizam abordagem gulosa e programação dinâmica.

## Programação Dinâmica

A solução por programação dinâmica aborda o problema dividindo-o em subproblemas menores e sobrepostos. Ela constrói um vetor onde cada posição representa o número mínimo de moedas necessárias para compor cada valor intermediário até o valor-alvo. A técnica explora a otimalidade de subestrutura, garantindo que a solução para o valor maior dependa das soluções ótimas para valores menores. Essa abordagem é completa e sempre encontra a solução ótima quando ela existe.

- **Complexidade de Tempo:** O(n · v), onde `n` é o número de moedas (tamanho do conjunto `s`) e `v` é o valor-alvo.
- **Complexidade de Espaço:** O(v), pois é necessário armazenar resultados para todos os subvalores de 1 até v.

## Abordagem Gulosa

A abordagem gulosa tenta resolver o problema selecionando, a cada passo, a moeda de maior valor possível que não ultrapasse o valor restante. Essa estratégia é eficiente e simples, mas não é garantidamente ótima para todos os conjuntos de moedas. Ela funciona corretamente quando as moedas formam um sistema canônico, como o sistema decimal (ex: moedas 1, 5, 10, 25). Contudo, em conjuntos não canônicos, a abordagem falha, tomando como exemplo o conjunto de moedas [1, 3, 4] buscando atingir o valor alvo 6, onde a solução gulosa seleciona 4 + 1 + 1 (3 moedas) ao invés da solução ótima 3 + 3 (2 moedas).

- **Complexidade de Tempo:** O(n + k), sendo `n` o número de moedas e `k` o número total de moedas usadas na solução.
- **Complexidade de Espaço:** O(1), pois a solução utiliza apenas algumas variáveis simples e nenhuma estrutura auxiliar é instanciada.

## Como Rodar o Código

1. **Verifique se o Python está instalado na sua Máquina**  
```
python --version
```
Caso não tenha o Python Instalado, você pode baixá-lo clicando aqui: 
[https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Clone o Projeto**
```
git clone https://github.com/caioviniciusml/coin-change.git
```

3. **Va para a Pasta do Projeto**
```
cd coin-change/
```

4. **Execute o código**
```
python coin_change.py
```