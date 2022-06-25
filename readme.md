# INSTAGRAM AUTOMATE

---

Bot que automatiza o uso do Instagram. conta com as seguintes funções:

- [ ] seguir usuários
- [ ] deixar de seguir usuários
- [ ] bloquear usuários
- [ ] desbloquear usuários

---

## Modo de uso

recomendado possuir python instalado, se não possuir [instale o python](https://www.python.org/downloads/)

(Opcional) criar um ambiente de desenvolvimente, rodeos seguintes comandos:

```
python3 -m venv venv
source venv/bin/activate (se estiver no linux/ou VPS)
.\venv\scripts\activate (se estiver no windows)
```

Será iniciado o ambiente de desenvolvimento.

# instalar as dependencias

Para o projeto funcionar corretamente é necessário instalar as seguintes dependencias:

```
pip install -r requirements.txt
```

# configurações

em ".env.example", possui os exemplos de configuração do bot para ser usado.

crie o arquivo ".env", copie os exemplos e altere os valores.

valores:

- INSTAGRAM_USER: seu usuario do instagram
- INSTAGRAM_PASSWORD: sua senha do instagram
- HEADLESS: se o bot deve ser executado em modo headless (sem abrir a janela do navegador) (True:sim/False:nao)
- INSTAGRAM_NICKNAME: nome do perfil para o bot seguir
- LOGIN_SAVE: se o bot deve salvar o login do usuario (True:sim/False:nao) 


# rodar o projeto

instalado o projeto, é possível iniciar o bot com o comando:

```
python3 main.py
```

Erros ou dúvidas pode me contatar por este mesmo perfil.