def dTree(x):
    decision = ''
    if x['smoker'] == 'yes':
        if x['age'] > 29.5:
            decision = 'more riks'
        else:
            decision = 'less risks'
    elif x['smoker']=='no':
        if x['diet'] == 'poor':
            decision = 'more risk'
        elif x['diet']== 'good':
            decision = 'less risk'
    return decision

test=dTree({'smoker':'yes','age':31,'diet':'good'})
print test