# Blue Print
class Car():
  wheels  = 4
  doors   = 4
  windows = 4
  seats   = 4

  # __str__ method override
  def __str__(self):
    return f"Car with {self.wheels} wheels"

  def __init__(self, *args, **kwargs):
    print(kwargs)
    self.wheels   = 4
    self.doors    = 4
    self.windows  = 4
    self.seats    = 4
    self.color    = kwargs.get("color", "black")
    self.price    = kwargs.get("price", "$20")
    


  #Function 과 Method 차이
  # Method : Function In Class
  def start(self):
    # self 는 자바의 this와 같다. 
    # Python Method First argumets is self
    print("I Started")

# Function
# def start():
#   print("I Started")


gm = Car()

# print(gm) == print(gm.__str__)
print(gm) 

kia = Car(color="green", price="$40")
print(kia.color, kia.price)
# dir은 Class안에 있는 모든 내용을 리스트로 보여준다.
# Java의 ToString과 비슷하다
# Properties를 보여준다.
print(dir(Car))

#Car classs의 instance == porche, ferrari 
porche = Car()
porche.color = "Red"
porche.start()

ferrari = Car()
ferrari.color = "Yellow"

mini = Car()
print(mini.color, mini.price)