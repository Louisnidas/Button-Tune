# establish reference data
filename = "data.csv"
Metres = ["m", "metres", "metre", "meters", "meter"]
Yards = ["y", "yards", "yard"]


def get_distance():
    print("Metre or Yard distances?")
    unit = input()


    if (Metres.count(unit.lower()) != 0):
        dist = get_float()
        return dist + ", metres"
    
    elif (Yards.count(unit.lower()) != 0):
        dist = get_float()
        return dist + ", yards"
    
    else:   #loop if the unit is not accepted
        print("That unit was not recognised, please try another wording")
        return get_distance()

def get_float():
    print ("What distance is the target at?")
    dist = input()
    if (str(int(dist)) == dist):
        return dist
    else:
        print ("Please input an integer value")
        return get_float()

def get_target():
    print ("What size target face (in cm) are you shooting?")
    size = input()
    if (str(float(size)) == size or str(float(size)) == size + ".0"):
        return ", " + size
    else:
        print ("Please input a numerical value")
        return get_target()


def get_arrow_pos():
    print ("What score did the arrow land on?")
    print ("Feel free to add in decimal points for a more precise position - 4.5 for a line cutter between 4 and 5, for example")
    score = input()
    if (str(float(score)) == score or str(float(score)) == score + ".0"):
        if (float(score) <= 10.0 and float(score) >= 0.0):
            bearing = get_bearing()
            return ", " + score + bearing
        else:
            print ("That is not a valid arrow score")
            return get_arrow_pos()
    else:
        print ("Please input a numerical value")
        return get_arrow_pos()
    
def get_bearing():
        print ("What bearing from upwards is the arrow at?")
        print ("e.g. 270 for 9 o'clock or 090 for 3 o'clock")
        bearing = input()
        if ((str(int(bearing)) == bearing or "0"+str(int(bearing)) == bearing or "00"+str(int(bearing)) == bearing) and (int(bearing) >= 0 and int(bearing) < 360)):
            return ", " + bearing
        else:
            print ("That input was not valid, please reattempt")
            return get_bearing()


distance    = get_distance()
target_size = get_target()
position    = get_arrow_pos()

data = distance + target_size + position
with open(filename, "a") as f:
    f.write("\n")
    f.write(data)