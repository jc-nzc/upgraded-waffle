def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


y = 700
def myfunc():
  print(y)

myfunc()

print(y)
