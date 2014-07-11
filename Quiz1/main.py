# Julian Rodriguez
# 7/10/14
# DPW Quiz1


##functions
width = raw_input("width?")
height = raw_input("height?")

def calc_area(w,h):
    area= w * h
    return area

if width == height or height == width:
    print "The area of this square is "+str(calc_area(int(width), int(height)))
elif width != height or height != width:
        print "The area of this rectangle is "+str(calc_area(int(width), int(height)))


###loop
raw_input("press enter")

bottles = 99

def count_down(a):
    global bottles
    bottles = bottles - a
    return bottles

while bottles > 0:
    print str(count_down(0))+ " Bottles of Beer on the Wall, "+ str(count_down(0)) +" Bottles of Beer.. take one down and pass it around. Now you have " + str(count_down(1))  + " bottles of beer on the wall!"
