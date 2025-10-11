#============================================================
# 🤖 ChatGPT-based Chatbot
#============================================================

#import necessary packages
import google.generativeai as genai
import os
#from dotenv import load_dotenv

#============================================================
# Load API Key from .env file
#============================================================
#load_dotenv()
#api_key = os.getenv('OPENAI_API_KEY')
genai.configure(api_key='Your Api KEy')

model = genai.GenerativeModel("gemini-2.5-flash")

#============================================================
# Chatbot Function
#============================================================
def chat_with_chatgpt():
    print("Chat bot is Ready...! type 'exit' for quit")
    print("="*50)
    
    while True:
        user_input = input("You:")
        if user_input.lower() == 'exit':
            print("ChatGpt: Good Bye.. 👋🏻")

        reply = model.generate_content(user_input)
        print("Gemini:",reply.text)
        print("="*50)

if __name__=='__main__':
    chat_with_chatgpt() 