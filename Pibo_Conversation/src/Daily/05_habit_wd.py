# -*- coding: utf-8 -*-

# 일상-평일 생활 습관 대화

import os, sys
import re
import csv
import random
from datetime import datetime
import time
import json
import time
import json
from datetime import datetime, timedelta
import schedule_run

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


class Daily():
    
    def __init__(self): 
        self.user_name = '다영'
        self.start_morning = '' # input("오전 시작 시간(HH:MM):") 
        self.delay = int        # int(input("알림 간격(MM):"))
        self.alarm = []           

    
    def morning(self, type):
        
        if type == 1:
            
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_wakeup", string="3밤만 자면 크리스마스야!")
            elif rand == 2:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_wakeup", string="해가 환하게 떴어! 일어나.")                
            elif rand == 3:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_wakeup", string="벌써 아침이야! 일어나!")
        
        if type == 2:
            
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_suggestion_L", string="좋은 아침이야! 부모님께 가서 인사하자.")
            elif rand == 2:
                pibo = cm.tts(bhv="do_suggestion_L", string="잘잤니? 부모님께 인사하는 거 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="굿모닝. 우리 같이 부모님께 아침 인사 하자.")
                
        if type == 3:
            
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_suggestion_L", string="식사 시간이야! 꼭꼭 씹어서 맛있게 먹자.")
            elif rand == 2:
                pibo = cm.tts(bhv="do_suggestion_L", string="밥 먹자. 딴 짓 하지 말고 맛있게 밥 먹자! ")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="아침 안 먹니? 우리 같이 맛있게 밥 먹자.")
                
        if type == 4:
                        
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_question_S", string="양치했어?")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="밥 먹고 양치하는 거 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="나랑 같이 양치하자")
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                
        if type == 5:
                        
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_question_L", string="오늘도 멋지게 옷 입었어?")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="오늘은 무슨 옷을 입을까? 멋지게 입어보자!")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="나랑 같이 단장할까? 멋지게 옷 입고 나도 꾸며줘!")
                
        if type == 6:
                        
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_joy_A", string="오늘도 선생님께 인사 잘하고 친구들과 사이좋게 지내.")
            elif rand == 2:
                pibo = cm.tts(bhv="do_joy_A", string="유치원 갈 시간이야! 친구들과 사이좋게 지내고 집에서 만나자.")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_joy_A", string="오늘도 재밌고 활기찬 유치원 생활을 보내고 나중에 만나서 얘기해 줘.")
                
    def afternoon(self, type):
        
        if type == 1:
            
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_suggestion_L", string="점심시간이야! 부모님께 감사 인사 드리고 맛있게 밥 먹자.")
            elif rand == 2:
                pibo = cm.tts(bhv="do_suggestion_L", string="밥먹자. 밥 먹기 전에 부모님께 감사 인사 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="점심 안 먹니? 우리 같이 부모님께 감사 인사 드리고 밥 먹자.")
                
        if type == 2:
                        
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_question_S", string="양치했어?")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="밥 먹고 양치하는 거 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="나랑 같이 양치하자")
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                
        if type == 3:
                        
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_question_S", string="어디 다녀왔어? 손 부터 씻을까?")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="왔구나! 손 씻기 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="나랑 같이 손 씻자!")
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
              
    def evening(self, type):                
       
        if type == 1:
            
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_suggestion_L", string="저녁시간이야! 부모님께 감사 인사 드리고 맛있게 밥 먹자.")
            elif rand == 2:
                pibo = cm.tts(bhv="do_suggestion_L", string="저녁시간이야! 부모님께 감사 인사 드리고 맛있게 밥 먹자.")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="저녁 안 먹니? 우리 같이 부모님께 감사 인사 드리고 밥 먹자.")
                 
        if type == 2:
            
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_question_S", string="양치했어?")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="밥 먹고 양치하는 거 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="나랑 같이 양치하자")
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                
        if type == 3:
            
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_suggestion_L", string="어질러진 방을 깨끗하게 정리하자!")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="다 놀았니? 정리하는 거 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="우리 같이 어질러진 물건을 정리하자.")
                                
        if type == 4:
            
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_suggestion_L", string="내일 준비물을 미리 챙기자!")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="준비물 미리 챙기는 거 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="우리 같이 준비물을 미리 챙겨볼까?")
                
        if type == 5:
                        
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_suggestion_L", string="큰 소리가 난 것 같아! 조용히 움직이자.")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="무슨 소리지? 늦은 시간에는 이웃에 방해가 되지 않도록 조용히 움직여야 해!")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="밤이 되었어. 우리 이제 조용히 움직이자!")
            
        if type == 6:
                        
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_suggestion_L", string="오늘의 특별한 일을 기록해 볼까?")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="일기쓰는 거 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="나랑 같이 일기쓸까? 오늘 있었던 이야기를 알려줘.")
            
        if type == 7:         
                    
            rand = random.randrange(1,4)  
            
            if rand == 1:
                # audio.audio_play(filename="/home/pi/AI_pibo2/src/data/audio/**")
                pibo = cm.tts(bhv="do_question_S", string="벌써 어두운 밤이네! 부모님께 인사 드리고 자자.")
            elif rand == 2:
                pibo = cm.tts(bhv="do_question_L", string="이제 잘까? 자기 전에 부모님께 인사 드리는 거 잊지 않았지?")                
            elif rand == 3:
                pibo = cm.tts(bhv="do_suggestion_L", string="피곤하지? 나랑 같이 부모님께 인사 드리고 자자.")
                
                
    def alarmtime(self, timeslot):      
        
        # 기상 시간 설정하고 몇 분 간격으로 알림 줄 것인지 결정할 수 있도록.
        # self.start_morning = input("오전 시작 시간(HH:MM):")    # 08:00
        # self.delay = int(input("알림 간격(MM):"))               # 30
        
        self.start_morning = datetime.strptime(self.start_morning, "%H:%M")
        
        for i in range(6):
            delaytime = self.start_morning + timedelta(minutes=(int(self.delay)*i))
            delaytime = datetime.strftime(delaytime, "%H:%M")            
            
            timeslot.append(delaytime) 
            
        return timeslot


    def Habit_weekend(self):
        timeslot = input("\n시간대(mor/aft/eve): ")
        while True:
            if timeslot in ['mor', 'aft', 'eve']:
                break
            else:
                timeslot = input("시간대(mor/aft/eve): ")
                continue
        self.start_morning = input("시작 시간(HH:MM): ") 
        self.delay = int(input("알림 간격(MM): "))
        
        mor = []
        # aft, eve = []
        # timeslot = []
        self.alarm = day.alarmtime(timeslot=timeslot)        
        print("schedule: ", timeslot)
        
        
        
        while True:
            schedule_run.run_pending()
            time.sleep(1)
    
    
if __name__ == '__main__':
    day = Daily()
    day.main()
    
        
        
    