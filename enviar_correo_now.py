###################################################################################################################

# Creado por: Pedro Montoya

###################################################################################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo():
    # Configurar los datos del correo electrónico
    remitente = "ejemplo@ejemplo.com"   # Correo del remitente
    destinatario = "ejemplo@ejemplo.com"    # Correo del destinatario
    asunto = ""     # Asunto del mensaje
    mensaje = ""    # Contenido del mensaje

    # Configurar el servidor SMTP de Gmail
    servidor_smtp = "smtp.gmail.com"
    puerto = 587    # Puerto por defecto usado por SMTP
    usuario = "ejemplo@ejemplo.com"   # Correo de tu usuario
    contraseña = ""     # Clave usada por el usuario para el SMTP (Contraseña de aplicación)

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(mensaje, 'plain'))

    # Iniciar sesión en el servidor SMTP y enviar el correo electrónico
    try:
        server = smtplib.SMTP(servidor_smtp, puerto)
        server.starttls()
        server.login(usuario, contraseña)
        texto = msg.as_string()
        server.sendmail(remitente, destinatario, texto)
        print("Correo enviado correctamente")
    except Exception as e:
        print("Error al enviar el correo:", e)
    finally:
        server.quit()

# Llamar a la función para enviar el correo electrónico
enviar_correo()
