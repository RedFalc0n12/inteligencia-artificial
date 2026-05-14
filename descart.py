""" aqui vamos armazenar o codigo completo inicial inclusivel com o resquicio do codigo inicial """

""" a ideia inicial era usar o pdfplumber para extrair o texto do PDF e enviar o texto para o modelo, mas isso tem limitações de tamanho. Então, a abordagem atual é enviar o PDF como um arquivo para o modelo, usando a funcionalidade de input_file da API. O modelo pode então processar o arquivo diretamente, o que é mais eficiente e permite lidar com documentos maiores. """

import os
import json
import pdfplumber
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

""" def ler_pdf(nome_pdf): # Função para ler o conteúdo do PDF
    texto = ""
    with pdfplumber.open(f"{caminho_pdf}/{nome_pdf}") as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text() + "\n"
    #print(texto)
    return texto """

def analisar_documento(nome_pdf, pergunta):
    """ # Se o usuário não informar documento, não tenta abrir PDF
    if not nome_pdf or not os.path.exists(f"{caminho_pdf}/{nome_pdf}"):
        texto = "Nenhum documento fornecido."
        source = "N/A"
    else:
        texto = ler_pdf(nome_pdf)
        source = os.path.basename(nome_pdf) """
    
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
        model="gpt-4.1-mini",  # escolha justificada no README
        input=[
            {"role": "system",
             "content": "Você é um analisador de documentos. "
                        "Sempre responda em **Markdown válido**, incluindo:\n"
                        "- Um título principal (###)\n"
                        "- Listas com marcadores (-)\n"
                        "- Destaques em negrito (**texto**)\n"},
            {"role": "user", "content": content}
        ]
    )
    print(content)





    """ resposta = client.chat.completions.create(
        model="gpt-4.1-mini",  # escolha justificada no README
        messages=[
            {"role": "system",
            "content": 
                "Você é um analisador de documentos. "
                "priorize o que o usuario esta pedindo, mas se for relevante, inclua insights adicionais do documento. \n"
                "Sempre responda em **Markdown válido**, incluindo:\n"
                "- Um título principal (###)\n"
                "- Listas com marcadores (-)\n"
                "- Destaques em negrito (**texto**)\n"
            },


            {"role": "user",
            "content": 
                f"Documento:\n{texto}\n\nPergunta: {pergunta}"
            },
            
        ]
        
    ) """



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


