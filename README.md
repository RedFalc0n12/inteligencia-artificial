# inteligencia-artificial
trabalhar com criação de agentes inteligentes

Instale as bibliotecas necessarias:

    pip install -r requerimentos.txt  

Abra o .env e configure:

    OPENAI_API_KEY="" # insira sua chave   
    CAMINHO_PASTA = "./documentos" # uma pasta local, mude para o caminho que desejar (opicional)
    MARKDOWN="false" # mude para true se quiser que o markdown fique como se fosse um html (opicional)
    
Execute:

    python compiler.py

Funcionalidade:

    depois de executar o script abrira um input no terminal
    1. insira o documento que você deseja trabalhar(pode ser uma URL ou um documento local do repositorio que você escolheu ou do ja pre-definido)
    2.faça a sua pergunta
    3. espere alguns segundos e você tera sua resposta 
    4. disponibilizei um arquivo de links_publicos para fazer o teste de URL

Ficha tecnica:
    
    Modelo:escolhi gpt-4.1-nano pelo fato dele ser um pouco mais rapido que o gpt-5-nano e mais barato que gpt-5-mini.
    
    Velocidade: para retornar a resposta da IA testei cada modelo em media umas 6 vezes para saber a velocidade
    {Modelo , Maior T , Menor T}
    {gpt-5-nano , 38s , 17s}
    {gpt-5-mini , 16s , 14.5s}
    {gpt-4.1-nano , 15.5 , 11.5}

    Preço:
    para cada 1M token
    {Model , Input , Cached input , Output}
    {gpt-5-mini , $0.25 , $0.025 , $2.00}
    {gpt-5-nano , $0.05 , $0.005 , $0.40}
    {gpt-4.1-nano , $0.10 , $0.025 , $0.40}

# Estimativa real de custos para análise de PDFs com OpenAI API (Copilot e ChatGPT)

metricas:

    usuario: {"Quais métricas se destacam?","Há tendências relevantes?","Quais recomendações podem ser feitas?"}

    IA:  {"Você é um analisador de documentos. ","Sempre responda em **Markdown válido**, incluindo:\n"
                    ,"priorize o pedido do usuario\n"
                        "- Um título principal (###)\n"
                        "- Listas com marcadores (-)\n"
                        "- Destaques em negrito (**texto**)\n"},


O cálculo considera:

    * Prompt fixo reutilizado
    * Pergunta do usuário
    * Conteúdo do PDF
    * Resposta da IA
    
    ---

# PDF utilizado como referência

    v18n36a08.pdf
    
    O PDF analisado possui aproximadamente:
    
    * 18 páginas
    * Texto acadêmico denso
    * Cerca de 10.000 tokens após extração
    
    ---
    
    # Estrutura da chamada
    
   ## Prompt fixo
    
    ```text
    "Você é um analisador de documentos. Sempre responda em Markdown válido..."
    ```
    
    Estimativa:
    
    * ~40 tokens
    
    ---
    
## Pergunta do usuário
    
    Exemplos:
    
    * "Quais métricas se destacam?"
    * "Há tendências relevantes?"
    * "Quais recomendações podem ser feitas?"
    
    Estimativa:
    
    * ~10 tokens
    
    ---
    
## Conteúdo do PDF
    
    Estimativa média:
    
    * ~10.000 tokens
    
    ---
    
 ## Resposta da IA
    
    Resposta média em Markdown:
    
    * ~200 tokens
    
    ---
    
 # Total estimado por chamada
    
    | Tipo                | Tokens  |
    | ------------------- | ------- |
    | Prompt fixo         | ~40     |
    | Pergunta do usuário | ~10     |
    | Conteúdo do PDF     | ~10.000 |
    | Output da IA        | ~200    |
    | Total aproximado    | ~10.250 |
    
    ---
    
 # Cenário 1 — Enviando o PDF inteiro em todas as perguntas
    
    ## Exemplo
    
    ```text
    Pergunta 1 -> envia PDF inteiro
    Pergunta 2 -> envia PDF inteiro novamente
    Pergunta 3 -> envia PDF inteiro novamente
    ```
    
    Neste cenário, o PDF representa praticamente todo o custo.
    
    ---
    
# Estimativa de custo por chamada
    
    ## GPT-5 Nano
    
    | Componente             | Valor aproximado |
    | ---------------------- | ---------------- |
    | Input (~10.050 tokens) | ~US$0,0005       |
    | Output (~200 tokens)   | ~US$0,00008      |
    | Total por chamada      | ~US$0,00058      |
    
    ---
    
    ## GPT-5 Mini
    
    | Componente             | Valor aproximado |
    | ---------------------- | ---------------- |
    | Input (~10.050 tokens) | ~US$0,0025       |
    | Output (~200 tokens)   | ~US$0,0004       |
    | Total por chamada      | ~US$0,0029       |
    
    ---
    
    ## GPT-4.1 Nano
    
    | Componente             | Valor aproximado |
    | ---------------------- | ---------------- |
    | Input (~10.050 tokens) | ~US$0,0010       |
    | Output (~200 tokens)   | ~US$0,00008      |
    | Total por chamada      | ~US$0,00108      |
    
    ---
    
    # Custo estimado para 3 perguntas
    
    | Modelo       | Custo aproximado |
    | ------------ | ---------------- |
    | GPT-5 Nano   | ~US$0,0017       |
    | GPT-5 Mini   | ~US$0,0087       |
    | GPT-4.1 Nano | ~US$0,0032       |
    
    ---
    
 # Cenário 2 — Arquitetura otimizada (recomendada)
    
    Em vez de enviar o PDF inteiro em cada pergunta:
    
    1. Extrair o texto apenas uma vez
    2. Dividir o conteúdo em chunks
    3. Criar embeddings
    4. Buscar apenas os trechos relevantes
    5. Enviar somente:
    
       * pergunta
       * chunks relevantes
       * prompt
    
    ---
    
# Tokens estimados por pergunta otimizada
    
    | Tipo              | Tokens |
    | ----------------- | ------ |
    | Prompt fixo       | ~40    |
    | Pergunta          | ~10    |
    | Chunks relevantes | ~800   |
    | Output            | ~200   |
    | Total aproximado  | ~1.050 |
    
    ---
    
# Custos estimados com arquitetura otimizada
    
    ## GPT-5 Nano
    
    | Componente        | Valor aproximado |
    | ----------------- | ---------------- |
    | Input             | ~US$0,00005      |
    | Output            | ~US$0,00008      |
    | Total por chamada | ~US$0,00013      |
    
    ---
    
    ## GPT-5 Mini
    
    | Componente        | Valor aproximado |
    | ----------------- | ---------------- |
    | Input             | ~US$0,00025      |
    | Output            | ~US$0,0004       |
    | Total por chamada | ~US$0,00065      |
    
    ---
    
    ## GPT-4.1 Nano
    
    | Componente        | Valor aproximado |
    | ----------------- | ---------------- |
    | Input             | ~US$0,00010      |
    | Output            | ~US$0,00008      |
    | Total por chamada | ~US$0,00018      |
    
    ---
    
    # Comparação final
    
    | Modelo       | PDF inteiro | Arquitetura otimizada |
    | ------------ | ----------- | --------------------- |
    | GPT-5 Nano   | ~US$0,00058 | ~US$0,00013           |
    | GPT-5 Mini   | ~US$0,0029  | ~US$0,00065           |
    | GPT-4.1 Nano | ~US$0,00108 | ~US$0,00018           |
    
    ---
    
# Conclusão
    
    ## Sem otimização
    
    * O PDF representa praticamente todo o custo.
    * Reenviar o documento inteiro em cada pergunta é ineficiente.
    * O histórico da conversa também aumenta os tokens.
    
    ## Com otimização
    
    * O custo pode cair mais de 80%.
    * O sistema fica mais rápido.
    * A qualidade das respostas geralmente melhora.
    * A escalabilidade aumenta significativamente.
    
    ---
    
 # Recomendação
    
    Para aplicações que analisam PDFs:
    
    * usar chunking
    * embeddings
    * busca semântica
    * envio parcial de contexto
    
 é praticamente obrigatório para manter baixo custo e boa performance.

OBS: acredito que a velocidade mude de acordo com a qualidade da maquina, internet, prompt do usuario.
    Estes resultados foram mais para justicar a utilização dos modelos sem me basear apenas nos parametros de preço.
    Cada modelo tem sua devida utilidade, para a tarefa sugerida acredito que escolhi o melhor modelo.
    Se for do seu interesse analise um pouco o arquivo descart.py la esta a minha ideia original que era extrair o texto do PDF e enviar como um prompt, mas depois de pensar um pouco e perguntar ao gpt decidi fazer enviando o arquivo inteiro 
    
