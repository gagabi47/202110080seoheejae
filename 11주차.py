#연습 11.1
#클래스
class Point :
  def __init__(self, x=0, y=0):
    self.__x = x
    self.__y = y

  def show(self) :
    print(f'({self.__x}, {self.__y})')

  def set(self, x, y) :
    self.__x = x
    self.__y = y

  def get(self):
    return(self.__x, self.__y)

#사용자 정의
def test():
  p1 = Point()
  p2 = Point(2, 3)

  p1.show() ;

  p1.set(10, 20) ; p1.show() ;

  p2.show();

  x, y = p2.get()
  print(f'x={x}, y={y}')

#주프
if __name__== '__main__' :
  test()


#11.2
#클래스
class Time :
  def __init__(self, hour=0, minute=0):
    self.__hour = hour
    self.__minute = minute

  def display(self):
    print(f'{self.__hour:02d}:{self.__minute:02d}') 

  def add(self, time):
    h = self.__hour + time.__hour
    m = self.__minute + time.__minute
    if m >= 60 :
      h += 1
      m -= 60
    return Time(h, m)

  @staticmethod
  def is_valid(hour, minute) :
    if 0<= hour < 24 and 0 <=minute < 60:
      return True
    return False

#사용
def main() :
  t1 =Time(9)
  t2 = Time(9, 30)

  t1.display()
  t2.display()

  later = t1.add(Time(1, 15))
  later.display()

  if Time.is_valid(25, 0) :
    print('유효한 시각')
  else:
    print('유효하지 않은 시각')

#주프
if __name__ == '__main__':
  main()

#11.3
#클래스
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1) 
        self.rb = Point(x2, y2) 

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.lt.getX()}, {self.lt.getY()})이고 '
              f'우측 하단 꼭지점이 ({self.rb.getX()}, {self.rb.getY()})인 사각형입니다.')

    def getWidth(self):
        return self.rb.getX() - self.lt.getX()

    def getHeight(self):
        return self.rb.getY() - self.lt.getY()

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

#주프
if __name__ == '__main__':
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()
    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')
