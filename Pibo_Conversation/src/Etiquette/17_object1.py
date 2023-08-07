# -*- coding: utf-8 -*-

# 사회기술-물건을 두 손으로 받고 드려요

import os, sys
import re
import csv
import random
from datetime import datetime
import time
import json

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Package_13/Pibo_Conversation/')
from data.c_conversation_manage import ConversationManage, WordManage, NLP
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech
from data.spread import google_spread_sheet
from openpibo.vision import Camera
from openpibo.vision import Detect


pibo_camera = Camera()
pibo_detect = Detect()

cm = ConversationManage()
wm = WordManage()
nlp = NLP()
audio = TextToSpeech()
gss = google_spread_sheet()

folder = "/home/pi/UserData"
filename = os.path.basename(__file__).strip('.py')
today = datetime.now().strftime('%m%d_%H%M')
csv_conversation = open(f'{folder}/{today}_{filename}.csv', 'a', newline='', encoding = 'utf-8')
csv_preference = open(f'{folder}/aa.csv', 'a', newline='', encoding = 'utf-8')
cwc = csv.writer(csv_conversation)
cwp = csv.writer(csv_preference)
crc = csv.reader(csv_conversation, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"')


class Etiquette():    
    
    def __init__(self): 
        with open('/home/pi/name_config.json', 'r') as f:
            config = json.load(f)        
            self.user_name = config['user_name'] 
        self.correct = ['손', '받', '한', '두']
        self.ox = ''
                
        
    def Object1(self):
        
        # 2.1 카드 대화
        pibo = cm.tts(bhv="do_question_L", string="이 카드의 어린이는 무엇을 잘못했을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="이 카드의 어린이는 무엇을 잘못했을까?",
                                   neg_bhv="do_suggestion_S", neg="같이 다시 한번 볼까?",
                                   neu_bhv="do_suggestion_S", neu="같이 다시 한번 볼까?")             
        
        if answer[0][0] == "action":            
            
            for i in range(len(self.correct)):
                if self.correct[i] in answer[0][1]:
                    self.ox = "(right)"                    
            if len(self.ox) == 0:
                self.ox = "(wrong ㅠㅠ)"
              
            if self.ox == "(right)":
                print(self.ox)
                pibo = cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
            else:
                print(self.ox)
                pibo = cm.tts(bhv="do_suggestion_S", string="또 무엇을 잘못했을까?")
                answer = cm.responses_proc(re_bhv="do_suggestion_S", re_q="또 무엇을 잘못했을까?")
                
                if answer[0][0] == "action":        
                                
                    for i in range(len(self.correct)):
                        if self.correct[i] in answer[0][1]:
                            self.ox = "(right)"                    
                    if len(self.ox) == 0:
                        self.ox = "(wrong ㅠㅠ)"
                    
                    if self.ox == "(right)":
                        print(self.ox)
                        pibo = cm.tts(bhv="do_compliment_S", string="맞아! 아주 똑똑한 걸?")
                    else:
                        print(self.ox)
                        pibo = cm.tts(bhv="do_suggestion_S", string="같이 다시 한번 볼까?")
        
        pibo = cm.tts(bhv="do_explain_A", string="이 카드의 어린이는 어른이 건네주는 물건을 두 손으로 받고 있지 않아.")
     
        # 2.2 경험 질문
        pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}는 친구들에게 물건을 줄 때 어떻게 주니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)}는 친구들에게 물건을 줄 때 어떻게 주니?",
                                   pos_bhv="do_joy_A", pos="한 손으로 친절하게 전달해 줘야겠지?",
                                   act_bhv="do_joy_B", act="한 손으로 친절하게 전달해 줘야겠지?")
        
        pibo = cm.tts(bhv="do_question_S", string="어른들께 물건을 드릴 땐, 어떻게 드리는게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어른들께 물건을 드릴 땐, 어떻게 드리는게 좋을까?",
                                   neu_bhv="do_explain_A", neu="두 손으로 공손하게 전달해 드려야 해!")
        
        pibo = cm.tts(bhv="do_question_S", string="어른들께서 주는 물건을 받을 땐, 어떻게 받는 것이 맞을까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어른들께 물건을 드릴 땐, 어떻게 드리는게 좋을까?",
                                   pos_bhv="do_explain_B", pos="두 손으로 감사합니다. 인사하며 받아야 해!",
                                   neu_bhv="do_explain_B", neu="두 손으로 감사합니다. 인사하며 받아야 해!",
                                   act_bhv="do_explain_B", act="두 손으로 감사합니다. 인사하며 받아야 해!")
        
        # 2.3 문제 인식
        pibo = cm.tts(bhv="do_question_L", string="어른들께 물건을 드릴 때 한 손으로 물건을 받거나 드리게 되면 어른들은 기분이 어떠실까?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q="어른들께 물건을 드릴 때 한 손으로 물건을 받거나 드리게 되면 어른들은 기분이 어떠실까?",
                                   pos_bhv="do_explain_C", pos=f"{wm.word(self.user_name, 0)}는 버릇이 없다고 생각하실 거야!",
                                   neu_bhv="do_explain_C", neu=f"괜찮아. 모를 수도 있어. {wm.word(self.user_name, 0)}는 버릇이 없다고 생각하실 거야!",
                                   act_bhv="do_explain_C", act=f"{wm.word(self.user_name, 0)}는 버릇이 없다고 생각하실 거야!")
    
        # 3.1 마무리 대화
        pibo = cm.tts(bhv="do_joy_A", string=f"어른들께 물건을 드리거나 받을 땐, 두 손으로 공손하게 드리고 받는 예의 바른 {wm.word(self.user_name, 0)}가 되자!")
    
        
        
        
        # 3. 피드백 수집
        time.sleep(1)                   
        pibo = cm.tts(bhv="do_question_S", string="파이보랑 얘기한 거 재미있었어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"파이보랑 얘기한 거 재미있었어?")
              
        if answer[0][0] == "negative":
            cm.tts(bhv="do_joy_A", string=f"파이보는 {wm.word(self.user_name, 0)}랑 놀아서 재미있었어!")
            self.score = [0.0, -0.5, 0.0, 0.0]
        
        if answer[0][0] == "positive":
            cm.tts(bhv="do_joy_A", string=f"나도야! 다음에 또 재미있는 놀이 알려줄게.")
            self.score = [0.0, 0.5, 0.0, 0.0]
            
        if answer[0][0] != "negative" and answer[0][0] != "positive": # if answer[0][0] == "neutral":
            cm.tts(bhv="do_joy_A", string=f"{wm.word(self.user_name, 0)}랑 노는 건 정말 재미있어.")
            self.score = [0.0, -0.25, 0.0, 0.0]
        
        cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])

        # 종료 인사
        pibo = cm.tts(bhv="do_joy_A", string=f"나랑 놀아줘서 고마워~")

        # 4. Paradise framework 기록
        turns = sum((self.reject[i] + 1) * 2 for i in range(len(self.reject)))  
        reject = sum(self.reject) 
        
        cwc.writerow(['Turns', turns])
        cwc.writerow(['Rejections', reject])
        cwc.writerow(['Misrecognitions', ])

        cwc.writerow(['%Turns', ])
        cwc.writerow(['%Rejections', ])
        cwc.writerow(['%Misrecognitions', ])

        # 5. 활동 완료 기록
        gss.write_sheet(name=self.user_name, today=today, activities=filename)




if __name__ == "__main__":
    
    etq = Etiquette()
    etq.Object1()