import os
import json
import markdown
from openai import OpenAI
from dotenv import load_dotenv

# Carregar chave da API
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
caminho_pdf = os.getenv("CAMINHO_PASTA", "./documentos") # Caminho padrão se não estiver definido
if caminho_pdf:
    print("\033[0;33m!!! Variável de ambiente CAMINHO_PASTA não definida. Usando caminho padrão !!!\033[m\n\033[1m!!! Coloque seus PDFs na pasta documentos ou defina CAMINHO_PASTA para outro diretório. !!!\033[m")

def dir_leitura(caminho_pdf): # Função para listar arquivos PDF disponíveis
    arquivos = [f for f in os.listdir(caminho_pdf) if f.endswith('.pdf')]
    print("Arquivos PDF disponíveis:")
    for idx, arquivo in enumerate(arquivos):
        print(f"{idx + 1}. {arquivo}")
    return arquivos
dir_leitura(caminho_pdf)

def analisar_documento(nome_pdf, pergunta):
    
    source = "N/A"
    input_file = None

    # Caso seja URL
    if nome_pdf.startswith("http"):
        source = nome_pdf
        input_file = {"type": "input_file", "file_url": nome_pdf}

    # Caso seja arquivo local
    elif nome_pdf and os.path.isfile(os.path.join(caminho_pdf, nome_pdf)):
        caminho_completo = os.path.join(caminho_pdf, nome_pdf)
        source = nome_pdf
        file = client.files.create(
                file=open(caminho_completo, "rb"),
                purpose="user_data"
        )
        input_file = {"type": "input_file", "file_id": file.id}

    else:
        source = "N/A"

    # Monta requisição
    content = [
        {"type": "input_text", "text": f"Documento: {source}\n\nPergunta: {pergunta}"},
    ]
    if input_file:
        content.append(input_file)

    response = client.responses.create(
        model="gpt-4.1-nano",  # escolha justificada no README
        input=[
            {"role": "system",
             "content": "Você é um analisador de documentos. "
                        "Sempre responda em **Markdown válido**, incluindo:\n"
                        "priorize o pedido do usuario\n"
                        "- Um título principal (###)\n"
                        "- Listas com marcadores (-)\n"
                        "- Destaques em negrito (**texto**)\n"},
            {"role": "user", "content": content}
        ]
    )
    print(content)

    conteudo = response.output_text
    if os.getenv("MARKDOWN").lower() == "true":
        conteudo = markdown.markdown(conteudo)
    output = {
        "type": "text",
        "text": conteudo,
        "source": source,
        "suggestions": [
            "Quais métricas se destacam?",
            "Há tendências relevantes?",
            "Quais recomendações podem ser feitas?"
        ]
    }

    return json.dumps(output, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    nome_pdf = "Atividade plano de ação (2).pdf"
    pergunta = "o que diz este documento?"
    print(analisar_documento(nome_pdf, pergunta))


