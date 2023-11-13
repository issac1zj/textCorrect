from paddlenlp import Taskflow
text_correction = Taskflow("text_correction")
print(text_correction('岩国陆战队航空站'))
'''
[{'source': '遇到逆竟时，我们必须勇于面对，而且要愈挫愈勇，这样我们才能朝著成功之路前进。',
    'target': '遇到逆境时，我们必须勇于面对，而且要愈挫愈勇，这样我们才能朝著成功之路前进。',
    'errors': [{'position': 3, 'correction': {'竟': '境'}}]}]
'''

# print(text_correction('人生就是如此，经过磨练才能让自己更加拙壮，才能使自己更加乐观。'))
'''
[{'source': '人生就是如此，经过磨练才能让自己更加拙壮，才能使自己更加乐观。',
    'target': '人生就是如此，经过磨练才能让自己更加茁壮，才能使自己更加乐观。',
    'errors': [{'position': 18, 'correction': {'拙': '茁'}}]}]
'''

