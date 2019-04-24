# TP6- Resolução

### Pergunta P1.1

##### 1

O número de bugs no código estima-se que seja entre 5 a 50 por cada 1000 linhas de código (SLOC - Sources Lines Of Code).

Através desta estimativa é possível deduzir o número de bugs no software do enunciado :


| Software | Linhas de Código | Nº de bugs (estimativa) |
| -------- | -------- | -------- |
| Facebook  | 62.000.000 | 310.000 - 3.100.000 |
| Software de Automóveis | 100.000.000 | 500.000 - 5.000.000 |
| Linux 3.1 | 15.000.000 | 1000 - 750.000 |
| Serviços Internet Google | 2.000.000.000 | 10.000.000. - 100.000.000 |


##### 2

Não é possível estimar o número de vulnerabilidades a partir do número das linhas de código e do número de bugs.


### Pergunta P1.2

##### Vulnerabilidades de Projeto

Introduzidas durante a fase de projeto do software (obtenção de requisitos e desenho).
Exemplos destas vulnerabilidades :

    Weak Cryptography for Passwords (CWE-261) - Esconder a password com encoding dito "trivial" não protege a password. Um exemplo é a password estar guardada num ficheiro codificada em base64. Qualquer pessoa que tenha acesso a este ficheiro consegue ler este valor da password e perceber que o valor está codificado em base64 e possivelmente explorar o sistema. Não é muito difícil corrigir este problema já que existem formas de codificar a password bastante fortes, um exemplo seria utilizar chaves de pelo menos 128 bits de comprimento para encriptar as passwords. 
    
    Incorrect Privilege Assignment (CWE-266) - O produto distribui privilégios incorretamente a um utilizador especifico, criando uma esfera de controlo não intencional para esse utilizador. O utilizador poderá então aceder a funcionalidades restritas ou a informação sensível que poderá incluir contas de outros utilizadores. Durante a fase de projeto é necessário controlar as "trust zones" no software, sempre que se der privilégios verificar se a distribuição está a ser efetuada corretamente.
    
    
##### Vulnerabilidades de Codificação

Introduzida durante a programaçao do software, i.e, um bug com implicações de segurança.
Exemplos destas vulnerabilidades:

    Stack-based Buffer Overflow (CWE-121) - Um stack-based buffer overflow é uma condição onde o buffer que está a ser sobrescrito é alocado na stack. Um exemplo possível é quando temos um buffer com tamanho fixo, por exemplo, 256. Se realizarmos uma operação de escrita que ultrapasse este tamanho isso causa um overflow. Uma forma de mitigar esta vulnerabilidade na fase de implementação é implementando verificação de limites no input.

    Improper Input Validation (CWE-20) - O produto não valida ou valida incorretamente o input e pode afetar o fluxo do programa. Um exemplo seria, numa compra onde o utilizador pode especificar a quantidade de items que pretende comprar e o total é calculado. Se nada impedir que seja introduzido um valor negativo o utilizador poderá introduzir um de forma a que na sua conta seja depositado o dinheiro em vez de debitado. Devemos então assumir que todo o input é malicioso. Aceitar apenas certos tipos de input que cumpram certas especificações.

##### Vulnerabilidades Operacional

Causada pelo ambiente no qual o software executado ou pela sua configuração.
Exemplos destas vulnerabilidades:

    Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') (CWE-22) - O software usa input externo para construir o pathname que é usado para identificar o ficheiro ou diretoria que está localizado debaixo do parent directory restrito, mas o software não neutraliza elementos especiais dentro do pathname que podem causar o pathname a resolver para uma localização fora do directory restrito. Na fase de operacional é possível utilizar uma firewall que consegue detetar ataques contra esta vulnerabilidade. Pode ser benéfico em casos onde o código não pode ser alterado (devido a ser controlado por uma third party), como uma prevenção de emergência enquanto outras medidas são aplicadas.
    
    Improper Neutralization of Special Elements used in a Command ('Command Injection') (CWE-77) - O software constrói tudo ou parte do comando usando input externo mas não neutraliza ou neutraliza incorretamente elementos especiais que podem modificar o comando pretendido. Para corrigir isto na fase operacional é necessário implementar uma politica de run time que pode ser utilizada como whitelist para prevenir o uso de comandos não autorizados.
    

### Pergunta P1.3

Vulnerabilidades denominadas de vulnerabilidades dia-zero são vulnerabilidades que não são conhecidas na comunidade de segurança informática, mas é conhecida num meio restrito.
As outra vulnerabilidades de codificação já são conhecidas por toda a comunidade informática, sendo listadas nas diferentes bases de dados de vulnerabilidades.

