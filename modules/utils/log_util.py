import time


def succeed(msg:str):
    current_time = time.strftime('[%H:%M:%S] ', time.localtime())
    return "%s<font color='green'>%s</font>"%(current_time,msg)

def fail(msg:str):
    current_time = time.strftime('[%H:%M:%S] ', time.localtime())
    return "%s<font color='red'>%s</font>" % (current_time,msg)