from datetime import timedelta

HH, MM, SS = input("Hour, Minute, and Second to start (GMT+2)(HH:MM:SS) : ").split(":")
CH, CM, CS = input("Hour, Minute, and Second now      (GMT+7)(HH:MM:SS) : ").split(":")
HH, MM, SS = int(HH), int(MM), int(SS)
CH, CM, CS = int(CH), int(CM), int(CS)

stt = ((HH+5)*60*60) + (MM*60) + SS
now = ((CH)*60*60) + (CM*60) + CS

wait = stt-now

if wait < 0:
    print("See you on the next peer event!")
else:
    h = wait//3600
    m = (wait-h)//60
    s = (wait-h-m)
    print(f"{h:02d}:{m:02d}:{s:02d}")