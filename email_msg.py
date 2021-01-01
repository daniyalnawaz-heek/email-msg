import yagmail

sender_gmail= "sender_email"
reciever_gmail= "receiver_email"
subject="test" 
content="just a test"
yag=yagmail.SMTP("sender_email","passowrd")
yag.send(reciever_gmail,subject,content)