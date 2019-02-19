 
# TP1- Resolução

### Pergunta P1.1


| Comando | Tempo |
| ------ | ------ |
| head -c 32 /dev/random \| openssl enc -base64 | 10 ms |
| head -c 64 /dev/random \| openssl enc -base64 | 11 ms |
| head -c 1024 /dev/random \| openssl enc -base64 | 26 min 43 s |
| head -c 1024 /dev/urandom \| openssl enc -base64 | 9 ms |

Após a execução dos comandos foi possivel verificar que, em numeros de tamanho reduzido (32 e 64), não existe grande descrepância entre os valores obtidos. Quando realizamos o mesmo comando mas com um valor muito superior (1024) é possivel notar que o tempo de execução aumenta abruptamente quando comparado com os comandos anteriores.

A diferença no tempo de execução do /dev/random e /dev/urandom deve-se ao facto de no segundo caso a geração do numero aleatório ser feito de imediato, pois não é preciso recolher entropia suficiente para gerar a sequência de bytes pseudoaleatórios criptográficamente forte, o que significa, como consequência, menos segurança criptográfica.

### Pergunta P1.2

| Comando | Tempo |
| ------ | ------ |
| head -c 1024 /dev/random \| openssl enc -base64 | 12 ms |
| head -c 1024 /dev/urandom \| openssl enc -base64 | 10 ms |

Após a execução destes comandos (agora com o haveged ativo), podemos constatar uma grande diminuição do tempo de execução. Este descida do tempo de execução deve se ao facto de o haveged recolher entropia a partir de outros processos, acelarando assim a o processo de geração de bytes pseudo aleatorios.

### Pergunta P1.3

1. Apenas gera dígitos e letras pois a função generateSecret(length) do módulo shamirsecret da package eVotUM.Cripto apenas imprime letras no formato ascii (string.ascii\_letters) e dígitos (string.digits) obtendo no resultado final apenas uma seqência de letras e dígitos.

2. Para não limitarmos o output a letras e dígitos, poderiamos alterar a função generateSecret(length) para utilizar algo que permitisse imprimir outros caracteres como, por exemplo, utilizar string.printable em vez de string.ascii\_letters e string.digits. Outra forma seria a utilização de base64 à semelhança das duas primeiras perguntas.

### Pergunta P2.1

##### A

Numa primeira fase foi criada uma diretoria onde se encontra o certificado e a chave privada que foram gerados através dos commandos no enunciado. De seguida foi executado o comando que se segue para dividir o segredo "Agora temos um segredo extremamente confidencial" em 8 partes e que necessite de um quorum de 5 para o reconstruir:

    python createSharedSecret-app.py 8 5 g9 key/mykey.pem

O programa pede a passe da private key (yoda) e o segredo que deseja utilizar.

Para reconstruir o segredo foi necessário executar o seguinte comando:

    python recoverSecretFromComponents-app.py 5 g9 key/mykey.crt

De seguida o programa pede que o utilizador introduza 5 das 8 partes(componentes) geradas
anteriormente, devido ao quorum escolhido (5).

##### B

A diferença entre recoverSecretFromComponents-app.py e recoverSecretFromAllComponents-app.py
é que a primeira apenas precisa de alguns dos intervenientes(quorum), neste exemplo necessita 
das componentes de 5 intervenientes. A segunda função necessita das componentes de 
todos os intervenientes.
Uma utilização do programa recoverSecretFromAllComponents-app.py é por exemplo, quando o nível 
de segurança necessita de ser elevado, requerendo assim o consentimento de todos os intervenientes
que fizeram parte da criação do segredo inicial.

### Pergunta P3.1

#### Método de cifrar

Para cifrar é necessário a função cifra() e o segredo_plaintext.

Numa fase inicial, de forma a garantir a confidencialidade do segredo, é necessário cifra-lo, utilizamos para isso a função cifra dada na API, da seguinte forma:

    segredo_cyphertext = cifra(segredo_plaintext)

Como o cliente pode etiquetar o segredo para saber o que cifrou, podemos concatenar o segredo_cyphertext vindo da função anterior com a etiqueta pretendida do seginte modo:

    new_segredo_cyphertext = segredo_cyphertext + etiqueta

Agora para permitir garantir a integridade e autenticidade, usamos a função dada na API do hmac.
Como a chave de cifra no hardware é alterada e identificada pelos ano, mês e dia utilizamos a 
função de hmac do seguinte modo:

    hmac = hmac(ano.mes.dia,new_segredo_cyphertext)

O resultado final do processo de cifra é o seguinte:

    final = segredo_cyphertext + etiqueta + hmac + ano.mes.dia
    
#### Método de decifrar

No início deste processo recebemos os parâmetros: new_segredo_cyphertext (segredo_cyphertext + etiqueta), o hmac e o ano,mes,dia

Concatenamos a etiqueta recebida com o segredo_cyphertext:

    new_segredo_cyphertext = segredo_cyphertext + etiqueta

Obtemos o hmac dos parâmetros recebidos:

    hmacS = hmac(ano.mes.dia, new_segredo_cyphertext)

Devemos agora comparar este resultado com o hmac original de forma a descobrir se 
o new_segredo_cyphertext sofreu algum tipo de alterações:
    
    if(hmac != hmacS) return error

Se estes forem iguais concluimos então o processo de decifragem utilizando
a seguinte função:

    segredo_plaintext = decifra(segredo_cyphertext, ano.mes.dia)
    
    
### Pergunta P4.1

Utilizando o website https://webgate.ec.europa.eu/tl-browser/#/ e o comando:
    
    openssl x509 -in cert.crt -text -noout
    
Foi possível obter a informação necessária para saber os algoritmos e o tamanho das chaves utilizados nos cretificados das Entidades de Certificação. Devido a sermos o grupo 9, foi necessário identificar estas propriedades para as ECs "Ministry of Defence of Slovenia" e "Republika Slovenija" da Eslovénia:

##### Ministry of Defence of Slovenia

| Algoritmo de Assinatura | Algoritmo de Chave Pública | Tamanho da Chave | Validade|
| ------------ | ------------ | ------------ | ------------ | 
| SHA256 with RSA Encryption | RSA Encryption | 4096 bits | De Feb 7 08:33:07 2014 GMT até Feb 7 09:03:07 2026 GMT |

##### Republika Slovenija 

| Algoritmo de Assinatura | Algoritmo de Chave Pública | Tamanho da Chave | Validade|
| ------------ | ------------ | ------------ | ------------ | 
| SHA256 with RSA Encryption | RSA Encryption | 3072 bits | De Apr 25 07:38:17 2016 GMT até Dec 25 08:08:17 2037 GMT

Segundo o site https://www.keylength.com/ prevê-se que um tamanho de chave de 3072 bits (ou superior) seja seguro durante 
bastante tempo (NIST: 2016-2030 & beyond ECRYPT: 2018-2028) logo ambos os tamanhos de chave bem como os algoritmos utilizados são adequados.