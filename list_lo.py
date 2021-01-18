
if __name__ == '__main__':

    food = ['rice', 'beans']
    food.append('broccoli')
    extra_food = ['bread', 'pizza']
    food.extend(extra_food)
    print(food[0:2])
    print(food[4])


    breakfast = 'eggs, fruit, orange juice'
    breakfast_list = breakfast.split(', ')
    print(breakfast_list)
    print(len(breakfast_list))

    user_values = (input('Please Enter Your Values. Enter "Stop" when finished: ')
    if input() == 'Stop'
        quit()
    average = sum(value_list) / len(value_list)
    print("Average: " + average)
    print("Max: " + max(value_list))
    print("Min: " + min(value_list))
    