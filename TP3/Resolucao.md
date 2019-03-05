# TP3- Resolução

### Pergunta P1.1

##### 1

Não é possível garantir que fica localizado nos EUA, pois o comando sudo anonsurf start cria uma conexão do IP para a rede TOR, o que permite garantir anonimato mas como consequência nãopermite descobrir a localização.

##### 2

Não é possível pois esta ferramenta pertende garantir o anonimato utilizando o protocolo TOR, encaminhando todo o tráfego para esta rede. Como o comando apenas gera um IP novo para esconder o IP verdadeiro, acaba po ser impossível garantir qual será o novo IP e qual será a localização desse mesmo IP (neste caso EUA).


### Pergunta P1.2

O circuito do site é:

 - This browser
 - France 
 - Switzerland 
 - Germany 
 - Relay
 - Relay
 - Relay
 - zqktlwi4fecvo6ri.onion



São realizados 6 saltos para garantir o anonimato, tanto do utilizador como do servidor. Os três primeiros IPs são conhecidos pois são "escolhidos" pelo utilizador, sendo os outros 3 (os Relays) escolhidos pelo servidor a que estamos a tentar aceder. Estes saltos são necessários de maneira a garantir o anonimato do utilizador para com o servidor, de forma a proteger se a si mesmo e aos seus dados.
