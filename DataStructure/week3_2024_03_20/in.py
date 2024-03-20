"""
나라이름 목록에서
각 나라명이 동북아 3국이면
~는 동북아 3국 중 하나입니다. 출력
아니면
~는 동북아 3국에 포함되지 않습니다. 출력
"""

s = 'Thai/Miyanma/Vietnam/Japan/Taiwan/Korea/Singapore/China/Cambodia'

n = 'Korea/Japan/China'

splits = s.split('/')

splitn = n.split('/')

for i in splits:
    if i in n:
        print('{}는 동북아 3국 중 하나입니다.'.format(i))
    else:
        print('{}는 동북아 3국에 포함되지 않습니다.'.format(i))
                  
