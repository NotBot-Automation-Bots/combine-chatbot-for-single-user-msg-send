from logging import exception
from flask import Flask, request
from waapis import create_group_chatapi 
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
import mysec
import waapis
import requests
import json
import datetime
app = Flask(__name__)



# Database config
app.config["MONGO_URI"] = mysec.MONGO_URI
mongo = PyMongo(app)
client = MongoClient(mysec.MONGO_URI)

db = client['dynamic_group_chatbot_dev']
groups = db.groups   


def getGroupChatID(groupname):
    chatid = groups.find_one({'groupname' : groupname})
    if(chatid is not None):
        return chatid['chatId']
    url = f"{mysec.API_URL}dialogs?token={mysec.TOKEN}"
    headers = {'Content-type': 'application/json'}
    resp = requests.get(url=url, headers=headers)
    groupsdata = {}
    alldata = resp.json()
    for item in (alldata['dialogs']):
        if(item['metadata']['isGroup'] and item['name'] == groupname):
            return item['id']
    return None


#################################### Start for Fiidaa Art chatbot ###########################


fiidaa_art_msg1 = "Hi {} \n\n Book an appointment now to find out what kind of art would best suit your living spaces! \n 1) Yes! Book an appointment \n 2) Tell me more please"


fiidaa_art_msg2 = "Fiidaa Art has been in the art industry with 15+ years, helping clients such as DBS Private Bank, King and Spalding LLP and many others with their art curation and interior decoration\n\n“Fiidaa Art worked with us every step of the way to ensure that timelines and targets were met. We are very satisfied with the art consulting services provided by Sangeeta at Fiidaa Art and would love to work with her for any of our future projects in the region.” \n\n  May Lum, Assistant Vice President, Product & Technical Services, Ascott International Management, Singapore \n 1) Yes! Book an appointment \n 2) No thank you"

fiidaa_art_msg3 = "Please leave your name and mobile number and our consultants will get back to you! Thank you!"

fiidaa_art_msg4 = "Do you have any inquiries or uncertainties about your first time art purchase? \n\n 1) Tell me more about your service! \n 2) May I speak to a consultant?"

fiidaa_art_msg5 = "Do you have any inquiries or uncertainties about your first time art purchase? \n\n 1) Tell me more about your service! \n 2) May I speak to a consultant?"


fiidaa_art_msgs = [fiidaa_art_msg2, fiidaa_art_msg3, fiidaa_art_msg4, fiidaa_art_msg5]





####################### Start fo right tatents for property bot #######################


propert_bot_for_tenants_msg1 = "Hi {} \n\n Talk to our consultants now to find the right tenants for your property! \n 1) Yes! Book an appointment \n 2) Tell me more please"


propert_bot_for_tenants_msg2 = "Nick and Rina have 15 years of experience in the market, and are committed to finding the best tenants for your property at the highest rates!  \n 1) Yes! Book an appointment \n 2) No thank you"

propert_bot_for_tenants_msg3 = "Our consultants will reach out to you! Thank you for choosing Nick and Rina!"

propert_bot_for_tenants_msg4 = "Hey! \n Recently, we just sold Simei 102 4rm unit and even got it  tenanted in a week. Why & how did we managed to sell? With our digital creative & video marketing methods, we managed to achieve the desired price for our seller and even got them the best rental rates with a desired tenant! Would you like to be our next success story?  \n\n 1) Tell me more about your service! \n 2) May I speak to a consultant?"


propert_bot_for_tenants_msg5 = "Do you have any inquiries on leasing your property? \n 1) Yes would like to book an appointment \n 2) May I speak to a consultant?"

propert_bot_for_tenants_msgs = [propert_bot_for_tenants_msg2, propert_bot_for_tenants_msg3, propert_bot_for_tenants_msg4, propert_bot_for_tenants_msg5]



####################### Start for Home bot #######################


home_bot_msg1 = "Hi {} \n\n\Book an appointment now to get the lowest 1% property agent rates for your home! \n 1) Yes! Book an appointment \n 2) Tell me more please"


home_bot_msg2 = "Nick and Rina are committed to selling your homes and saving you up to $8k or more! They have more than 15 years experience in the SG property market! \n 1) Yes! Book an appointment \n 2) No thank you"

home_bot_msg3 = "Our consultants will reach out to you! Thank you for choosing Nick and Rina!"

home_bot_msg4 = "Hey! \n We just helped our clients to sell their  HDB in 1 WEEK with High COV and the highest transacted price, with just a 1% AGENT FEE. They managed to upgrade to a beautiful spacious corner high floor EA without COV. \n\n\n The sellers contacted us via FB because they were having doubts about selling and buying immediately especially the timeline. We managed to clear all their doubts and queries with detailed explanations of all their financial calculations and the timeline process which is very crucial for all sellers, who are doing contra. Within 1 week of marketing, the unit was sold and they managed to buy it immediately and upgrade to an EA. The sellers are overjoyed because they got a HIGH COV for their flat and managed to upgrade to their dream home. Want to be our next success story? \n\n 1) Tell me more about your service! \n 2) May I speak to a consultant?"


home_bot_msg5 = "Do you have any inquiries on selling your property? \n 1) Yes would like to book an appointment \n 2) May I speak to a consultant?"

home_bot_msgs = [home_bot_msg2, home_bot_msg3, home_bot_msg4, home_bot_msg5]


####################### Start for HDB bot #######################



hdb_bot_msg1 = "Book an appointment now to find out how much you can make selling your HDB property! \n 1) Yes! Book an appointment \n 2) Tell me more please"


hdb_bot_msg2 = "Nick and Rina are committed to selling your homes and saving you up to $8k or more! They have more than 15 years experience in the SG property market!  \n 1) Yes! Book an appointment \n 2) No thank you"

hdb_bot_msg3 = "Our consultants will reach out to you! Thank you for choosing Nick and Rina!"

hdb_bot_msg4 = "Hey! \n Recently, some sellers contacted us for they were curious to know how we have helped so many clients to upgrade and cash out 6 figures with their MOP flats. Also looking through our track records and 20 years experience, they wanted to sell their 4rm Mop Flat and upgrade to a bigger spacious flat for their growing family. \n\n\n Thus, with an effective marketing strategy plan, we managed to clear their doubts with detailed explanations of all their financial calculations and started marketing immediately. We managed to achieve their desired price and that too above sellers' expectations \n\n Big congrats to our clients and thank you for trusting us in your asset progression journey. \n\n After Covid 19 outbreak, many HDB Owners have SOLD their flats above valuation with significant high COV amounts! Would you like to be our next success story? \n\n\n 1) Tell me more about your service! \n 2) May I speak to a consultant?"


hdb_bot_msg5 = "Do you have any MOP/inquiries on selling your HDB?  \n 1) Yes would like to book an appointment \n 2) May I speak to a consultant?"

hdb_bot_msgs = [hdb_bot_msg2, hdb_bot_msg3, hdb_bot_msg4, hdb_bot_msg5]


'''

{'messages': [{'id': 'false_120363040173984687@g.us_C960FF9BFCE6CD8CBBB62E522021A569_6593202649@c.us', 'body': 'Happy birthday @6581981427', 'fromMe': False, 'self': 0, 'isForwarded': None, 'author': '6593202649@c.us', 'time': 1651496940, 'chatId': '120363040173984687@g.us', 'messageNumber': 20185, 'type': 'chat', 'senderName': 'HamkaHasse', 'caption': None, 'quotedMsgBody': None, 'quotedMsgId': None, 'quotedMsgType': None, 'metadata': None, 'ack': None, 'chatName': '20/5 FRIDAY FLOORBALL'}], 'instanceId': '350463'}


'''



    
@app.route('/')
def index():
    return "Application is Up !!!! All chatbot"



'''

{'messages': [{'id': 'false_120363040173984687@g.us_C960FF9BFCE6CD8CBBB62E522021A569_6593202649@c.us', 'body': 'Happy birthday @6581981427', 'fromMe': False, 'self': 0, 'isForwarded': None, 'author': '6593202649@c.us', 'time': 1651496940, 'chatId': '120363040173984687@g.us', 'messageNumber': 20185, 'type': 'chat', 'senderName': 'HamkaHasse', 'caption': None, 'quotedMsgBody': None, 'quotedMsgId': None, 'quotedMsgType': None, 'metadata': None, 'ack': None, 'chatName': '20/5 FRIDAY FLOORBALL'}], 'instanceId': '350463'}


'''


@app.route('/handle', methods=['POST'])
def handleWebhook():
    try:

        print("request for webhhok")

        data = request.json
        if "messages" in data.keys():

            for msg in data['messages']:

                # if(msg['fromMe']):
                #     return "my msg"
                msg_text = (msg['body'])
                try:
                    msg_text = int(msg_text)
                except:
                    print("text type of reply")
                chatid = msg['chatId']
                sender = msg['author']
                sender = sender[:-5]
                group_obj = groups.find_one({'user_contact' : str(sender) , 'chatbot' : 1})
                print(group_obj)
                print(group_obj)
                print(group_obj)
#################################### End for fiidata chatbot ###########################
                
                if group_obj is not None and (str(group_obj['customer']) == str(sender),group_obj['user_contact_status'] == "fiidata_chatbot"+str(sender), group_obj['chat_bot_type'] == "fiidata_chatbot_data"):
                    filter = {'_id' : group_obj['_id']}
                    msg_number = group_obj['msg_sent']
                    newvalues = { "$set": { 'msg_sent': msg_number +1 } }
                    
                    msg_date = group_obj['msg_sent_date_time']

                    if (msg_date != False) : 
                        hr_diff = datetime.datetime.now().hour - msg_date.hour                    
                        date_diff = datetime.datetime.now().day  - msg_date.day
                        if(date_diff ==1 and hr_diff == 0 and msg_number == 0 and  group_obj['flow_step'] == 0):
                            #sending msg on group
                            newvalues = { "$set": { 'msg_sent': msg_number +10 ,"msg_sent_date_time" : False,'flow_step':4} }
                            msg_body = fiidaa_art_msg[2]
                            url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                            headers = {'Content-type': 'application/json'}
                            data = {
                                "body": msg_body,
                                "phone": sender
                            }
                            resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                            groups.update_one(filter, newvalues)
                        elif(date_diff ==1 and hr_diff == 0 and msg_number == 1 and  group_obj['flow_step'] == 2):
                            #sending msg on group
                            newvalues = { "$set": { 'msg_sent': msg_number +11 ,"msg_sent_date_time" : False,'flow_step':3} }
                            msg_body = fiidaa_art_msg[3]
                            url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                            headers = {'Content-type': 'application/json'}
                            data = {
                                "body": msg_body,
                                "phone": sender
                            }
                            resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                            groups.update_one(filter, newvalues)
                            
                    if (msg_number == 10 and group_obj['flow_step'] == 4 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': 1 ,"flow_step" : 2,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msg[0]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 10 and group_obj['flow_step'] == 4 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': 1 ,"flow_step" : 2,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msg[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    


                    elif (msg_number == 0 and group_obj['flow_step'] == 0 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msg[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 0 and group_obj['flow_step'] == 0 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 2 ,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msg[0]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    elif (msg_number == 1 and group_obj['flow_step'] == 2 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : datetime.datetime.now()} }
                        msg_body = fiidaa_art_msg[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 1 and group_obj['flow_step'] == 2 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : datetime.datetime.now()} }
                        msg_body = fiidaa_art_msg[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    
                    elif (msg_number == 12 and group_obj['flow_step'] == 3 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +12 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msg[5]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 12 and group_obj['flow_step'] == 3 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +12 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msg[5]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    return 'Success'

#################################### End for fiidata bot chatbot ###########################

#################################### Start for property_bot chatbot ###########################
                
                elif group_obj is not None and (str(group_obj['customer']) == str(sender),group_obj['user_contact_status'] == "property_bot_for_tenants_chatbot"+str(sender), group_obj['chat_bot_type'] == "property_bot_for_tenants_chatbot_data"):
                    filter = {'_id' : group_obj['_id']}
                    msg_number = group_obj['msg_sent']
                    newvalues = { "$set": { 'msg_sent': msg_number +1 } }
                    
                    msg_date = group_obj['msg_sent_date_time']

                    if (msg_date != False) : 
                        hr_diff = datetime.datetime.now().hour - msg_date.hour                    
                        date_diff = datetime.datetime.now().day  - msg_date.day
                        if(date_diff ==1 and hr_diff == 0 and msg_number == 0 and  group_obj['flow_step'] == 0):
                            #sending msg on group
                            newvalues = { "$set": { 'msg_sent': msg_number +10 ,"msg_sent_date_time" : False,'flow_step':4} }
                            msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[2]
                            url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                            headers = {'Content-type': 'application/json'}
                            data = {
                                "body": msg_body,
                                "phone": sender
                            }
                            resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                            groups.update_one(filter, newvalues)
                        elif(date_diff ==1 and hr_diff == 0 and msg_number == 1 and  group_obj['flow_step'] == 2):
                            #sending msg on group
                            newvalues = { "$set": { 'msg_sent': msg_number +11 ,"msg_sent_date_time" : False,'flow_step':3} }
                            msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[3]
                            url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                            headers = {'Content-type': 'application/json'}
                            data = {
                                "body": msg_body,
                                "phone": sender
                            }
                            resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                            groups.update_one(filter, newvalues)
                            
                    if (msg_number == 10 and group_obj['flow_step'] == 4 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': 1 ,"flow_step" : 2,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[0]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 10 and group_obj['flow_step'] == 4 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': 1 ,"flow_step" : 2,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    


                    elif (msg_number == 0 and group_obj['flow_step'] == 0 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 0 and group_obj['flow_step'] == 0 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 2 ,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[0]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    elif (msg_number == 1 and group_obj['flow_step'] == 2 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : datetime.datetime.now()} }
                        msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 1 and group_obj['flow_step'] == 2 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : datetime.datetime.now()} }
                        msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    
                    elif (msg_number == 12 and group_obj['flow_step'] == 3 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +12 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[5]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 12 and group_obj['flow_step'] == 3 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +12 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = fiidaa_art_msgpropert_bot_for_tenants_msgs[5]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                
                    return 'Success'

#################################### Start for property bot chatbot ###########################
                

#################################### Start for home_bot chatbot ###########################
                
                
                elif group_obj is not None and (str(group_obj['customer']) == str(sender),group_obj['user_contact_status'] == "home_bot_chatbot"+str(sender), group_obj['chat_bot_type'] == "home_bot_chatbot_data"):
                    
                    filter = {'_id' : group_obj['_id']}
                    msg_number = group_obj['msg_sent']
                    newvalues = { "$set": { 'msg_sent': msg_number +1 } }
                    
                    msg_date = group_obj['msg_sent_date_time']

                    if (msg_date != False) : 
                        hr_diff = datetime.datetime.now().hour - msg_date.hour                    
                        date_diff = datetime.datetime.now().day  - msg_date.day
                        if(date_diff ==1 and hr_diff == 0 and msg_number == 0 and  group_obj['flow_step'] == 0):
                            #sending msg on group
                            newvalues = { "$set": { 'msg_sent': msg_number +10 ,"msg_sent_date_time" : False,'flow_step':4} }
                            msg_body = home_bot_msgs[2]
                            url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                            headers = {'Content-type': 'application/json'}
                            data = {
                                "body": msg_body,
                                "phone": sender
                            }
                            resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                            groups.update_one(filter, newvalues)
                        elif(date_diff ==1 and hr_diff == 0 and msg_number == 1 and  group_obj['flow_step'] == 2):
                            #sending msg on group
                            newvalues = { "$set": { 'msg_sent': msg_number +11 ,"msg_sent_date_time" : False,'flow_step':3} }
                            msg_body = home_bot_msgs[3]
                            url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                            headers = {'Content-type': 'application/json'}
                            data = {
                                "body": msg_body,
                                "phone": sender
                            }
                            resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                            groups.update_one(filter, newvalues)
                            
                    if (msg_number == 10 and group_obj['flow_step'] == 4 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': 1 ,"flow_step" : 2,"msg_sent_date_time" : False} }
                        msg_body = home_bot_msgs[0]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 10 and group_obj['flow_step'] == 4 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': 1 ,"flow_step" : 2,"msg_sent_date_time" : False} }
                        msg_body = home_bot_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    


                    elif (msg_number == 0 and group_obj['flow_step'] == 0 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = home_bot_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 0 and group_obj['flow_step'] == 0 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 2 ,"msg_sent_date_time" : False} }
                        msg_body = home_bot_msgs[0]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    elif (msg_number == 1 and group_obj['flow_step'] == 2 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : datetime.datetime.now()} }
                        msg_body = home_bot_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 1 and group_obj['flow_step'] == 2 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : datetime.datetime.now()} }
                        msg_body = home_bot_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    
                    elif (msg_number == 12 and group_obj['flow_step'] == 3 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +12 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = home_bot_msgs[5]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 12 and group_obj['flow_step'] == 3 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +12 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = home_bot_msgs[5]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    

                    # elif (msg_number == 1 and flow_step == 0):

                    # if(msg_number == 0 and(msg_text not in [1,2,3])):
                    #     return "Wrong Reply"

                    # elif(msg_number == 2 and(msg_text not in [1,2])):
                    #     return "Wrong Reply"
                    # elif(msg_number == 3 and(msg_text not in [1,2])):
                    #     return "Wrong Reply"
                    # print(group_obj)
                    # print(msg_number)
                    # print(msg_number)
                    # if(msg_number > 3):
                    #     print("Msg Number exceding")
                    #     return "done"
                    
                    # #sending msg on group
                    # msg_body = home_bot_msgs[msg_number]
                    # url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                    # headers = {'Content-type': 'application/json'}
                    # data = {
                    #     "body": msg_body,
                    #     "phone": sender
                    # }
                    # resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                    # groups.update_one(filter, newvalues)
                    # print(resp.text)
                    # return resp.text
                    return 'Success'

#################################### End for home_bot chatbot ###########################


#################################### Start for hdb_bot chatbot ###########################


                elif group_obj is not None and (str(group_obj['customer']) == str(sender),group_obj['user_contact_status'] == "hdb_bot_chatbot"+str(sender), group_obj['chat_bot_type'] == "hdb_bot_chatbot_data"):
                    hr_diff = datetime.datetime.now().hour - msg_date.hour                    
                    date_diff = datetime.datetime.now().day  - msg_date.day
                    if(date_diff ==1 and hr_diff == 0 and msg_number == 0 and  group_obj['flow_step'] == 0):
                        #sending msg on group
                        newvalues = { "$set": { 'msg_sent': msg_number +10 ,"msg_sent_date_time" : False,'flow_step':4} }
                        msg_body = hdb_bot_msgs[2]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif(date_diff ==1 and hr_diff == 0 and msg_number == 1 and  group_obj['flow_step'] == 2):
                        #sending msg on group
                        newvalues = { "$set": { 'msg_sent': msg_number +11 ,"msg_sent_date_time" : False,'flow_step':3} }
                        msg_body = hdb_bot_msgs[3]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                            
                    if (msg_number == 10 and group_obj['flow_step'] == 4 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': 1 ,"flow_step" : 2,"msg_sent_date_time" : False} }
                        msg_body = hdb_bot_msgs[0]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 10 and group_obj['flow_step'] == 4 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': 1 ,"flow_step" : 2,"msg_sent_date_time" : False} }
                        msg_body = hdb_bot_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    


                    elif (msg_number == 0 and group_obj['flow_step'] == 0 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = hdb_bot_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 0 and group_obj['flow_step'] == 0 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 2 ,"msg_sent_date_time" : False} }
                        msg_body = hdb_bot_msgs[0]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    elif (msg_number == 1 and group_obj['flow_step'] == 2 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : datetime.datetime.now()} }
                        msg_body = hdb_bot_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 1 and group_obj['flow_step'] == 2 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +1 ,"flow_step" : 5,"msg_sent_date_time" : datetime.datetime.now()} }
                        msg_body = hdb_bot_msgs[1]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    
                    elif (msg_number == 12 and group_obj['flow_step'] == 3 and msg_text == 1):
                        newvalues = { "$set": { 'msg_sent': msg_number +12 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = hdb_bot_msgs[5]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    elif (msg_number == 12 and group_obj['flow_step'] == 3 and msg_text == 2):
                        newvalues = { "$set": { 'msg_sent': msg_number +12 ,"flow_step" : 5,"msg_sent_date_time" : False} }
                        msg_body = hdb_bot_msgs[5]
                        url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                        headers = {'Content-type': 'application/json'}
                        data = {
                            "body": msg_body,
                            "phone": sender
                        }
                        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                        groups.update_one(filter, newvalues)
                    
                    return 'Success'
#################################### End for hdb_bot chatbot ###########################


                else:
                    print("Group not exist in DB or msg from the owner")
                    return "group not exists"
        else:
            return "Out of my Scope"

    except Exception as e:
        print(e)
        return str(e)
    

@app.route('/sendmsg', methods=['POST'])
def fiidaa_art_create_group():
    request_data = request.get_json()
    chatbot_type = request.json['chatbot_type']

    ############## Start for Fiidaa Art chatbot ##############

    if chatbot_type == "fiidaa_art_chatbot":
        phone_number = None
        group_name = ""
        if request_data:
            # request_data = request.get_json()
            if ('customer' in request_data) :
                customer = request_data["customer"]
                # chatbot_status = request.json['bot_status']
                chatbot_status = request_data['bot_status']
                group_name = request_data["customer"]
                grps = groups.find_one({
                    'phone_list': [customer],
                    "user_contact" : customer,
                    "user_contact_status" : "fiidata_chatbot"+str(customer),
                    "chat_bot_type" : "fiidata_chatbot_data",
                    })
                if(grps is None):
                    url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                    headers = {'Content-type': 'application/json'}
                    data = {
                        "body": fiidaa_art_msg1.format(request_data['msg']),
                        "phone": customer
                    }
                    resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                    


                    newGroup = {
                        # 'owner': owner,
                        "customer": customer,
                        'phone_list' : customer,
                        "user_contact" : customer,
                        "user_contact_status" : "fiidata_chatbot"+str(customer),
                        "chatbot" : chatbot_status,
                        "msg_sent": 0,
                        "chat_bot_type" : "fiidata_chatbot_data",
                        }
                    groups.insert_one(newGroup)  
                    
                    return '0'              
                else :
                    return "Message already send "

            else:
                return {"message": "Failed", "details": "phone number or group name is missing"}
            
        else:
            return {"message": "Failed", "details": "request body missing"}

#################################### End for Fiidaa Art chatbot ###########################


#################################### Start for property_bot_for_tenants chatbot ###########################

    elif chatbot_type == "property_bot_for_tenants_chatbot":
        phone_number = None
        group_name = ""
        if request_data:
            # request_data = request.get_json()
            if ('customer' in request_data) :
                customer = request_data["customer"]
                # chatbot_status = request.json['bot_status']
                chatbot_status = request_data['bot_status']
                group_name = request_data["customer"]
                grps = groups.find_one({
                    'phone_list': [customer],
                    "user_contact" : customer,
                    "user_contact_status" : "property_bot_for_tenants_chatbot"+str(customer),
                    "chat_bot_type" : "property_bot_for_tenants_chatbot_data",
                    })
                if(grps is None):
                    url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                    headers = {'Content-type': 'application/json'}
                    data = {
                        "body": propert_bot_for_tenants_msg1.format(request_data['msg']),
                        "phone": customer
                    }
                    resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                    


                    newGroup = {
                        # 'owner': owner,
                        "customer": customer,
                        'phone_list' : customer,
                        "user_contact" : customer,
                        "user_contact_status" : "property_bot_for_tenants_chatbot"+str(customer),
                        "chatbot" : chatbot_status,
                        "msg_sent": 0,
                        "chat_bot_type" : "property_bot_for_tenants_chatbot_data",
                        }
                    groups.insert_one(newGroup)  
                    
                    return '0'              
                else :
                    return "Message already send "

            else:
                return {"message": "Failed", "details": "phone number or group name is missing"}
            
        else:
            return {"message": "Failed", "details": "request body missing"}

#################################### End for property_bot_for_tenants chatbot ###########################

#################################### Start for home_bot chatbot ###########################


    elif chatbot_type == "home_bot_chatbot":
        phone_number = None
        group_name = ""
        if request_data:
            # request_data = request.get_json()
            if ('customer' in request_data) :
                customer = request_data["customer"]
                # chatbot_status = request.json['bot_status']
                chatbot_status = request_data['bot_status']
                group_name = request_data["customer"]
                grps = groups.find_one({
                    'phone_list': [customer],
                    "user_contact" : customer,
                    "user_contact_status" : "home_bot_chatbot"+str(customer),
                    "chat_bot_type" : "home_bot_chatbot_data",
                    })
                if(grps is None):
                    url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                    headers = {'Content-type': 'application/json'}
                    data = {
                        "body": home_bot_msg1.format(request_data['msg']),
                        "phone": customer
                    }
                    resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                    
                    newGroup = {
                        # 'owner': owner,
                        "customer": customer,
                        'phone_list' : customer,
                        "user_contact" : customer,
                        "user_contact_status" : "home_bot_chatbot"+str(customer),
                        "chatbot" : chatbot_status,
                        "msg_sent": 0,
                        "chat_bot_type" : "home_bot_chatbot_data",
                        }
                    groups.insert_one(newGroup)  
                    
                    return '0'              
                else :
                    return "Message already send "

            else:
                return {"message": "Failed", "details": "phone number or group name is missing"}
            
        else:
            return {"message": "Failed", "details": "request body missing"}

#################################### End for home_bot chatbot ###########################

#################################### Start for hdb_bot chatbot ###########################

    elif chatbot_type == "hdb_bot_chatbot":
        phone_number = None
        group_name = ""
        if request_data:
            # request_data = request.get_json()
            if ('customer' in request_data) :
                customer = request_data["customer"]
                # chatbot_status = request.json['bot_status']
                chatbot_status = request_data['bot_status']
                group_name = request_data["customer"]
                grps = groups.find_one({
                    'phone_list': [customer],
                    "user_contact" : customer,
                    "user_contact_status" : "hdb_bot_chatbot"+str(customer),
                    "chat_bot_type" : "hdb_bot_chatbot_data",
                    })
                if(grps is None):
                    url = f"{mysec.API_URL}sendMessage?token={mysec.TOKEN}"
                    headers = {'Content-type': 'application/json'}
                    data = {
                        "body": hdb_bot_msg1.format(request_data['msg']),
                        "phone": customer
                    }
                    resp = requests.post(url=url, headers=headers, data=json.dumps(data))
                    


                    newGroup = {
                        # 'owner': owner,
                        "customer": customer,
                        'phone_list' : customer,
                        "user_contact" : customer,
                        "user_contact_status" : "hdb_bot_chatbot"+str(customer),
                        "chatbot" : chatbot_status,
                        "msg_sent": 0,
                        "chat_bot_type" : "hdb_bot_chatbot_data",
                        }
                    groups.insert_one(newGroup)  
                    
                    return '0'              
                else :
                    return "Message already send "

            else:
                return {"message": "Failed", "details": "phone number or group name is missing"}
            
        else:
            return {"message": "Failed", "details": "request body missing"}

#################################### End for hdb_bot chatbot ###########################


if __name__ == '__main__':
    app.run()




# first_chatbot = {
#     "customer" : "918815312085",
#     "msg" : "Arun Ahirwar",
#     "bot_status" : 1,
#     "chatbot_type" : "fiidaa_art_chatbot"
# }


# second_chatbot = {
#     "customer" : "918815312085",
#     "msg" : "Arun Ahirwar",
#     "bot_status" : 1,
#     "chatbot_type" : "property_bot_for_tenants_chatbot"
# }


# third_chatbot = {
#     "customer" : "918815312085",
#     "msg" : "Arun Ahirwar",
#     "bot_status" : 1,
#     "chatbot_type" : "home_bot_chatbot"
# }

# third_chatbot = {
#     "customer" : "918815312085",
#     "msg" : "Arun Ahirwar",
#     "bot_status" : 1,
#     "chatbot_type" : "hdb_bot_chatbot"
# }