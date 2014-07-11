# Julian Rodriguez
# 7/10/14
# DPW Quiz1


##functions
def square_area(w,h):
    area= w * h
    return area

def rectangle_area(w,h):
    area= w * h
    return area

print "The area of this square is "+str(square_area(2, 100))

print "The area of this rectangle is "+str(rectangle_area(2, 20))

###loop

bottles = 99

def count_down(a):
    global bottles
    bottles = bottles - a
    return bottles

while bottles > 0:
    print str(count_down(0))+ " Bottles of Beer on the Wall, "+ str(count_down(0)) +" Bottles of Beer.. take one down and pass it around. Now you have " + str(count_down(1))  + " bottles of beer on the wall!"
