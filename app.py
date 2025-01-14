from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'suudi.abdisalan1@student.moringaschool.com'
app.config['MAIL_PASSWORD'] = 'cfba uzjf yfjv zxcq' 
app.config['MAIL_DEFAULT_SENDER'] = 'suudi.abdisalan1@student.moringaschool.com'

mail = Mail(app)

@app.route('/send-email', methods=['GET'])
def send_email():
    
    subject = request.args.get('subject', 'moringaaaa')
    body = request.args.get('body', 'Hello, there.')
    recipient = request.args.get('recipient', 'charles.njoroge@student.moringaschool.com')

    # Create and send the email

    msg = Message(subject=subject, recipients=[recipient])
    msg.body = body

    try:
        mail.send(msg)
        return "Email sent to the recipient successfully."
    except Exception as e:
        return f"Failed to send email: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
