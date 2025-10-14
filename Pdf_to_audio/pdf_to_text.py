import pdfplumber 
from gtts import gTTS
import os


def pdf_to_speech(pdf_path,language,speed):
    filepath = pdf_path

    if not  os.path.exists(filepath):
        print("PDF Path not exist")
        return None

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            data = page.extract_text()

    language = language
    speed = speed.lower()

    if speed == 'no':
        myobj = gTTS(text=data,lang=language,slow=False)


    filename_with_extension = os.path.basename(pdf_path)
    filename,extension = os.path.splitext(filename_with_extension)
    myobj.save(f"E:\linkedinProjects\BankManagementProject\PythonMiniProjects\Pdf_to_audio\{filename}.mp3")
    print("Pdf converted into audio")

def play_audio(pdf_path):
    filename_with_extension = os.path.basename(pdf_path)
    filename = os.path.splitext(filename_with_extension)
    audio_path = f'E:\linkedinProjects\BankManagementProject\PythonMiniProjects\{filename}.mp3'
    if os.path.exists(audio_path+filename):
        os.system(f"start {audio_path}")


if __name__=="__main__":
    while True:
        print("#=======================================================")
        print("# PDF To Audio Converter ")
        print("#=======================================================")
        
        pdf_path = input("Paste the Pdf Path: ")
        language = input("Enter the Pdf language (en,ta,etc): ")
        speed = input("Can Audio is slow if yes enter [Yes,No]: ")

        #pdf to audio
        pdf_to_speech(pdf_path,language,speed)
        print("#=======================================================")

        #confirm do you want to listen audio
        confirm = input("Do You want play the Audi press [y/n]: ")
        if confirm.lower() == 'y':
            play_audio(pdf_path)
        print("#=======================================================")
        #exit loop
        choice = input("Do You want continue[y/n]: ")
        if choice.lower() == 'n':
            break
        print("#=======================================================")





