import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


def send_email(name, registration_number, attachment_filename):
    # Construct the recipient's email address
    rec = f"{name}.{registration_number}@muj.manipal.edu"

    # Construct email body
    body = f"""Dear {name}, 

    Please Find Attached the NOC for your Long Internship
    Regards
    """

    fromaddr = "tanay.act3@gmail.com"
    toaddr = rec

    msg = MIMEMultipart()
    msg['From'] = 'Tanay Shah'
    msg['To'] = toaddr
    msg['Subject'] = "No Objection Certificate"
    msg.attach(MIMEText(body, 'plain'))

    # Attach the specified attachment file for the current recipient
    with open(f"/Users/tanay/Documents/TANAY/TECH/Certificate_Automation/NOC/{attachment_filename}", "rb") as attachment_file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment_filename}')
        msg.attach(part)

    # Send email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "fmlwszthqutdthqb")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


def process_excel_data():
    # Read data from Excel file
    df = pd.read_excel("data.xlsx")

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        name = row['NAME']
        registration_number = row['REGISTRATION NUMBER']
        attachment_filename = f"{name}_{registration_number}.pdf"  # Assuming PDF files
        send_email(name, registration_number, attachment_filename)


if __name__ == "__main__":
    process_excel_data()
