# inteligencia-artificial
trabalhar com criação de agentes inteligentes

instale as bibliotecas necessarias
    pip install -r requerimentos.txt  

abra o .env e configure
    OPENAI_API_KEY="" # insira sua chave   
    CAMINHO_PASTA = "./documentos" # uma pasta local como mude para o caminho que desejar (opicional)
    MARKDOWN="false" # mude para true se quiser que o markdown fique como se fosse um html (opicional)
    
execute
    python compiler.py

funcionalidade 
    depois de executar o script abrira um input no terminal
    1. insira o documento que você deseja trabalhar(pode ser uma URL ou um documento local do repositorio que você escolheu ou do ja pre-definido)
    2.faça a sua pergunta
    3. espere alguns segundos e você tera sua resposta 
    4. disponibilizei um arquivo de links_publicos para fazer o teste de URL

ficha tecnica
    Modelo: escolhi gpt-4.1-nano pelo fato dele ser um pouco mais rapido que o gpt-5-nano e mais barato que gpt-5-mini.

    velocidade: para retornar a resposta da IA testei cada modelo em media umas 6 vezes para saber a velocidade
    {Modelo , Maior T , Menor T}
    {gpt-5-nano , 38s , 17s}
    {gpt-5-mini , 16s , 14.5s}
    {gpt-4.1-nano , 15.5 , 11.5}

    Preço:
    {Model , Input , Cached input , Output}
    {gpt-5-mini , $0.25 , $0.025 , $2.00}
    {gpt-5-nano , $0.05 , $0.005 , $0.40}
    {gpt-4.1-nano , $0.10 , $0.025 , $0.40}
    OBS: acredito que a velocidade mude de acordo com a qualidade da maquina, internet, prompt do usuario. estes resultados foram mais para justicar a utilização dos modelos sem me basear apenas nos parametros de preço, e cada modelo tem sua devida utilidade, para a tarefa sugerida agredito que escolhi o melhor modelo.
    