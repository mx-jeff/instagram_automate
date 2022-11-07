# instagram follwer

## todo

- [x] download enviroment
    - [x] setup the credentials
    - [x] start tests

- [ ] instapy way
    - [x] login in the instagram
    - [x] load page
    - [ERROR] Due for recent changes in instagram api, instapay its offfile
    - [ ] unblock the target account
    - [ ] select the target account
        - [ ] follow the last XX profile of it
    - [ ] block the target user

- [ ] instagram selenium way
    - [x] login in the instagram
    - [x] load page
    - [x] set browser profile
    - [x] select the target account
    - [x] follow the last XX profile of it
        - limite to 40 profiles
        - aumentar o tempo de espera
    - [x] print logs
    - [x] update library: scrapper-boilerplate
    - [x] update test
    - [x] unblock the target account
    - [x] block the target user
    - [x] save the followed users on database or file
    - [ ] unfollow
        - [ ] unfollow directly in main accounte instead to collect profiles
    - [ ] view proxies to avoid block
    - [ ] bluestacks

- [ ] edit params:
    - [ ] add login on csv
    - [ ] QUANTIDADE_DE_CONTAS: 2
    - [ ] QUANTIDADES_DE_CONTAS_SEGUIDAS: 30
    - [ ] HORARIOS_DE_FUNCIONAMENTO: 20:30:csv
    - [ ] TEMPO_SEGUINDO: 3 horas

Olá gustavo, tudo bem?

Verifiquei aqui é possível dar prosseguimento com o os requisitos definidos, embora com algumas limitações tais como:

- tem um limite para segui diário a partir de 45 pessoas, alem disso, o instagram consta como comportamente dúvidoso, alem de bloquear o acesso por 1 hora
    - podemos aumentar o tempo de espera randomicamente, através do dia
    - se for muito rápido a chance de ser bloqueado é alta

- com o prazo de até 5 dias (desenvolvimento), se aprovado subimos na vps
- preço da assinatura $95 ao mês (desenvolvimento + manutenção) podendo ser, cartão, pix

link do plano: https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c938084808477b601808535deeb0079

Assim que aprovado o prazo e pagamento, podemos dar início ao desenvolvimento do mesmo

Dúvidas á disposição

Att.

----

Olá Gustavo, tudo bem?

Como mencionado antes, o projeto consiste em programa (bot) do instagram faça as seguintes funções:

- desbloquear usuário alvo
- seguir número x de seguidores do memso
- esperar x tempo
- parar de seguir os mesmos
- bloquear o usuário

sendo esse ditos acima possíveis

Constatei que existe um bloqueio podendo ser:
    - rate limit de seguir por hora/dia (sendo 40 o limite de seguir/deseguir o usuários)
    - sendo assim adicionar uma espera de tempo consideravel entre cada ação
    - simular um usuário real nos perfis

tambem podemos usuar vpn/proxy para evitar banimentos (se necessário futuramente / custos adicionais) se possível usar multiplas contas em sequências

assim que validade e aprovado, podendo subir em uma vps para o mesmo (custos váriam)

Sendo de:
    - prazo: 5 dias úteis (desenvolvimento + testagem), posterior colocar na vps
    - preço: $1.140 (com as taxas do 99freela inclusa)

agora pendente:
    - fazer o arquivo de configuração do mesmo
    - juntar as funcionalidades
    - realizar a testagem do mesmo

tenho disponibilidade de inciar a partir de segunda-feira (07/11) (te avisarei ao início)

Dúvidas estou á disposição

Att.