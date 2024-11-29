import customtkinter as ctk
import ctk_utils as ctku
import time,threading

ctk.CTk7SegmentDisplay=ctku.CTk7SegmentDisplay

ctk.CTkBlinkingColon=ctku.CTkBlinkingColon

ctk.set_appearance_mode("dark")
app=ctk.CTk()
app.title("Clock")
app.geometry("700x300")
app.configure(fg_color="black")

displayFrame=ctk.CTkFrame(app,width=500,height=250,fg_color="black",corner_radius=0)
displayFrame.pack(pady=40)

displays=[]

for i in range(2):
    display=ctk.CTk7SegmentDisplay(displayFrame,fg_color="black",width=100,height=200,thickness=15,segment_distance=5)
    display.grid(row=0,column=i,padx=10)
    displays.append(display)

colon=ctk.CTkBlinkingColon(displayFrame,width=20,height=200,fg_color="black")
colon.grid(row=0,column=2)

for i in range(4,6):
    display=ctk.CTk7SegmentDisplay(displayFrame,fg_color="black",width=100,height=200,thickness=15,segment_distance=5)
    display.grid(row=0,column=i,padx=10)
    displays.append(display)

for i in range(6,8):
    display=ctk.CTk7SegmentDisplay(displayFrame,fg_color="black",width=50,height=100,thickness=20,segment_distance=8)
    display.grid(row=0,column=i,padx=5,sticky="s")
    displays.append(display)

def setNumber(displays,number):
    strnum=str(number).rjust(6," ")[-6:]
    for i,c in enumerate(strnum):
        displays[i].setNumber(c)

def numberLoop():
    i=0
    while running:
        i+=1
        setNumber(displays,i)
        time.sleep(0.01)

def timeLoop():
    while running:
        ctime=time.time()
        current=time.localtime(ctime)
        hours=current.tm_hour
        minutes=current.tm_min
        seconds=current.tm_sec
        setNumber(displays,10000*hours+100*minutes+seconds)
        colon.setState((ctime-int(ctime))<0.5)
        time.sleep(0.5)

running=True

threading.Thread(target=timeLoop).start()

app.mainloop()

running=False
