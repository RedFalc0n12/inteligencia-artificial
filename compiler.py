import os
import Script 

print("Utilize nosso agente para analisar seu documento")
caminho_pdf = os.getenv("CAMINHO_PASTA")  # Caminho padrão se não estiver definido 
caminho_padrao = "./"  # Caminho padrão se não estiver definido 
if not caminho_pdf:
    caminho_pdf = caminho_padrao
    
nome_pdf = input("Qual o nome do documento? ").strip() 
pergunta = input("Qual sua requisição? ").strip()

resultado = Script.analisar_documento(f"{nome_pdf}", pergunta)
print(resultado)
    