# TP2- Resolução

### Pergunta P1.1

Inicialmente para resolver esta pergunta foi necessário gerar um par de chaves e o respetivo certificado, utilizando o OpenSSL, através dos seguintes comandos:

#### Key

    openssl ecparam -name prime256v1 -genkey -noout -out key.pem
   
#### Certificado
    openssl req -key key.pem -new -x509 -days 365 -out key.crt

De forma a simplificar o input e output, foi alterado o código fornecido para a experiência 1.2 . Este código encontra-se na seguinte pasta:

[Código](https://github.com/uminho-miei-engseg-18-19/Grupo9/tree/master/TP2/P1/)

### Pergunta P2.1

#### 1

Os três sites escolhidos para analisar utilizando o SSL Server test foram o Argentena Bank, banco belga, o Banco Nacional Checo (BNC), banco checo, e o Alpha Bank , banco grego. 
Tanto o Argentena Bank como o BNC têm classificação de A, sendo por isso bastante seguros ao contrário do Alpha Bank que possui um rating de F.

1. Argentena Bank
[Resultados](https://github.com/uminho-miei-engseg-18-19/Grupo9/tree/master/TP2/P2/SSLServer/argentenaBank.pdf)

2. BNC
[Resultados](https://github.com/uminho-miei-engseg-18-19/Grupo9/tree/master/TP2/P2/SSLServer/bancoNacionalCheco.pdf)

3. Alpha Bank
[Resultados](https://github.com/uminho-miei-engseg-18-19/Grupo9/tree/master/TP2/P2/SSLServer/alphaBank.pdf)

#### 2- Analise o resultado do SSL Server test relativo ao site escolhido com pior rating. Que comentários pode fazer sobre a sua segurança. Porquê?

O site menos seguro é claramente o site do Alpha Bank, isto deve-se a este site ser bastante vulnerável ao ataque ROBOT(Return Of Bleichencacher's Oracle Threat). Isto acontece porque o servidor apenas suporta trocas de chaves de encriptação RSA e consiste num invasor que pode gravar passivamente o tráfego podendo desencriptá-lo mais tarde. 
Além disso o servidor não conta com o forward secrecy, correndo o risco das chaves serem comprometidas.
Este servidor está bastante exposto a ataques man-in-the-middle por exemplo.

#### 3- É natural que tenha reparado na seguinte informação: "Heartbleed (vulnerability)" na secção de detalhe do protocolo. O que significa, para efeitos práticos?

A vulnerabilidade Heartbleed consiste no atacante enganar o servidor de forma a este libertar um pedaço de memória. Em termos práticos o atacante pode obter informação sensível como chaves privadas para encriptação, comprometendo assim a segurança do servidor.

### Pergunta P3.1

De forma a escolhermos dois servidores ssh de empresas comerciais em Londres (devido a sermos o Grupo9) foi necessário
utilizar o site shodan.io e realizar a seguinte pesquisa:

    port:22 country:gb
    
A partir dos resultados foram escolhidos os servidores que se seguem assim como a versao do software e versao utilizada pelos servidores ssh.

| Servidor | Empresa | Software | Versão |
| -------- | -------- | -------- | -------- |
| 178.62.217.182 | Digital Ocean | OpenSSH | 7.2p2 |
| 18.139.6.106 | Amazon | OpenSSH | 7.6p1 |

Utilizando o ssh-audit obtivemos os seguintes resultados:

1. Digital Ocean
[Resultados](https://github.com/uminho-miei-engseg-18-19/Grupo9/tree/master/TP2/P3/digocean.md)

2. Amazon
[Resultados](https://github.com/uminho-miei-engseg-18-19/Grupo9/tree/master/TP2/P3/amazon.md)

A seguir procedeu-se à análise das vulnerabilidades existentes nas versões de software de ambos os servidores escolhidos.

##### 3- Qual dessas versões de software tem mais vulnerabilidades?

Utilizando o site CVE Details foi possível observar que a versão do OpenSSH 7.2p2 contem mais vulnerabilidades possuindo 7 vulnerabilidades ao contrário da versão OpenSSH 7.6p1 que apenas possui 2 vulnerabilidades.

##### 4- Qual tem a vulnerabilidade mais grave (de acordo com o CVSS score identificado no CVE details)?

A vulnerabilidade mais grave é do software com a versão do OpenSSH 7.2p2 que possui uma vulnerabilidade com CVSS score 7.8 com designação CVE-2016-6515

##### 5- Para efeitos práticos, a vulnerabilidade indicada no ponto anterior é grave? Porquê?

Em termos práticos à vulnerabilidade é bastante grave. A vulnerabilidade consiste em não limitar o tamanho da password para autenticação de passwords na função auth_password no ficheiro aut_passwd.c em sshd. Isto permite que um atacante remoto cause um denial of service(crypt CPU consumption) através de uma string longa.
