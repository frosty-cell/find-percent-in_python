isr = int(input('input Moodeng => "%" such as 50% Enter |50| : '))
print(f'number of percent: {isr}%')

rpcP = (isr / 100) + 1
# print(f'percent factor: {rpcP:.2f}')
rpcM = (isr / 100)

based = int(input('based starter: ')) 
rbP = based * rpcP
rbM = based - (based * rpcM)

selection = str(input('select: minus or plus to solve your program ==> insert [ "-" or "+" ] '))
if (selection in ['-', 'minus']):
    print(f'based({based}) - percent({isr}%) = {rbM:.3f}')
elif (selection in ['+', 'plus']):
    print(f'based({based}) + percent({isr}%) = {rbP:.3f}')
else:
    print('Please Select again (Hint: only insert "-" or "+")')
