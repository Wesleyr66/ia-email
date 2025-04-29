import imaplib
import email
from iaClassifier import classify_email_with_ai  # Importa a função de classificação
from config import EMAIL, SENHA

def get_latest_email_text():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, SENHA)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()
        if not email_ids:
            print("Caixa de entrada vazia.")
            return None

        latest_email_id = email_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                email_content = part.get_payload(decode=True).decode()
                print(f"📨 Texto bruto do último e-mail:\n{email_content}")
                return email_content
        
        print("Nenhum conteúdo de texto encontrado no e-mail.")
        return None

    except Exception as e:
        print("Erro ao ler o e-mail:", e)
        return None

def classify_latest_email():
    email_content = get_latest_email_text()
    if email_content:
        classification = classify_email_with_ai(email_content)
        print("🤖 Classificação do e-mail pela IA:", classification)
    else:
        print("Não foi possível classificar o e-mail.")
