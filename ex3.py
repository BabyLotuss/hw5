from itertools import zip_longest, islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В']

result = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(result))
print(*islice(result, 8))
print(list(islice(result, 3)))
