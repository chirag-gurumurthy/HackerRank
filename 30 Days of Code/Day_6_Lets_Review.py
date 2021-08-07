def eveodd(string):
    text_one = ''
    text_two = ''
    for index, value in enumerate(string):
        if index % 2 == 0:
            text_one += value
        elif index % 2 != 0:
            text_two += value
    
    print(text_one + " " + text_two)

test_cases = int(input())

for i in range(test_cases):
    test_string = str(input())
    eveodd(test_string)
