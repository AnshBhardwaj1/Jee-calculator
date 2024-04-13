from keys_data import *
import os
from pathlib import Path
class question :
    def __init__(self,questionNumber, questionID, answerID, KeyID):
        self.questionNumber = questionNumber
        self.questionID = questionID
        self.answerID = answerID
        self.KeyID = KeyID
    def marks(self):
        if self.KeyID=="Drop":
            return 4
        elif self.answerID != ' -- ':
            if self.answerID == self.KeyID:
                return 4
            elif self.answerID != self.KeyID :
                return -1
        elif self.answerID == ' -- ':
            return 0 
    def __str__(self):
        return "Question Number: " + self.questionNumber + " Question ID: " + self.questionID + " Answer ID: " + self.answerID + " Key ID: " + self.KeyID

def soup_from_link(link):
    import requests
    from bs4 import BeautifulSoup
    page=requests.get(link)
    soup=BeautifulSoup(page.content,'lxml')
    return soup
def soup_from_file(file):
    from bs4 import BeautifulSoup
    with open(file, 'r') as file:
        soup=BeautifulSoup(file,'lxml')
    return soup
def give_marks_of_soup(soup):
    option_chose=None
    marked={}
    marks=0
    tag=list(soup.find_all('td'))
    tag = list(map(lambda i: i.text, tag))
    for i in range(len(tag)):
        if "Test Date" in tag[i]:
            date=(tag[i+1])
        if "Test Time" in tag[i]:
            time=(tag[i+1])
    if date=="27/01/2024" and time=="9:00 AM - 12:00 PM":
        key=mains27janshift1anskey
    if date=="27/01/2024" and time=="3:00 PM - 6:00 PM":
        key=mains27janshift2anskey
    if date=="29/01/2024" and time=="9:00 AM - 12:00 PM":
        key=mains29janshift1anskey
    if date=="29/01/2024" and time=="3:00 PM - 6:00 PM":
        key=mains29janshift2anskey
    if date=="30/01/2024" and time=="9:00 AM - 12:00 PM":
        key=mains30janshift1anskey
    if date=="30/01/2024" and time=="3:00 PM - 6:00 PM":
        key=mains30janshift2anskey
    if date=="31/01/2024" and time=="9:00 AM - 12:00 PM":
        key=mains31janshift1anskey
    if date=="31/01/2024" and time=="3:00 PM - 6:00 PM":
        key=mains31janshift2anskey
    if date=="01/02/2024" and time=="9:00 AM - 12:00 PM":
        key=mains1febshift1anskey
    if date=="01/02/2024" and time=="3:00 PM - 6:00 PM":
        key=mains1febshift2anskey
    if date=="04/04/2024" and time=="9:00 AM - 12:00 PM":
        key=mains4aprilshift1anskey
    if date=="04/04/2024" and time=="3:00 PM - 6:00 PM":
        key=mains4aprilshift2anskey
    if date=="05/04/2024" and time=="9:00 AM - 12:00 PM":
        key=mains5aprilshift1anskey
    if date=="05/04/2024" and time=="3:00 PM - 6:00 PM":
        key=mains5aprilshift2anskey
    if date=="06/04/2024" and time=="9:00 AM - 12:00 PM":
        key=mains6aprilshift1anskey
    if date=="06/04/2024" and time=="3:00 PM - 6:00 PM":
        key=mains6aprilshift2anskey
    if date=="08/04/2024" and time=="9:00 AM - 12:00 PM":
        key=mains8aprilshift1anskey
    if date=="08/04/2024" and time=="3:00 PM - 6:00 PM":
        key=mains8aprilshift2anskey
    if date=="09/04/2024" and time=="9:00 AM - 12:00 PM":
        key=mains9aprilshift1anskey
    if date=="09/04/2024" and time=="3:00 PM - 6:00 PM":
        key=mains9aprilshift2anskey

    #option_chose=None
    questions=[]
    question_ID=None
    for i in range(len(tag)):
        #questionID=4058591108
        if "Question ID :" == tag[i]: 
            #print("Question ID is ",tag[i+1])
            question_ID=tag[i+1]

        # to get answers of mcq type
        if "Option 1 ID :" == tag[i]: 
            opt1_ID=tag[i+1]
            #print ("Option 1 ID is ",tag[i+1])
        if "Option 2 ID :" == tag[i]:
            opt2_ID=tag[i+1]
            #print ("Option 2 ID is ",tag[i+1])
        if "Option 3 ID :" == tag[i]:
            opt3_ID=tag[i+1]
            #print ("Option 3 ID is ",tag[i+1])
        if "Option 4 ID :" == tag[i]:
            opt4_ID=tag[i+1]
            #print ("Option 4 ID is ",tag[i+1])
        if "Chosen Option :" == tag[i]:
            option_chose=tag[i+1]
            #print("Chosen Option is ",tag[i+1])
            if option_chose != " -- ":
                if option_chose=="1":
                    answer_ID=opt1_ID
                if option_chose=="2":
                    answer_ID=opt2_ID
                if option_chose=="3":
                    answer_ID=opt3_ID
                if option_chose=="4":
                    answer_ID=opt4_ID
            else:
                answer_ID=" -- "

        #to get answers of numerical type
        if "Given Answer :" == tag[i]: 
            given_ans=tag[i+1]
            answer_ID=given_ans
            #print("Given Answer is ",tag[i+1])

        #to get question number
        if "Q." in tag[i]:
            if len (tag[i])<6:
                questionNumber=tag[i][2:]
                if question_ID is not None: 
                    key_ID=key[question_ID]
                    questions.append(question(questionNumber, question_ID, answer_ID, key_ID))
                    #print (questionNumber, question_ID, answer_ID, key_ID)
    

    maths=0
    for i in range(1,32):
        maths = maths + questions[i].marks()
    physics=0
    for i in range(32,62):
        physics = physics + questions[i].marks()
    chemistry=questions[0].marks()
    for i in range(62,len(questions)):
        chemistry = chemistry + questions[i].marks()
    total=maths+physics+chemistry
    return (total,maths,physics,chemistry)


def give_marks(whatever):
    if whatever.startswith("http"):
        soup = soup_from_link(whatever)
        marks = give_marks_of_soup(soup)
    else:
        if Path(whatever).is_file():
            soup = soup_from_file(whatever)
            marks = give_marks_of_soup(soup)
            os.remove(whatever) 
        else:
            print(f"File {whatever} does not exist.")
            return (None)
    return marks
    
if __name__=="__main__":
    link=("https://cdn3.digialm.com//per/g28/pub/2083/touchstone/AssessmentQPHTMLMode1//2083O23354/2083O23354S15D16244/17067996516627886/KK14005904_2083O23354S15D16244E1.html#")
    marks=give_marks(link)
    print (f"Your marks are {marks}")
    #marks_html=give_marks('Test.html')
    #print (f"Your marks are {marks_html}")

        
