
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

    user_values = float((input('Please Enter Your Values. Enter "Stop" when finished: '))
    print("Average: " + mean(user_values))
    print("Max: " + max(user_values))
    print("Min: " + min(user_values))
    