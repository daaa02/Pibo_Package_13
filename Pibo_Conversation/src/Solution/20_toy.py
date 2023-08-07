# -*- coding: utf-8 -*-

# 문제해결-친구들과 장난감 가지고 놀고 싶어

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


class Solution():    
    
    def __init__(self): 
        with open('/home/pi/name_config.json', 'r') as f:
            config = json.load(f)        
            self.user_name = config['user_name'] 
        self.score = []
        self.turns = []
        self.reject = []
                
        
    def Toy(self):
        
        # 1.1 문제 제시
        pibo = cm.tts(bhv="do_sad", string="친구들이랑 싸우지 않고 사이좋게 장난감을 가지고 놀고 싶어.")
        
        # 1.2 경험 질문
        pibo = cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 친구들이랑 어떤 장난감을 가지고 놀 때 제일 재밌니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"{wm.word(self.user_name, 0)}는 친구들이랑 어떤 장난감을 가지고 놀 때 제일 재밌니?",
                                   neu_bhv="do_compliment_S", neu="괜찮아. 생각이 나지 않을 수 있어.")
        
        pibo = cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)} 친구들은 장난감을 잘 양보해주니?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"{wm.word(self.user_name, 0)} 친구들은 장난감을 잘 양보해주니?",
                                   pos_bhv="do_joy_B", pos=f"{wm.word(self.user_name, 0)}는 멋진 친구들이 있구나!")
            
        pibo = cm.tts(bhv="do_question_L", string=f"다른 친구만 계속 장난감을 가지고 놀면 {wm.word(self.user_name, 0)}의 기분이 어떠니?")
        answer = cm.responses_proc(re_bhv="do_question_L", re_q=f"다른 친구만 계속 장난감을 가지고 놀면 {wm.word(self.user_name, 0)}의 기분이 어때?",
                                   neu_bhv="do_explain_A", neu=f"괜찮아. 바로 떠오르지 않을 수 있어. {wm.word(self.user_name, 0)}의 기분이 속상하지 않았을까?")
            
        pibo = cm.tts(bhv="do_question_S", string="장난감을 혼자서만 가지고 놀면 친구들이 싫어하겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="장난감을 혼자서만 가지고 놀면 친구들이 싫어하겠지?",
                                   pos_bhv="do_compliment_S", pos="같이 가지고 놀면 더 재미있을 것 같아!",
                                   neu_bhv="do_explain_B", neu="괜찮아. 모를 수도 있어. 그런데, 같이 가지고 놀면 더 재미있을 것 같아!",
                                   neg_bhv="do_compliment_S", neg="같이 가지고 놀면 더 재미있을 것 같아!",
                                   act_bhv="do_compliment_S", act="같이 가지고 놀면 더 재미있을 것 같아!")
            
        pibo = cm.tts(bhv="do_question_S", string="혼자 장난감을 가지고 노는 친구에게 뭐라고 말하는게 좋을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="혼자 장난감을 가지고 노는 친구에게 뭐라고 말하는게 좋을까?",
                                   neu_bhv="do_explain_C", neu="괜찮아. 말하기 어려울 수 있어. 같이 놀자. 라고 말해보면 어떨까?")
         
        pibo = cm.tts(bhv="do_question_L", string="장난감을 친구들이랑 사이좋게 가지고 노는 방법은 뭘까?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q="장난감을 친구들이랑 사이좋게 가지고 노는 방법은 뭘까?",
                                   pos_bhv="do_compliment_S", pos="서로 양보하면 사이좋게 놀 수 있겠다!",
                                   neu_bhv="do_explain_A", neu="찮아. 생각이 나지 않을 수 있어. 서로 양보하면 사이좋게 놀 수 있겠지?",
                                   act_bhv="do_compliment_S", act="서로 양보하면 사이좋게 놀 수 있겠다!")
        
        # 2.1 문제 해결
        pibo = cm.tts(bhv="do_joy_A", string="파이보도 이제는 친구들이랑 장난감을 가지고 놀 땐 다른 친구들도 생각하면서 재밌게 잘 놀아야 겠다. 알려줘서 정말 고마워!")
                            
        
        
        
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
    
    sol = Solution()
    sol.Toy()