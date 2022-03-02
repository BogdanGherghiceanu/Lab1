import smtplib
import random

def sendMail(email_to, jsonAnaf, prodString):
    # print(prodString)
    print("LOG MAILAPITrimit status comanda catre:" + email_to)
    email_address = email_to  # add email address here
    email_address_from = 'ccapptest@yahoo.com'
    Subject = f'Subject: Confirmare comanda nr{random.randint(10000,100000)}...\n\n'
    content = 'Salut!\n' \
              'Confirmam comanda pentru firma:\n' \
              f'Nume:{jsonAnaf["denumire"]}\n' \
              f'CUI:{jsonAnaf["cui"]}\n' \
            f'Nr registru comertului:{jsonAnaf["nrRegCom"]}\n' \
              f'Platitor de TVA:{jsonAnaf["scpTVA"]}\n' \
            'Comanda contine urmatoarele produse:\n'+prodString+ \
              '\nVa multumim pentru comanda' \
              ' \n\n '
    # print(content)
    footer = 'v1'  # add test footer
    passcode = 'qtczmdhghiaadaxf'  # add passcode here
    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    conn.ehlo()
    conn.login(email_address_from, passcode)
    print(conn.sendmail(email_address_from,
                  email_address,
                  Subject + content + footer))

    conn.quit()

def sendMailLipsaFirma(email_to, cui):
    print("LOG MAILAPITrimit status comanda catre:" + email_to)
    email_address = email_to  # add email address here
    email_address_from = 'ccapptest@yahoo.com'
    Subject = 'Subject: Eroare comanda...\n\n'
    content = 'Salut!\n' \
              f'Cui-ul {str(cui)} firmei este invalid:\n' \
              'Va multumim ' \
              ' \n\n '
    footer = 'da'  # add test footer
    passcode = 'qtczmdhghiaadaxf'  # add passcode here
    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    conn.ehlo()
    conn.login(email_address_from, passcode)
    print(conn.sendmail(email_address_from,
                  email_address,
                  Subject + content + footer))
    conn.quit()
def sendMailTVAFalse(email_to, jsonAnaf):
    print("LOG MAILAPITrimit status comanda catre:" + email_to)
    email_address = email_to  # add email address here
    email_address_from = 'ccapptest@yahoo.com'
    Subject = 'Subject: Comanda respinsa...\n\n'
    content = 'Salut!\n' \
              'Societatea:\n' \
              f'Nume:{jsonAnaf["denumire"]}\n' \
              f'CUI:{jsonAnaf["cui"]}\n' \
            f'Nr registru comertului:{jsonAnaf["nrRegCom"]}\n' \
              f'Platitor de TVA:{jsonAnaf["scpTVA"]}\n' \
                'Nu este platitoare de TVA si nu poate efectua comenzi de la noi\n' \
              'Va multumim' \
              ' \n\n '
    footer = 'da'  # add test footer
    passcode = 'qtczmdhghiaadaxf'  # add passcode here
    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    conn.ehlo()
    conn.login(email_address_from, passcode)
    print(conn.sendmail(email_address_from,
                  email_address,
                  Subject + content + footer))
    conn.quit()