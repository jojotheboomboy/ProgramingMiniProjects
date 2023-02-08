def estimatedRTT_func(e, s):
    newVal = (0.875*e) + (0.125*s)
    print("0.875*{} + 0.125*{}".format(e, s))
    print("{} + {} = {}\n".format(0.875*e,0.125*s, newVal))
    return newVal

def devRTT_func(d, e, s):
    k = (0.75*d) + (0.25*abs(s-e))
    print("0.75*{} + 0.25*|{} - {}|".format(d, s, e))
    print("{} + {} = {}\n".format(0.75*d,0.25*abs(s-e), k))
    return k

def timeoutInterval_func(d, e):
    j = e + 4*d
    print("{} + 4*{}".format(e, d))
    print("{} + {} = {}\n".format(e, 4*d, j))
    return j


estimatedRTT = 210.0
DevRTT = 17.0
timeout_interval = 0

array = [320.0, 270.0, 340.0]


for i in range(3): 
    estimatedRTT = estimatedRTT_func(estimatedRTT, array[i])
    DevRTT = devRTT_func(DevRTT, estimatedRTT, array[i])
    timeout_interval = timeoutInterval_func(DevRTT, estimatedRTT)
    print("EstimatedRTT = {}\t DevRTT = {}\t Timeout Interval = {}\n".format(estimatedRTT, DevRTT, timeout_interval))
    
    
    
    
