def answer(user_msg):
    msg = str(user_msg).lower()
    result=[]

    if msg in ['hello','hi','yo','sup']:
        return "Hello, (wave)"

    elif msg in ['i need a friend', 'be my friend', 'will you be my friend']:
        return "hi👋..\n\nMessage form creator: My bot took on my charactor and is a little introverted but i hope you treat my BlueBat as a friend"

    elif msg == "i am an idiot":
        return "Same"
    
    elif msg in ['time', 'time', 'what is the time']:
        from datetime import datetime as dt
        now = dt.now()
        return str(now.strftime("%d/%m/%y, %H:%M:%S"))

    elif msg == 'luck please':
        charm = " ᓚᘏᗢ \n 'the cat wishpers--meow'"
        return charm
        
    return user_msg
