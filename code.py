from tkinter import *
root = Tk()
root.title("HELP ME OUT WITH MY MOOD")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# FRAME
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)


lbl_title = Label(Top, text = "LET ME PREDICT YOUR MOOD", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")

lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

USERNAME = StringVar()
Login = StringVar()


username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)

 
import json
import tweepy 
from watson_developer_cloud import ToneAnalyzerV3
        
tone_analyzer = ToneAnalyzerV3(
version='2018-09-30',
username='35956e51-1250-46ea-87b8-ef7a4a6e9fdb',
password='xtJhBUG6xfNT',
url='https://gateway.watsonplatform.net/tone-analyzer/api'
)
         
        
        
        
        
        # Fill the X's with the credentials obtained by  
        # following the above mentioned procedure. 
consumer_key = "3jtFjAKzQ0uYCDIeZat29Tdjh" 
consumer_secret = "oUuqy8QASFqoA6YFo1o2IYerA9yNbByQvLJrHZ399bOXvGPRTK"
access_key = "981550201457467392-FJmPRmHKwokb5Chp0iFkVbf17qFcNIV"
access_secret = "DPPN7yhHPkpGebBZQ1EEDcfupC6h1zrqpdfReNjJjey7L"
          
        # Function to extract tweets 
def get_tweets(username): 
                          
                # Authorization to consumer key and consumer secret 
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
          
                # Access to user's access key and access secret 
                auth.set_access_token(access_key, access_secret) 
          
                # Calling api 
                api = tweepy.API(auth) 
          
                # 200 tweets to be extracted 
                number_of_tweets=25
                tweets = api.user_timeline(screen_name=username) 
          
                # Empty Array 
                tmp=[]  
          
                # create array of tweet information: username,  
                # tweet id, date/time, text 
                tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
                for j in tweets_for_csv: 
          
                    # Appending tweets to the empty array tmp 
                    tmp.append(j)  
                    tmp1=str(tmp)
                # Printing the tweets 
                
                tone_analysis = tone_analyzer.tone(
                {'text': tmp1},
                'application/json'
                ).get_result()
               # print(json.dumps(tone_analysis, indent=2))
                with open('tone_analysis', 'w', encoding='utf8') as outfile:
                    str_ = json.dumps(tone_analysis,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=True)
                    outfile.write(str_)
        
        # Read JSON file
                with open('tone_analysis') as data_file:
                    data_loaded = json.load(data_file)
                    list=[]
                    list1=(data_loaded['document_tone']['tones'])
                    #print(list1)
                    l=len(list1)
                    list2=[]
        
        
        
                    str_1=data_loaded['document_tone']['tones']    
                    with open('str_1', 'w', encoding='utf8') as outfile:
                            str_2 = json.dumps(str_1,
                                      indent=4, sort_keys=True,
                                      separators=(',', ': '), ensure_ascii=False)
                            outfile.write(str_2)
                    with open('str_1') as data_file1:
                        data_loaded1 = json.load(data_file1)
                    for i in range(0,l):
                        list2.append(data_loaded1[i]['score'])
                        maxscore=max(list2)
                        index=list2.index(maxscore)
                    root1 = Tk()
                    root1.title("HELP ME OUT WITH MY MOOD")
                    width = 400
                    height = 280
                    screen_width = root1.winfo_screenwidth()
                    screen_height = root1.winfo_screenheight()
                    x = (screen_width/2) - (width/2)
                    y = (screen_height/2) - (height/2)
                    root1.geometry("%dx%d+%d+%d" % (width, height, x, y))
                    root1.resizable(0, 0)
                    
                    # FRAME
                    
                    mood=data_loaded1[index]['tone_name']
                    if(mood=='Sadness'):
                      T = Text(root1, height=50, width=50)
                      T.pack()
                      quote = """               WELCOME DEAR
                    
                    
ROBOT:- hello your current mood is """+mood+""" 

>>don't worry dear i have suggestions to get out from your mood

>> below are some video link jusk copy it into  
browser and get relaxed

>>https://www.youtube.com/results?search_query=comedy+shows+(sadness) """
                     T.insert(INSERT, quote)
                    
                    
                    elif (mood=='Joy'):
                          T = Text(root1, height=50, width=50)
                          T.pack()
                          quote = """               WELCOME DEAR
                    
                    
ROBOT:- hello your current mood is """+mood+""" 

>>don't worry dear i have suggestions to get advantage for it

>> below are some video link jusk copy it into  
browser and get relaxed

>>https://www.youtube.com/results?search_query=beer+biceps+podcast(joy)"""
                          T.insert(INSERT, quote)
                     
                    elif (mood=='Anger'):
                          T = Text(root1, height=50, width=50)
                          T.pack()
                          quote = """               WELCOME DEAR
                    
                    
ROBOT:- hello your current mood is """+mood+""" 

>>don't worry dear i have suggestions to get advantage for it

>> below are some video link jusk copy it into  
browser and get relaxed

>>https://www.youtube.com/results?search_query=mr.bean+funny+videos(anger)"""
                          T.insert(INSERT, quote)
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
  def Login():    
       var=username.get()
       get_tweets(var)  

     

btn_login = Button(Form, text="Login", width=45, command= Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)
root.mainloop()
