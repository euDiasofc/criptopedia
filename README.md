# CryptoPedia Bot do Telegram

CryptoPedia é um bot do Telegram projetado para fornecer informações em tempo real sobre criptomoedas. Ele oferece uma variedade de funcionalidades, incluindo as 10 principais criptomoedas por capitalização de mercado, as moedas mais negociadas nas últimas 24 horas e 7 dias, informações detalhadas sobre criptomoedas específicas e as últimas notícias relacionadas a criptomoedas.

## Funcionalidades

- **Top 10 Criptomoedas**: Lista as 10 principais criptomoedas por capitalização de mercado.
- **Moedas Mais Negociadas (24h & 7d)**: Fornece as moedas mais negociadas nas últimas 24 horas e nos últimos 7 dias.
- **Informações de Criptomoedas**: Busca informações detalhadas sobre uma criptomoeda específica, incluindo seu preço atual, capitalização de mercado, volume de 24 horas e mais.
- **Notícias de Criptomoedas**: Obtém as últimas notícias relacionadas a uma criptomoeda específica.
- **Menu de Opções**: Oferece um menu de botões inline para facilitar o acesso às funcionalidades do bot.

## Comandos do Bot

- `/start`: Inicia o bot e exibe a mensagem de boas-vindas.
- `/help`: Exibe o menu de ajuda com informações sobre como usar o bot.
- `/top10`: Lista as 10 principais criptomoedas por capitalização de mercado.
- `/moeda <nome/símbolo/ID>`: Fornece informações detalhadas sobre uma criptomoeda específica.
- `/noticias <nome>`: Busca as últimas notícias relacionadas à criptomoeda especificada.
- `/callback`: Exibe botões inline com links de interesse.
- `/menu`: Mostra um menu de botões inline para acessar rapidamente as funcionalidades do bot.

## Configuração

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/cryptopedia-telegram-bot.git
    cd cryptopedia-telegram-bot
    ```

2. Crie um arquivo `.env` com as seguintes variáveis:
    ```env
    api_id=<SEU_API_ID>
    api_hash=<SEU_API_HASH>
    bot_token=<SEU_BOT_TOKEN>
    NEWS_API_KEY=<SEU_NEWS_API_KEY>
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute o bot:
    ```sh
    python bot.py
    ```

## Dependências

- `requests`
- `aiohttp`
- `pycoingecko`
- `python-dotenv`
- `pyrogram`

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

---


