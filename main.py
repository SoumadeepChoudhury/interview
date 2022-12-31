try:
    import pyttsx3
except:
    import COLORS
    print(f"{COLORS.RED}Libraries are not installed properly...Run {COLORS.YELLOW}`pip install -r requirements.txt` {COLORS.RED}and then re-run this application using 'python main.py'.{COLORS.RESET}")
    exit()
PX=pyttsx3.init()
cmds=["clear","nano","touch","python","python3","pip install -r","pip3 install -r"]

def loading() -> None:
    from time import sleep
    import COLORS
    inc=1
    for i in range(0,10):
        if i==9:
            print(f"\r{' '*20}",end='\r')
            break
        print(f"\r{COLORS.MAGENTA}Loading{'.'*inc}{COLORS.RESET}",end='\r')
        inc+=1
        if inc==5:
            inc=1
            print(f"\r{COLORS.MAGENTA}Loading {' '*10}{COLORS.RESET} ",end='\r')
        sleep(0.5)

def say(text:str,rate:int=150)->None:
    global PX
    PX.setProperty('rate',rate)
    PX.say(text)
    PX.runAndWait()


def run(cmd_code:int,args:str="")->None:
    import subprocess
    global cmds
    if args!="":
        cmd_run=subprocess.call([cmds[cmd_code],args])
    else:
        cmd_run=subprocess.Popen(cmds[cmd_code])
        cmd_run.wait()

def self_destruct()->None:
    import os
    import shutil
    path=os.getcwd().replace('\\','/')
    try:
        shutil.rmtree(path)
    except:
        pass


def main():
    try:
        import COLORS
        import requests as req
        import json
        import time
        import os
        import webbrowser
    except:
        print(f"{COLORS.RED}Libraries are not installed properly...Run {COLORS.YELLOW}`pip install -r requirements.txt` {COLORS.RED}and then re-run this application using 'python main.py'.{COLORS.RESET}")
        exit()
    name=input(f"{COLORS.RED}Enter your name: {COLORS.RESET}")
    run(0)
    say(f"Welcome {name} to the world's largest P P E Session, Hi, I am your virtual voice assistant. I will guide you through this session.")
    loading()
    print(f"{COLORS.CYAN}**Welcome {name} To The PPE session**{COLORS.RESET}")
    with open("incx.txt",'r') as file:
        read=file.read()
        print(read)
    input(f"{COLORS.YELLOW}Press enter to start...{COLORS.RESET}")
    run(0)
    loading()
    questions=[]
    extension=[]
    attempted=0
    viva=False
    next=True
    meet=''
    response=json.loads(req.get("https://soumadeepchoudhury.github.io/fetchapi/data.json").text)
    for i in response:
        try:
            questions.append(i['question'])
            extension.append(i['extension'])
        except:
            meet=i['meet']
    while True:
        if attempted<len(questions) and next==True:
            next=False
            print(COLORS.RED+"Q"+str(attempted+1)+". "+COLORS.GREEN+questions[attempted]+COLORS.RESET)
            say(questions[attempted],150)
            fileName=str(time.time()).split('.')[0]+"_"+str(attempted+1)+"."+extension[attempted]
            fileName=str(os.getcwd().replace('\\','/'))+'/res/'+fileName
            with open(fileName,'w') as file:
                if extension[attempted]=='py':
                    file.write(f'#{questions[attempted]}')
                elif extension[attempted]=='txt':
                    file.write(f'Q. {questions[attempted]}')
        userInp=input(f"{COLORS.YELLOW}[*]{COLORS.RESET} ")
        if userInp==":soln":
            run(1,fileName)
        elif userInp==":next":
            if attempted<len(questions)-1:
                checkPoint=input(f"{COLORS.RED}Are You Sure, you wanna permanently save your answer? No changes can be made after saving....[y/n] {COLORS.RESET}").lower()
                if checkPoint=='y':
                    print("\n\n")
                    next=True
                    attempted+=1
                    loading()
            else:
                print("All questions are over. Run :viva to attend the viva...")
        elif userInp==":run":
            print("\n",'--'*20,"\nRunning Code...\n",'--'*20,COLORS.BLUE)
            try:
                run(3,fileName)
            except:
                run(4,fileName)
            print("\n",COLORS.RESET)
        elif userInp==":viva":
            if attempted>=len(questions)-1:
                webbrowser.open_new(f"https://meet.google.com/{meet}")
                viva=True
            else:
                print(f"{COLORS.RED}Questions are not over..You need to complete all the questions before starting viva..{COLORS.RESET}")
        elif userInp==":submit":
            if attempted>=len(questions)-1 and viva==True:
                print(f"You need to follow the following instructions in order to send your responses for verification.\nOpen Gmail and compose a new email attach the {COLORS.RED}response.zip{COLORS.RESET} folder present in the {COLORS.BLUE}{os.getcwd()}{COLORS.RESET} and send it to {COLORS.YELLOW}ahensinitiative@gmail.com{COLORS.RESET}.")
                try:
                    import shutil
                    shutil.make_archive('responses','zip',str(os.getcwd().replace('\\','/')+'/res/'))
                    confirm=input(f"{COLORS.RED}Have You completed sending the file ?[y/n] You will not get back your responses after comfirming {COLORS.BLUE}'y'..  {COLORS.RESET}").lower()
                    if confirm == 'y':
                        loading()
                        print(f"Thank you {name} for joining the PPE Session...Results will be declared soon. Stay Tuned. Good Bye.") 
                        self_destruct()
                        break
                except:
                    print(f"Internal error in creating archive. Please select the res folder in order to send.")
                    confirm=input(f"{COLORS.RED}Have You completed sending the file ?[y/n] You will not get back your responses after comfirming {COLORS.BLUE}'y'..  {COLORS.RESET}").lower()
                    if confirm == 'y':
                        loading()
                        print(f"Thank you {name} for joining the PPE Session...Results will be declared soon. Stay Tuned. Good Bye.")
                        self_destruct()
                        break
            else:
                say("Questions or viva are not over...Do you wanna forcefully exit the session?")
                choice=input(f"{COLORS.RED}Questions or Viva are not over...Do you wanna forcefully exit the session?[y/n]{COLORS.RESET}").lower()
                if choice=='y':
                    say("Exiting the session.....Good Bye")
                    loading()
                    self_destruct()
                    break

        elif userInp==":help":
            print(f"{COLORS.BLUE}The valid commands are as follows:{COLORS.RESET}\n\t{COLORS.RED}:help{COLORS.RESET} -> MAN PAGE\n\t{COLORS.RED}:soln{COLORS.RESET} -> To provide response\n\t{COLORS.RED}:run{COLORS.RESET} -> To run code\n\t{COLORS.RED}:next{COLORS.RESET} -> To move to next question\n\t{COLORS.RED}:submit{COLORS.RESET} -> To finally submit all the responses.\n\t{COLORS.RED}:viva{COLORS.RESET} -> To start viva session.")
        else:
            print(f"{COLORS.RED}Invalid Command...run :help to check for valid commands{COLORS.RESET}")

if __name__=="__main__":
    try:
        main()
    except:
        exit()
