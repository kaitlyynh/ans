# question 1
def question1():
    my_tuple = (0, 1, 2) #a
    my_tuple[2] = 4
    print(my_tuple[2])

    my_str = "school" #b
    print(my_str[5: :-2]) 

    cool_stuff = "Math is cool" #c
    print(cool_stuff.split())

    lst = [0, 1, 2, 3, 4] #d
    lst.insert(2, 3)
    print(lst)

    lst = [0, 1, 2, 3, 4] #e
    print(lst.pop(2))  

    lst = [0, 1, 2, 3, 4] #f
    lst.pop()
    lst.append(5)
    print(lst)

    dict = {"a": 0, "b": 1} #g
    dict["c"] = 2
    print(dict)

    lst = [1, 2, 3, 4, 5, 6] #h
    new_lst = lst.reverse()
    print(new_lst[1]) 

# question 2
def display_triangle(symbol, n):
	for i in range(n):
		spaces = " " * (n - i + 1)
		fill = symbol * (2 * i + 1)
		print(spaces + fill)


def display_num_triangle(n):
    for row in range(1, n+1):
        for column in range(row, 0, -1):
            print(column, end=" ")
        print()

def question3():
    def func1(x):
        for i in range(x, 0, -2):
            print(i ** 2, end = " ")
        print()

    def func2(x):
        while x > 1:
            x //= 2
            func1(x)

    y = 10
    func2(y)

question3()



