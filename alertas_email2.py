import smtplib
from email.message import EmailMessage

def enviar_alerta_email(asunto, mensaje, to_email):
    email_address = "alertatradingbtc15@gmail.com"       # Tu dirección Gmail
    email_password = "123456781234567812345678" # Usa una contraseña de aplicación si tienes 2FA

    msg = EmailMessage()
    msg['Subject'] = asunto
    msg['From'] = email_address
    msg['To'] = to_email
    msg.set_content(mensaje)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
