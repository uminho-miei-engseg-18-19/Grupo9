# TP5 - Resolução 

### Pergunta 2.1

| Dificuldade | Tempo |
| :--------:  | ----- |
| 2 | 0.14s user 0.03s system 99% cpu 0.168 total |
| 3 | 0.14s user 0.03s system 107% cpu 0.156 total |
| 4 | 0.14s user 0.03s system 116% cpu 0.147 total |
| 5 | 0.15s user 0.03s system 86% cpu 0.203 total |


### Pergunta 2.2

#### 1

O algoritmo de proof of work usa o último valor do proof of work e incrementa 1 unidade. A seguir pega neste valor e verifica se é divisivel por 9 e pelo proof of work anterior, se não for incrementa até ser possível. O código correspondente a este proof of work é o seguinte:

    def proof_of_work(last_proof)
     incrementor = last_proof + 1
  
     while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
         incrementor += 1
  
     return incrementor
  
#### 2

Não é um algoritmo adequado para minerar devido aos seguintes fatores:

* Cálculo da prova é realizado através da prova anterior, o que permite realizar facilmente o cálculo das provas dos blocos antes que estes sejam publicados

* Não é possível definir o grau de dificuldade

* Dificuldade em encontrar um número divisivel por 9 e pelo número do último proof of work torna-se cada vez mais intenso computacionalmente.