num_x = 5
num_y = 10
mean_xy = (num_x + num_y) / 2
print(mean_xy)

num_x = 10
num_y = 70
mean_xy = (num_x + num_y) / 2
print(mean_xy)

num_x = 15
num_y = 3
mean_xy = (num_x + num_y) / 2
print(mean_xy)

# mean_cal(20, 40)

def mean_cal(num1, num2):
    res = (num1 + num2) / 2
    print(res)

mean_cal(5, 10)
# print(res)
mean_cal(10, 70)
mean_cal(15, 3)

def verb_like(subj, obj):
    msg = subj + " likes " + obj
    print(msg)

verb_like("John", "Mary")
verb_like("Mary", "John")