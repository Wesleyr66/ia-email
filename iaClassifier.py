import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def classify_email_with_ai(content):
    """Classifica o tipo de e-mail com IA usando o OpenAI GPT"""
    if content is None:
        return "Nenhum conteúdo para classificar"
    
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Classifique este e-mail em uma das seguintes categorias: 'Segurança', 'Promoção', 'Notificação', 'Outros'. E-mail: {content}",
            max_tokens=100,
            temperature=0.7
        )

        classification = response.choices[0].text.strip()
        return classification

    except Exception as e:
        print(f"Erro ao classificar o e-mail com IA: {e}")
        return "Erro na classificação"
3