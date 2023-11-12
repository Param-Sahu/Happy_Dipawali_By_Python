# Program to wish Happy Dipawali to your family and friends through Whatsapp Web by python.
# Message will automatically send through Whatsapp Web.
from pywhatkit import sendwhatmsg 

# Enter name and mobile number of people in dictionary
people = [
            {'name':'Enter Name','mobile_no':'+91Mobile_Number'},
            {'name':'Enter Name','mobile_no':'+91Mobile_Number'},
            {'name':'Enter Name','mobile_no':'+91Mobile_Number'}  
        ] 
'''
 Make sure replace 'Enter_Name' with actual person Name and '+91Mobile_Number' with actual mobile number of that person.
 replace '+91Mobile_Number' with actual mobile number Example :  '+9198XXXXXXXX'
Make sure mobile number in string format with country code and without space.
You can add more name and mobile number according to your need.
'''

print("Enter Time to send message (in 24 hour format) \n.")
hour = int(input('Enter Hour : ')) 

minutes = int(input("Enter Minutes : "))

for person in people:
    sendwhatmsg(person['mobile_no'],f"Happy Dipawali {person['name']}",hour,minutes,40)
    minutes+=2
    '''
    After 2 minutes next message will be send. At a time only one message will send.
     You can modify hour/minutes time delay between messages according to your need.

 Make sure You have logged in your whatsapp in your primary browser (Microsoft Edge or Chrome etc).
 Make sure You are connected to internet.
 Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!'''