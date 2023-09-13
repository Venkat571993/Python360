def car_brand(cars,index_input):
    try:
        awarded_car = cars[index_input]
        print(f"The best car brand award for this year: {awarded_car}")
    except IndexError:
        print("Error: Index Out of Range.")



cars = ["Hyundai","Suzuki","Audi","Benz","RR","Jeep"]

input_index = int(input("Enter the car code :"))

car_brand(cars,input_index)