import smtplib
from email.mime.text import MIMEText
import time
import os

os.system("bash fx.sh")
print ("WELCOME ANONYMOUS SAVE YOUR TARGET !")
EMAIL = "dyrothmvp98@gmail.com"
PASSWORD = "‎wdix mqoo kvbf ebbb"
TO_EMAIL = "support@support.whatsapp.com"

# Minta nomor WA dari terminal
nomor = input("This is UNBANNED With WhyNFX !(example: 62xxxxx): ")

SUBJECT = ""
BODY = """ola desenvolvedor do whatsapp para desativar a conta do whatsapp de alguem por ter vendido itens proibidos em forma de drogas no aplicativo whatsapp, peço a desativação da conta do whatsapp dessa pessoa para diminuir o número de vendas de itens proibidos, e para não prejudicar a nação e a geração do estado, peço ajuda a Mark Zuckerberg e aos desenvolvedores do whatsapp,

o número do whatsapp do vendedor de itens proibidos é {nomor}, obrigado a Mark Zuckerberg e ao desenvolvedor do whatsapp por me"""

JUMLAH_KIRIM = 100
DELAY = 6

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(EMAIL, PASSWORD)

for i in range(JUMLAH_KIRIM):
    msg = MIMEText(BODY)
    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    
    server.send_message(msg)
    print(f"[{i+1}] Hey Kids,This is fun {nomor}")
    time.sleep(DELAY)

server.quit()
print("Succesfully, estimated....")
