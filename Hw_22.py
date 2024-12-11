

#start
#basic python - final work 8 - 22
#8
student = {
'name': 'John',
'age': 20,
'hobbies': ['reading', 'games', 'coding'],}

def student_data(student):
    for key , value in student.items():
        print(f'{key} : {value}')

print(student_data(student))

def add_hobby(student,hobby):
    if hobby not in student['hobbies']:
        student['hobbies'].append(hobby)

print(student_data(student))
print(add_hobby("shalom", "football"))


# 9
def matrix(list1):
    for i in list1:
        for num in i:
            print(num, end= " ")
    print()


matrix1 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(matrix(matrix1))

#10
def zeros(list0):
    zero_times = 0
    for row in list0:
        for num in row:
            if num == 0:
                zero_times += 1
    print(zero_times)

matrix_0 =[
    [0,1,1],
    [0,1,0],
    [1,0,0]
    ]
print(zeros(matrix_0))

# 11
def repeated_num(list_n):
    result = {}
    for num in list_n:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    repeated = [num for num,count in result.items() if count > 1]

    return repeated
arr = [4,2,34,4,1,12,1,4]
print(f"result{repeated_num(arr)}")

# 12
list1_4 = [1,2,3,4]
def reverse_lst(list):
    rvrs = []
    for num in range(len(list)-1,-1,-1):
        rvrs.append(list[num])
    return rvrs

print(reverse_lst(list1_4))

#13
def same_pos_sum(l1,l2):
    summed_l = []
    for i in range(len(l1)):
        sum_l1_l2 = l1[i] + l2[i]
        summed_l.append(sum_l1_l2)
    return summed_l

    # i_0 = l1[0] + l2[0]
    # i_1 = l1[1] + l2[1]
    # i_2 = l1[2] + l2[2]
    # return i_0 ,i_1, i_2
print(same_pos_sum([4,6,7,],[8,1,9,]))

#14
def check_palind(w1,w2):
    if w1 == w1[::-1]:
        print("True")
    else:
        print("False")
    if w2 == w2[::-1]:
        print("True")
    else:
        print("False")

print(check_palind('racecar','java'))

#15
counter = 1
while counter < 100:
    counter *= 2
    print(counter)

#16
counter_50 = 900000
while counter_50 > 50:
    counter_50 = counter_50 / 2
    print(counter_50, end= " ")

#17
def repeated_word(strings):
    repeats = []
    seen = []
    index = 0

    while index < len(strings):
        current_string = strings[index]
        if current_string in seen:
            if current_string not in repeats:
                repeats.append(current_string)
        else:
            seen.append(current_string)
        index += 1

    return repeats

names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor','Chris','Kevin']

#18

def original_word(strings):
    seen = []
    index = 0
    while index < len(strings):
        current_string = strings[index]
        if current_string not in seen:
            seen.append(current_string)
        else:
            pass
        index += 1
    return seen

print(original_word(names))

# 19

def no_pete_word(strings):
    seen = []
    index = 0
    while index < len(strings):
        current_string = strings[index]

        if current_string not in seen and current_string != 'Pete':
            # if current_string == 'Pete': # why is not work?
            #     continue
            seen.append(current_string)
        else:
            pass
        index += 1
    return seen

print(no_pete_word(names))

# 20
def two_bool(bools):
    last_index = 0
    now_index = 1

    while now_index < len(bools):
        if bools[now_index] == bools[last_index]:
            return now_index
        last_index += 1
        now_index += 1
    else:
        return -1
print(two_bool([True, False, False]))

# 21
def user_input_name(shem: str):
    if len(shem.split()) == 2:
        print("True")
        return True #dosnt work
    else:
        print("False")
        return False # dosnt work

while True:
    user_name: str = input('user name? ')
    if user_input_name(user_name):
        break

def valid_age(a: int):
    if 0 < a <= 130:
        print('True')
    else:
        print('False')

age: int = int(input('age? '))
if valid_age(age):
    print("done")


def email(mail):
    if "@" in mail:
        print(True)
    else:
        print('false')

e_mail: str = input('email? ')
if email(e_mail):
    print("done")




