 
# TP4- Resolução

### Pergunta P1.1

##### Regulamento (UE) 2016/679 (RGPD) - Artigo 5º

 Este artigo retrata os princípios relativos ao tratamento de dados pessoais, onde são definidas regras para a seleção de recolha dos dados. Desta maneira, são definidos seis pontos essenciais:

    1. licitude, lealdade e transparência
    2. limitação das finalidades
    3. minimização dos dados 
    4. exatidão
    5. limitação da conservação
    6. integridade e confidencialidade 

   De modo a integrar este artigo com a questão de desenvolvimento de software é necessário, primeiramente, compreender do que se tratam os pontos referidos. Sendo assim, é de realçar o facto de que o tratamento de dados de um titular tem de ser feito de maneira transparente e recolhido para finalidades explícitas, sendo proibida a utilização da informação para tratamento posterior ou com fins diferentes dos iniciais, a não ser que estejamos perante casos de arquivo público, fins de investigação científica ou estatísticos. Ao mesmo tempo, também está definido que a informação recolhida tem de ser sucinta e concreta para responder apenas ao necessário, denotando que deve estar sempre exata e atualizada e, em caso contrário, deve ser dado o direito de retificação, ao titular da mesma. Por fim, este regulamento garante, não só, a conservação dos dados apenas durante o período necessário de tratamento, como também a integridade e confidencialidade dos dados na medida em que salvaguarda a proteção contra o tratamento não autorizado e outras atividades ilícitas.
   Depois de analisar este artigo conseguimos perceber a importância do mesmo para a definição de princípios de tratamento/armazenamento da informação aquando do desenvolvimento de software. Desta maneira, é importante que um sistema permita a um utilizador realizar funcionalidades básicas como a alteração/atualização da informação existente sobre ele. Ao mesmo tempo, só devem ser guardados, no sistema, dados estritamente necessários por um período bem definido e, o software deve garantir a segurança dos mesmos, podendo os detentores serem penalizados caso haja algum tipo de fuga de informação pessoal de um cliente.




### Pergunta P1.2

#### ENISA -  Data protection by default in practice

No âmbito do tema do RGPD foi analisado um documento que retrata alguma documentação sobre o desenvolvimento de software adaptado a este regulamento.
Desta maneira, foram identificados 4 critérios fundamentais:
    
    1. Minimização das quantidades de dados 
    2. Minimização do processamento dos dados pessoais
    3. Minimização do período de armazenamento dos dados pessoais
    4. Minimização da acessibilidade dos dados pessoais

O primeiro trata-se da mais óbvia prática no que toca ao tratamento de informação pessoal defendendo, não só, a diminuição do número de campos como, também, o ajuste da granularidade dos dados, processando apenas os estritamente necessários. Tudo isto através do uso de tecnologias tais como a pseudo-anonimização dos dados, uso de encriptação ou outras baseadas em zero knowledge proof. 
Quanto ao processamento dos dados, quanto menor, melhor. Isto é, ao nível da memória utilizada seria preferível o armazenamento dos dados na memória principal se isto fosse suficiente para o propósito. Em conjunto com esta ideia entra a de minimizar o período de depósito da informação, pois, muitas vezes, esta fica guardada mesmo quando já não é necessária.
Em termos de acessibilidade, poder-se-ia restringir o acesso com base na necessidade ao distribuir a informação por diferentes servidores/bases de dados ou até limitar as maneiras de partilhar a mesma. Ao invés de ter informação pessoal pública, à partida, dá-se, ao utilizador, o direito de escolher quais os dados que podem ser partilhados.
Por último, o documento retrata certos padrões essenciais que devem ser seguidos de maneira a termos um sistema user-friendly que respeita a privacidade da informação, por default. Na atualidade é normal que o design de uma aplicação leve um utilizador a fazer escolhas que o desviem dos padrões de privacidade. Desta maneira, é importante desenvolver sistemas que tenham isto em atenção sem dificultar o acesso aos mesmos.



### Pergunta P1.3

#### P1.3.1

De forma a avaliar se o processamento de dados pessoais irá resultar num risco elevado são usados os seguintes nove critérios:

    1. Evaluation or scoring - quando se pode prever determinados aspectos da vida do utilizador através dos seus dados pessoais;

    2. Automated-decision making with legal or similar significant effect - decisões automáticas que podem ter efeitos legais;

    3. Systematic monitoring - dados recolhidos por monitorização automática onde as pessoas observadas podem não estar conscientes desse processo;

    4. Sensitive data or data of a highly personal nature - processamento de dados pessoais como convicções políticas ou registos médicos;

    5. Data processed on a large scale- O RGPD não define o que constitui larga escala. Apesar de isso o WP29 recomenda que se sigam os seguintes fatores quando é necessário determinar se o processo é feito em larga escala: 

    a) O número de utilizadores
    b) O volume de dados
    c) A duração da atividade de processamento
    d) A extensão geográfica da atividade de processamento

    6. Matching or combining datasets - originar/prever dados através de dados previamente processados

    7. Data concerning vulnerable data subjects- A entidade responsável pelo processamento de dados deve ter em consideração utilizadores considerados vulneráveis (crianças, idosos, trabalhadores...), sendo que este processamento deve sempre ser feito com o consentimento destes ou de alguém que os represente. 

    8. Innovative use or applying new technological or organisational solutions- O uso de tecnologias novas tais como a combinação de impressões digitais com reconhecimento facial pode tornar necessário um DPIA. Isto deve-se à forma como são recolhidos os dados sendo que estes podem representar grandes riscos para os utilizadores em termos de direitos e liberdades.

    9. Preventing data subjects from exercising a right or using a service or a contract- Inclui operações de processamento que têm como objetivo permitir, modificar ou recusar os utilizadores a aceder a um serviço ou entrada num contrato. 



#### Pergunta P1.3.2

Imaginemos uma aplicação que utilize os dados geográficos do utilizador para encontrar a melhor rota para um certo local(como por exemplo o Google Maps). Devido a possuirmos a localização atual do utilizador devemos ter imenso cuidado como a guardamos já que estes são dados bastante sensíveis. O utilizador se consentir em deixar a aplicação usar os seus dados geográficos receberá sugestões de outras localizações parecidas ao que já visitou, sugestões de rotas alternativas no caso da existência de trânsito, entre outras funcionalidades.
O processamento de dados do utilizador satisfaz assim os seguintes critérios:

    Evaluation or scoring - prever locais de interesse do utilizador (1)
    Systematic monitoring - monitorização sistemática dos dados  (3)
    Sensitive data or data of a highly personal nature - processamento de dados considerados sensíveis e de carácter pessoal (4)

#### Pergunta P1.3.3

DPIA [preenchido](https://github.com/uminho-miei-engseg-18-19/Grupo9/tree/master/TP4/dpia.pdf)

### Pergunta P1.4

PIA [preenchido](https://github.com/uminho-miei-engseg-18-19/Grupo9/tree/master/TP4/pia.pdf)
