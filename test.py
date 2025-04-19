# question 1
def question1():
    my_tuple = (0, 1, 2) #a
    my_tuple[2] = 4
    print(my_tuple[2])
    # ERROR

    my_str = "school" #b
    print(my_str[5: :-2]) 
    # "loc"

    cool_stuff = "Math is cool" #c
    print(cool_stuff.split())
    # ["Math", "is", "cool"]

    lst = [0, 1, 2, 3, 4] #d
    lst.insert(2, 3)
    print(lst)
    #[0, 1, 3, 2, 3, 4]

    lst = [0, 1, 2, 3, 4] #e
    print(lst.pop(2))  
    # 2

    lst = [0, 1, 2, 3, 4] #f
    lst.pop()
    lst.append(5)
    print(lst)
    # [0, 1, 2, 3, 5]

    dict = {"a": 0, "b": 1} #g
    dict["c"] = 2
    print(dict)
    #{“a”: 0, “b”: 1, “c”: 2}


    lst = [1, 2, 3, 4, 5, 6] #h
    new_lst = lst.reverse()
    print(new_lst[1]) 
    #ERROR

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

"""Output:
25 9 1
4
1
"""

# question3()


def question4():
    try:
        f = open('test_file.txt', 'r+')
    except FileNotFoundError as err:
        print('look here: \t',err)
        f = open('solid_file.txt','r+')
    finally:
        ct = 0
        for each in f.read():
            if each.isalpha():
                ct+=1
        f.write(f'ct: {ct}')
        f.close()

def question5():
    # does this code work? if not, what error does it give?
    s = "the 167 20 lazy 210 brown 78 87 2 fox 245 123"
    lst = s.split()
    count = 0
    for elem in lst:
        count += int(elem)
    print(count)


# question 6
def get_player_dict():
    player_dict = {}
    num_of_players = int(input("Number of players: "))
    for i in range(num_of_players):
            player_stats = get_player_stats() 
            # add player to dictionary with their stats
            # ... 
            player_dict[player_stats[0]] = (player_stats[1], player_stats[2])
    return player_dict

def get_player_stats(): # PART A)
    name = input("Player name: ")
    games_played = int(input("Games played: "))
    hits = int(input("Number of hits: "))
    pa = int(input("Number of plate appearances: "))
    bat_avg = hits / pa
    return (name, games_played, bat_avg)

"""
PART B)
player_dict[player_stats[0]] = (player_stats[1], player_stats[2]) 
"""
import copy
def question7():
    lst = [1,2,[3,4,5]]
    lst2 = lst[1:]
    lst3 = copy.deepcopy(lst)
    lst[2][2] = 0
    print(f"lst:{lst}\n lst2:{lst2}\n lst3:{lst3}")






    








