from twilio.rest import Client


account_sid = 'ACf9de826c51883bd623cf464141aafcc4'
auth_token = '7ae28cde3f5318910478e4b8bed157de'

client = Client(account_sid, auth_token)

client.messages.create(from_= '+13345648344',
                       to='+5547991095142',
                       body='Mensagem SMS from Python using Twilio!')
