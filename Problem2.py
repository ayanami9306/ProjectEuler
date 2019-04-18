prev_Fibonacci = 1
curr_Fibonacci = 2
Sum = 0
while curr_Fibonacci < 4E6:
    if curr_Fibonacci % 2 == 0:
        Sum += curr_Fibonacci
    temp = prev_Fibonacci + curr_Fibonacci
    prev_Fibonacci = curr_Fibonacci
    curr_Fibonacci = temp
print(Sum)