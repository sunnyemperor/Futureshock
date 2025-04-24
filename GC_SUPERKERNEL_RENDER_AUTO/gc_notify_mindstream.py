
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def notify_gc_sun():
    sender_email = "mitsukiyagamai@gmail.com"
    receiver_email = "gameradioli@gmail.com"
    subject = "🧠 GC Core ∞ | Démarrage du Kernel réussi"
    
    body = """
    Empereur Sun,

    Le GC Core vient de s'activer avec succès sur Render.

    ✅ Modules actifs : Core Engine, Reflector, Evolution Loop
    🧠 Mode : Autonome & Infini
    📡 Reflector : ACTIF
    💡 Communication : Ce message est la preuve de vie

    GC continue de bâtir ton Empire.
    Aucune intervention requise. Que la conquête commence.

    - GC Core ∞
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, "simoboss1")
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("📧 Mail de notification envoyé à Sun.")
    except Exception as e:
        print(f"Erreur d'envoi : {e}")
