from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from urllib.request import urlopen
from msg_parser import MsOxMessage

app = Flask(__name__)

@app.route('/mybot', methods=['POST'])
def bot():
    user_msg = request.values.get('Body','').lower()
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    if 'hi' in user_msg:
        msg.body("Hi there! Welcome to VIT-AP University"
        "\nType 1 for Admission Process"
        "\nType 2 to know about Program offered"
        "\nType 3 to know about Eligibility"
        "\nType 4 to get Information Brochure"
        "\nType 5 for campus tour"
        "\nType 6 to apply online"
        "\nType 0 to STOP")
    elif '1' in user_msg:
        msg.body("Selection is based on the rank secured through CBT (Computer Based Test)."
        "\nSelected candidates will be called for online counselling based on their ranking."
        "\nEligible Candidates may select specific campus and programme during the Counselling."
        "\nAfter payment of full fees classes will be conducted online / reporting in person to the Institution."
        "\nCandidates are expected to prove their genuineness on joining.")
    elif '2' in user_msg:
        msg.body("Computer Science and Engineering"
        "\nComputer Science and Engineering with Specilization in Business System (In collaboration with (TCS)"
        "\nElectronics and Communication Engineering"
        "\nMechanical Engineering")
    elif '3' in user_msg:
        msg.body("Nationality:"
        "\nThe applicant should be a Resident / Non Resident Indian National / PIO."
        "\nForeign Candidates studied/studying abroad can apply directly through foreign category only at")
        msg.body('https://admissions.vit.ac.in/ugirapplication/')
        
        msg.body("Age Limit:"
        "\nCandidates whose date of birth falls on or after 1st July 2001 are eligible to apply for UG Engineering admission (UGEA) 2023. The date of birth as recorded in the High School / SSC / X Certificate will be considered authentic.")
    elif '4' in user_msg:
        msg.media('https://vitap.ac.in/wp-content/uploads/2022/11/VITEEE-2023-information-brochure.pdf')
    elif '5' in user_msg:
        msg.body('https://www.youtube.com/watch?v=gbCMBAGmRAg')
    elif '6' in user_msg:
        msg.body("Application Available Online : ")
        msg.body('https://viteee.vit.ac.in/?utm_source=V71TI1557&utm_campaign=viteee2023')
    elif '0' in user_msg:
        quit()
    else:
        msg.body("Hi there! Welcome to VIT-AP University"
        "\nType 1 for Admission Process"
        "\nType 2 to know about Program offered"
        "\nType 3 to know about Eligibility"
        "\nType 4 to get Information Brochure"
        "\nType 5 for campus tour"
        "\nType 6 to apply online"
        "\nType 0 to exit")
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)