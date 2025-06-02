isr = int(input('input Moodeng => "%" such as 50% Enter |50| : '))
print(f'number of percent: {isr}%')

rpc = (isr / 100) + 1
# print(f' percent:  {ry:.2f}'')

based = int(input("based starter: ")) 
rb = based * rpc

print(f'based({based}) + percent({isr}%) = {rb:.3f}')
