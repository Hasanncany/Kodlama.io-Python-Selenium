import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime

def send_email():

    # Resmi Gazete'nin web sitesindeki adres
    url = "https://www.resmigazete.gov.tr/"

    # Resmi Gazete'nin yayınlanacağı tarih
    date = datetime.datetime.now().strftime("%Y%m%d")

    try:
        # E-posta mesajının oluşturulması
        mesaj = MIMEMultipart()
        mesaj['Subject'] = "Resmi Gazete - " + date
        mesaj['From'] = "hassncan.yildirim21@gmail.com"
        mesaj['To'] = "dilekkomy@gmail.com"

        # Resmi Gazete'nin PDF formatında indirilmesi
        # pdf = url + "gazete_oku_" + date + ".pdf"
        # response = requests.get(pdf)
        response = requests.get("https://www.resmigazete.gov.tr/202203/20220307-1.pdf")
        with open(date + ".pdf", 'wb') as f:
            f.write(response.content)

        # E-posta mesajına PDF dosyasının eklenmesi
        with open(date + ".pdf", 'rb') as f:
            attach = MIMEApplication(f.read(),_subtype="pdf")
            attach.add_header('Content-Disposition','attachment',filename=str(date)+".pdf")
            mesaj.attach(attach)

        # SMTP sunucusuna bağlanarak e-posta gönderimi yapılması
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.starttls()
        mail.login("hassncan.yildirim21@gmail.com" , "gyhrmijswbdzoeto")

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        mail.quit()
        print("E-posta gönderimi başarılı.")
    except Exception as e:
        print("Hata oluştu: ", e)

send_email()
