def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    PI = 3.14
    area = PI * radius * radius
    return area

radius = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
area = get_circle_area(radius)
print(f"반지름 {radius}인 원의 넓이 = 3.14 x {radius} x {radius} = {area:.2f}")
