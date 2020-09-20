import turtle
import webbrowser
import time
import math
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
s.bgcolor(0,0,0)
s.colormode(255)
t.ht()
t.penup()
#ask which module they wish to use
while True:
    try:
        modulechoice = str(input("Welcome to spaceship, spaceship, SPACESHIP with Ben-ni, a fun game all about space! Would you like to play the gravity module, spectral analysis module, or the Mars mission module? "))
        break
    except ValueError:
        print("Sorry, please only enter text.")
choice = 0
x=1
y=1
z=1
#loop to ensure the choice goes through
while x==1:
    modulechoice.lower()
    if modulechoice == "gravity" or modulechoice == "gravity module":
        print("[Ben-ni]: Thank you for choosing the gravity module! I'm Ben-ni, your friendly astronaut guide to all things space. In the gravity module, we're going to have fun with seeing how much you weigh on different planets, and in space. Let's have some fun with WEIGHT!!")
        choice = 1
        x=0
    elif modulechoice == "spectral" or modulechoice == "spectral analysis" or modulechoice == "spectral analysis module":
        print("[Ben-ni]: Thank you for choosing the spectral analysis module! I'm Ben-ni, your friendly astronaut guide to all things space. In the spectral analysis module, we're going to have some fun with one of the coolest techniques in astronomy, and look at light to learn what stars are made of. Let's have some fun with LIGHT!!")
        choice = 2 
        x=0
    elif modulechoice == "mars" or modulechoice == "mars mission" or modulechoice == "mars mission module" or modulechoice =="mars module":
        print("[Ben-ni]: Thank you for choosing the Mars mission module. I'm Ben-ni, your friendly astronaut guide to all things space. In the Mars mission module, we're going to explore travel to Mars, one of my dreams. And it will have a spaceship! Let's have some fun with SPACE!!")
        choice = 3
        x=0
    else:
        modulechoice = str(input("I'm sorry, that didn't quite register. For the gravity module, enter gravity; for the spectral analysis module, enter spectral analysis; and for the Mars mission module, enter mars mission. "))
#start the gravity module
if choice == 1:
    #draw the planets
        t_one = t.clone()
        t_two = t.clone()
        t.goto(-150,50)
        t.pencolor((64,224,208))
        t.setheading(0)
        circlesegment = (100*3.14)/90
        t.fillcolor((64,224,208))
        t.pendown()
        t.begin_fill()
        for i in range (90):
            t.fd(circlesegment)
            t.right(4)
        t.end_fill()
        t.penup()
        t_one.goto(0,50)
        t_one.pencolor((64,224,208))
        t_one.setheading(0)
        circlesegment = (100*3.14)/90
        t_one.fillcolor((64,224,208))
        t_one.pendown()
        t_one.begin_fill()
        for i in range (90):
            t_one.fd(circlesegment)
            t_one.right(4)
        t_one.end_fill()
        #draw the people
        t_one.penup()
        t.goto(-140,49)
        t.pendown()
        t.pencolor((210,180,140))
        t.goto(-150,62)
        t.goto(-160,49)
        t.goto(-150,62)
        t.goto(-150,77)
        t.goto(-160,67)
        t.goto(-150,77)
        t.goto(-140,67)
        t.goto(-150,77)
        t.goto(-150,80)
        t.dot(8)
        t_one.goto(10,49)
        t_one.pendown()
        t_one.pencolor((210,180,140))
        t_one.goto(0,62)
        t_one.goto(-10,49)
        t_one.goto(0,62)
        t_one.goto(0,77)
        t_one.goto(-10,67)
        t_one.goto(0,77)
        t_one.goto(10,67)
        t_one.goto(0,77)
        t_one.goto(0,80)
        t_one.dot(8)
        t_two.goto(160,-1)
        t_two.pendown()
        t_two.pencolor((255,255,255))
        t_two.goto(150,12)
        t_two.goto(140,-1)
        t_two.goto(150,12)
        t_two.goto(150,27)
        t_two.goto(140,17)
        t_two.goto(150,27)
        t_two.goto(160,17)
        t_two.goto(150,27)
        t_two.goto(150,30)
        t_two.dot(8)
        t_two.pencolor((210,180,140))
        t_two.dot(5)
        #ask their weight
        print("[Ben-ni]: Shown is three versions of you, one on Earth, one on another planet, and one in space.")
        while True:
            try:
                weight_on_earth = int(input("[Ben-ni]: What is your weight on Earth in pounds? Please enter so I can figure our how much you weight on different planets."))
                if weight_on_earth > 1500:
                    print("Please enter your real weight")
                else:
                    break
            except ValueError:
                print("Please enter a whole number instead (don't spell out the number)")
        #calculate and write their weight and mass
        print("[Ben-ni]: Great! Now that I have your weight, we can figure out your weigh in deep space, and on another planet. But there's more! We can also figure out your mass. Mass is an idea similar to weight, it is a measure of how much 'stuff' you are made of absolutely, while weight refers to how 'heavy' you are. The difference lies in a mysterious and powerful force that we use every day, gravity. I'll explain more in a little bit, but first let's play around with seeing your weight on another planet.")
        earthwrite = "Your weigh on Earth is: " + str(weight_on_earth) + " pounds"
        mass = weight_on_earth/2.20462262185
        mass = mass*100
        mass = math.floor(mass)
        mass = mass/100
        masswrite = "Your mass is: " + str(mass) + " kilograms"
        t.penup()
        t.goto(-225,-75)
        t.pendown()
        t.pencolor(255,255,0)
        t.write(earthwrite,font=("Arial",8,"normal"))
        t.penup()
        t.goto(-225,-100)
        t.pendown()
        t.write(masswrite,font=("Arial",8,"normal"))
        t.penup()
        t.goto(170,-75)
        t.pendown()
        t.write("Your weight in deep space is: 0 pounds",font=("Arial",8,"normal"))
        t.penup()
        t.goto(170,-100)
        t.pendown()
        t.write(masswrite,font=("Arial",8,"normal"))
        while x == 0 or x == 2:
            y=1
            #clear the old text if their was already stuff written
            if x == 2:
                t.penup()
                t.goto(-35,-50)
                t.pendown()
                t.pencolor(0,0,0)
                t.fillcolor(0,0,0)
                t.begin_fill()
                t.goto(165,-50)
                t.goto(165,-100)
                t.goto(-35,-100)
                t.goto(-35,-50)
                t.end_fill()
            #ask for a planet choice
            while x == 0:
                try:
                    planetchoice = str(input("Please choose a planet from Mercury, Venus, Mars, Jupiter, Saturn, Uranus, or Neptune."))
                    planetchoice = planetchoice.lower()
                    if planetchoice == "mercury" or planetchoice == "venus" or planetchoice == "mars" or planetchoice == "jupiter" or planetchoice == "saturn" or planetchoice == "uranus" or planetchoice == "neptune":
                        x=1
                    else:
                        print("Sorry, that's not a choice. Please enter the name of the planet in the solar system you wish to choose.")
                except ValueError:
                    print("Sorry, that's not a choice. Please enter the name of the planet in the solar system you wish to choose.")
            #check the planet and change the appropriate variable for shifting weight
            if planetchoice == "mercury":
                factor = 3.7/9.81
                planet = "Mercury"
            if planetchoice == "venus":
                factor = 8.87/9.81
                planet = "Venus"
            if planetchoice == "mars":
                factor = 3.711/9.81
                planet = "Mars"
            if planetchoice == "jupiter":
                factor = 2.528
                planet = "Jupiter"
            if planetchoice == "saturn":
                factor = 10.44/9.81
                planet = "Saturn"
            if planetchoice == "uranus":
                factor = 8.69/9.81
                planet = "Uranus"
            if planetchoice == "neptune":
                factor = 11.15/9.81
                planet = "Neptune"
            weightanother = weight_on_earth*factor
            weightanother = weightanother*100
            weightanother = float(math.floor(weightanother))
            weightanother = weightanother/100
            #write out their weight
            if z  == 1:
                earthwrite = "Your weigh on " + str(planet) + " is: " + str((weightanother)) + " pounds"
            if z == 2:
                earthwrite = "Their weigh on " + str(planet) + " is: " + str((weightanother)) + " pounds"
            mass = weight_on_earth/2.20462262185
            mass = mass*100
            mass = math.floor(mass)
            mass = mass/100
            if z ==1:
                masswrite = "Your mass is: " + str(mass) + " kilograms"
            if z ==2:
                masswrite = "Their mass is: " + str(mass) + " kilograms"
            t.penup()
            t.goto(-35,-75)
            t.pendown()
            t.pencolor(255,255,0)
            t.write(earthwrite,font=("Arial",8,"normal"))
            t.penup()
            t.goto(-35,-100)
            t.pendown()
            t.write(masswrite,font=("Arial",8,"normal"))
            #ask if they want to go again
            while y == 1:
                try:
                    planetagain = str(input("Would you like to explore weight more by seeing your weight on another planet? "))
                    planetagain = planetagain.lower()
                    if planetagain == "yes" or planetagain == "y":
                        print("Great!")
                        planetagain = "yes"
                        x=2
                        y=2
                    else:
                        y=2
                except ValueError:
                    print("Sorry, that was unclear. Enter 'yes' for yes and 'no' for no.")
            #choose a new planet if they want to go again
            if planetagain == "yes":
                while y == 2:
                    try:
                        planetchoice = str(input("Please choose a planet from Mercury, Venus, Mars, Jupiter, Saturn, Uranus, or Neptune."))
                        planetchoice = planetchoice.lower()
                        if planetchoice == "mercury" or planetchoice == "venus" or planetchoice == "mars" or planetchoice == "jupiter" or planetchoice == "saturn" or planetchoice == "uranus" or planetchoice == "neptune":
                            y=1
                        else:
                            print("Sorry, that's not a choice. Please enter the name of the planet in the solar system you wish to choose.")
                    except ValueError:
                        print("Sorry, that's not a choice. Please enter the name of the planet in the solar system you wish to choose.")
            y=1
            #ask if they want to go again with a new weight
            weightagain = "no"
            if planetagain != "yes":
                while y == 1:
                    try:
                        weightagain = str(input("Would you like to play again, but using the weight of someone else you know this time?"))
                        weightagain = weightagain.lower()
                        if weightagain == "yes" or weightagain == "y":
                            print("Great!")
                            weightagain = "yes"
                            y = 2
                            x=2
                        else:
                            y=2
                    except ValueError:
                        print("Sorry, that was unclear. Enter 'yes' for yes and 'no' for no.")
            y=2
            if weightagain == "yes":
                #erase old text
                t.penup()
                t.goto(-225,-50)
                t.pendown()
                t.pencolor(0,0,0)
                t.fillcolor(0,0,0)
                t.begin_fill()
                t.goto(300,-50)
                t.goto(300,-100)
                t.goto(-225,-100)
                t.goto(-225,-50)
                t.end_fill()
                #re-ask all the part about the weight and mass
                while y==2:
                    try:
                        weight_on_earth = int(input("[Ben-ni]: What is the weight on Earth in pounds of the person you would like to calculate have their weight on another planet calculated? Please enter so I can figure our how much they weight on different planets."))
                        if weight_on_earth > 1500:
                            print("Please enter a real weight")
                        else:
                            y=1
                    except ValueError:
                        print("Please enter a whole number instead (don't spell out the number)")
                print("[Ben-ni]: Great! Now that I have their weight, we can figure out their weigh in deep space, and on another planet. But there's more! We can also figure out theur mass. Mass is an idea similar to weight, it is a measure of how much 'stuff' you are made of absolutely, while weight refers to how 'heavy' you are. The difference lies in a invisible and powerful force that we use every day, gravity. I'll explain more in a little bit, but first let's play around with seeing weight on another planet.")
                earthwrite = "Their weigh on Earth is: " + str(weight_on_earth) + " pounds"
                #re-calculate weight and mass
                mass = weight_on_earth/2.20462262185
                mass = mass*100
                mass = math.floor(mass)
                mass = mass/100
                masswrite = "Their mass is: " + str(mass) + " kilograms"
                #re-write new text
                t.penup()
                t.goto(-225,-75)
                t.pendown()
                t.pencolor(255,255,0)
                t.write(earthwrite,font=("Arial",8,"normal"))
                t.penup()
                t.goto(-225,-100)
                t.pendown()
                t.write(masswrite,font=("Arial",8,"normal"))
                t.penup()
                t.goto(170,-75)
                t.pendown()
                t.write("Their weight in deep space is: 0 pounds",font=("Arial",8,"normal"))
                t.penup()
                t.goto(170,-100)
                t.pendown()
                t.write(masswrite,font=("Arial",8,"normal"))
                z=2
        print("[Ben-ni]: I hope you had fun playing around with weights on other planets! As you probably saw through playing around with weights on other planets, weight in deep space is always zero and mass for a given person is always the same, but weight can change on other planets. This is because other planets have different amounts of gravity. Gravity is that invisible, powerful force I was talking about earlier. It's a force of an attraction, making everything in the universe 'pull' each other together. However, that pull is very weal for most things, so weak we can't feel or even notice it. For really massive things, like planets, it is definetly noticible, because the more mass something has, the more it 'pulls' other things towards it. Gravity is what pulls us towards the Earth and prevents us from flying away, or jumping as high as we want. Because other planets have more or less mass, they have a stronger or weaker gravity, and 'pull' things more or less. So, on Mercury, which has not a lot of mass, the 'pull' isn't very strong. But on Jupiter, which does have a lot of mass, it is very strong.")
        z=1
        #ask if they want more info
        while z ==1:
            try:
                moreinfograv = str(input("Would you like to view more info on gravity?"))
                if moreinfograv == "yes" or moreinfograv == "y":
                    moreinfograv = moreinfograv = "yes"
                    z = 2
                else:
                    z=2
            except ValueError:
                print("Sorry, don't quite understand. Please enter 'yes' for yes, and 'no' for no.")
        if moreinfograv == "yes":
            webbrowser.open('https://spaceplace.nasa.gov/what-is-gravity/en/', new=2)
        print("Thanks for playing the gravity module in spaceship, spaceship, SPACESHIP with Ben-ni! Come again soon!")
#start the spectral analysis module
if choice == 2:
    #draw the spectrums
    t.penup()
    t.goto(-100,100)
    t.pencolor(255,255,255)
    t.pendown()
    t.goto(-20,100)
    t.goto(-20,80)
    t.goto(-100,80)
    t.goto(-100,100)
    t.penup()
    t.goto(-30,100)
    t.pendown()
    t.width(2)
    t.pencolor(255,0,0)
    t.goto(-30,80)
    t.penup()
    t.pencolor(50,255,50)
    t.goto(-65,100)
    t.pendown()
    t.goto(-65,80)
    t.penup()
    t.pencolor(0,0,215)
    t.goto(-77,100)
    t.pendown()
    t.goto(-77,80)
    t.penup()
    t.pencolor(148,0,211)
    t.goto(-85,100)
    t.pendown()
    t.goto(-85,80)
    t.width(1)
    t.penup()
    t.goto(0,50)
    t.pencolor(255,255,255)
    t.pendown()
    t.goto(80,50)
    t.goto(80,30)
    t.goto(0,30)
    t.goto(0,50)
    t.penup()
    t.goto(70,50)
    t.pendown()
    t.width(2)
    t.pencolor(255,0,0)
    t.goto(70,30)
    t.penup()
    t.pencolor(50,255,50)
    t.goto(35,50)
    t.pendown()
    t.goto(35,30)
    t.penup()
    t.pencolor(0,0,215)
    t.goto(23,50)
    t.pendown()
    t.goto(23,30)
    t.penup()
    t.pencolor(148,0,211)
    t.goto(15,50)
    t.pendown()
    t.goto(15,30)
    t.width(1)
    t.penup()
    t.goto(0,100)
    t.pencolor(255,255,255)
    t.pendown()
    t.goto(80,100)
    t.goto(80,80)
    t.goto(0,80)
    t.goto(0,100)
    t.penup()
    t.width(1)
    t.penup()
    t.goto(-100,50)
    t.pencolor(255,255,255)
    t.pendown()
    t.goto(-20,50)
    t.goto(-20,30)
    t.goto(-100,30)
    t.goto(-100,50)
    t.penup()
    t.width(1)
    t.penup()
    t.goto(-100,0)
    t.pencolor(255,255,255)
    t.pendown()
    t.goto(-20,0)
    t.goto(-20,-20)
    t.goto(-100,-20)
    t.goto(-100,0)
    t.penup()
    t.width(1)
    t.penup()
    t.goto(-100,-50)
    t.pencolor(255,255,255)
    t.pendown()
    t.goto(-20,-50)
    t.goto(-20,-70)
    t.goto(-100,-70)
    t.goto(-100,-50)
    t.penup()
    t.width(1)
    t.penup()
    t.goto(0,0)
    t.pencolor(255,255,255)
    t.pendown()
    t.goto(80,0)
    t.goto(80,-20)
    t.goto(0,-20)
    t.goto(0,0)
    t.penup()
    t.width(1)
    t.penup()
    t.goto(0,-50)
    t.pencolor(255,255,255)
    t.pendown()
    t.goto(80,-50)
    t.goto(80,-70)
    t.goto(0,-70)
    t.goto(0,-50)
    t.penup()
    t.width(2)
    t.goto(-27,50)
    t.pencolor(255,0,0)
    t.pendown()
    t.goto(-27,30)
    t.penup()
    t.width(1)
    t.goto(-24,50)
    t.pencolor(210,0,0)
    t.pendown()
    t.goto(-24,30)
    t.penup()
    t.width(4)
    t.pencolor(255,255,0)
    t.goto(-50,50)
    t.pendown()
    t.goto(-50,30)
    t.penup()
    t.goto(-65,50)
    t.pendown()
    t.width(2)
    t.pencolor(50,255,50)
    t.goto(-65,30)
    t.penup()
    t.goto(-75,50)
    t.pendown()
    t.pencolor(50,255,150)
    t.goto(-75,30)
    t.penup()
    t.goto(-95,50)
    t.width(1)
    t.pendown()
    t.pencolor(130,0,200)
    t.goto(-95,30)
    t.penup()
    t.width(2)
    t.goto(73,-50)
    t.pencolor(255,0,0)
    t.pendown()
    t.goto(73,-70)
    t.penup()
    t.width(1)
    t.goto(76,-50)
    t.pencolor(210,0,0)
    t.pendown()
    t.goto(76,-70)
    t.penup()
    t.width(4)
    t.pencolor(255,255,0)
    t.goto(50,-50)
    t.pendown()
    t.goto(50,-70)
    t.penup()
    t.goto(35,-50)
    t.pendown()
    t.width(2)
    t.pencolor(50,255,50)
    t.goto(35,-70)
    t.penup()
    t.goto(25,-50)
    t.pendown()
    t.pencolor(50,255,150)
    t.goto(25,-70)
    t.penup()
    t.goto(5,-50)
    t.width(1)
    t.pendown()
    t.pencolor(130,0,200)
    t.goto(5,-70)
    t.penup()
    t.goto(-40,0)
    t.width(1)
    t.pencolor(0,210,0)
    t.pendown()
    t.goto(-40,-20)
    t.penup()
    t.goto(-30,0)
    t.pencolor(210,0,0)
    t.pendown()
    t.goto(-30,-20)
    t.penup()
    t.goto(-25,0)
    t.pencolor(180,0,0)
    t.pendown()
    t.goto(-25,-20)
    t.penup()
    t.goto(60,100)
    t.width(1)
    t.pencolor(0,210,0)
    t.pendown()
    t.goto(60,80)
    t.penup()
    t.goto(70,100)
    t.pencolor(210,0,0)
    t.pendown()
    t.goto(70,80)
    t.penup()
    t.goto(75,100)
    t.pencolor(180,0,0)
    t.pendown()
    t.goto(75,80)
    t.penup()
    t.goto(70,0)
    t.pencolor(255,255,0)
    t.pendown()
    t.goto(70,-20)
    t.penup()
    t.goto(75,0)
    t.pendown()
    t.pencolor(235,235,0)
    t.pendown()
    t.goto(75,-20)
    t.penup()
    t.goto(-30,-50)
    t.pencolor(255,255,0)
    t.pendown()
    t.goto(-30,-70)
    t.penup()
    t.goto(-25,-50)
    t.pendown()
    t.pencolor(235,235,0)
    t.pendown()
    t.goto(-25,-70)
    t.penup()
    t.pencolor(255,255,255)
    t.goto(-100,105)
    t.pendown()
    t.write("Hydrogen",font=("Arial",8,"normal"))
    t.penup()
    t.goto(-100,55)
    t.pendown()
    t.write("Helium",font=("Arial",8,"normal"))
    t.penup()
    t.goto(-100,5)
    t.pendown()
    t.write("Oxygen",font=("Arial",8,"normal"))
    t.penup()
    t.goto(-100,-44)
    t.pendown()
    t.write("Sodium",font=("Arial",8,"normal"))
    t.penup()
    t.goto(0,105)
    t.pendown()
    t.write("A",font=("Arial",8,"normal"))
    t.penup()
    t.goto(0,55)
    t.pendown()
    t.write("B",font=("Arial",8,"normal"))
    t.penup()
    t.goto(0,5)
    t.pendown()
    t.write("C",font=("Arial",8,"normal"))
    t.penup()
    t.goto(0,-44)
    t.pendown()
    t.write("D",font=("Arial",8,"normal"))
    t.penup()
    #have them guess all the elements
    print("[Ben-ni]: Shown are the emission spectra for several elements. You may be wondering what an emission spectrum is, and what an element is. Elements are the building blocks of the universe, comprising all of the things in the universe. When these elements are spread really thin, they can let light go through them, and 'split' it, making a rainbow. A rainbow is a type of spectrum. All a spectrum is is a collection of lights. When things get really hot, thousands of times hotter than a summer day, things start to glow, and light up. The sprectra shown are a sort of rainbow that you can see by looking at really hot versions of the elements through a prism, which is a triangular wedge of glass. Stars are me up of really hot elements, and by looking at them through a telescope and a prism, astronomers can see the 'rainbows' made by the elements in the star, and figure out what they're made of, which is pretty neat. Do you know another way of figuring out what things too far away to imagine are made of? I don't. Let's have some fun matching the known element's spectra, on the left, with the mystery ones on the right.")
    while True:
        try:
            elementa = str(input("Which element do you think mystery spectrum 'A' is of?"))
            elementa = elementa.lower()
            if elementa == "oxygen":
                print("[Ben-ni]: Spot on! Oxygen is very important for many kinds of life on Earth, and astronomers use the spectra of oxygen to help gauge if planets in other solar systems might have aliens.")
                break
            elif elementa == "hydrogen" or elementa == "helium" or elementa == "sodium":
                print("Sorry, that's incorrect. Try again!")
            else:
                print("Sorry, didn't quite understand that. To guess Hydrogen, enter 'hydrogen'; to guess Helium, enter 'helium'; to guess Sodium, enter 'sodium'.")
        except ValueError:
            print("Sorry, didn't quite understand that. To guess Hydrogen, enter 'hydrogen'; to guess Helium, enter 'helium'; to guess Sodium, enter 'sodium'.")
    while True:
        try:
            elementb = str(input("Which element do you think mystery spectrum 'B' is of?"))
            elementb = elementb.lower()
            if elementb == "hydrogen":
                print("[Ben-ni]: Spot on! Hydrogen is the most common element in the universe..")
                break
            elif elementb == "oxygen" or elementb == "helium" or elementb == "sodium":
                print("Sorry, that's incorrect. Try again!")
            else:
                print("Sorry, didn't quite understand that. To guess Hydrogen, enter 'hydrogen'; to guess Helium, enter 'helium'; to guess Sodium, enter 'sodium'.")
        except ValueError:
            print("Sorry, didn't quite understand that. To guess Hydrogen, enter 'hydrogen'; to guess Helium, enter 'helium'; to guess Sodium, enter 'sodium'.")
    while True:
        try:
            elementc = str(input("Which element do you think mystery spectrum 'C' is of?"))
            elementc =elementc.lower()
            if elementc == "sodium":
                print("[Ben-ni]: Spot on! Sodium is one of the two elements in salt, along with chlorine.")
                break
            elif elementc == "hydrogen" or elementc == "helium" or elementc == "oxygen":
                print("Sorry, that's incorrect. Try again!")
            else:
                print("Sorry, didn't quite understand that. To guess Hydrogen, enter 'hydrogen'; to guess Helium, enter 'helium'; to guess Sodium, enter 'sodium'.")
        except ValueError:
            print("Sorry, didn't quite understand that. To guess Hydrogen, enter 'hydrogen'; to guess Helium, enter 'helium'; to guess Sodium, enter 'sodium'.")
    while True:
        try:
            elementd = str(input("Which element do you think mystery spectrum 'D' is of?"))
            elementd = elementd.lower()
            if elementd == "helium":
                print("[Ben-ni]: Spot on! There's Helium in many balloons. It also makes your voice sound squeaky if you inhale it!")
                break
            elif elementd == "hydrogen" or elementd == "oxygen" or elementd == "sodium":
                print("Sorry, that's incorrect. Try again!")
            else:
                print("Sorry, didn't quite understand that. To guess Hydrogen, enter 'hydrogen'; to guess Helium, enter 'helium'; to guess Sodium, enter 'sodium'.")
        except ValueError:
            print("Sorry, didn't quite understand that. To guess Hydrogen, enter 'hydrogen'; to guess Helium, enter 'helium'; to guess Sodium, enter 'sodium'.")
    print("[Ben-ni]: Congratulations! You have successfully determined all of the elements. I'd bet you'll make a great astronomer one day.")
    #ask if they want more info
    while True:
        try:
            moreinfospect = str(input("Would you like more info on spectrums?"))
            moreinfospect = moreinfospect.lower()
            if moreinfospect == "yes" or moreinfospect == "y":
                print("Great!")
                moreinfospect = "yes"
                break
            else:
                break
        except ValueError:
            print("Sorry, didn't quite understand that. For yes, enter 'yes', and for no, enter 'no'.")
    if moreinfospect == "yes":
        webbrowser.open("http://loke.as.arizona.edu/~ckulesa/camp/spectroscopy_intro.html", new=2)
    print("Thanks for playing the spectral analysis module of spaceship, spaceship, SPACESHIP with Ben-ni. Come again soon!")
#start the Mars mission module
if choice == 3:
    spaceshipparts=[]
    print("[Ben-ni]: In order to get to Mars, we have to build a spaceship. And not just any spaceship. We have to build one that's great. Let's build a great spaceship!")
    w = 1
    #start the mars mission adding rocket parts loop
    while True:
        #mars mission which part ask loop
        while w ==1:
            try:
                newestpart = str(input("which part would you like to add to your spaceship next? An air scrubber, a food storage unit, a gym, a hull, an engine, fuel tanks, or a water slide? "))
                newestpart = newestpart.lower()
                if newestpart in spaceshipparts:
                    print("Sorry, you already have that part on your spaceship.")
                elif newestpart == "air scrubber" or newestpart == "food storage" or newestpart == "gym" or newestpart == "hull" or newestpart == "engine" or newestpart == "fuel tanks" or newestpart == "water slide":
                    w = 2
                else:
                    print("Sorry, don't quite understand. For an air scrubber, enter 'air scrubber'; for a food storage unit, enter 'food storage'; for a gym, enter 'gym'; for a hull, enter 'hull'; for an engine, enter 'engine'; for fuel tanks, enter 'fuel tanks'; and for a water slide, enter 'water slide'. ")
            except ValueError:
                print("Sorry, don't quite understand. For an air scrubber, enter 'air scrubber'; for a food storage unit, enter 'food storage'; for a gym, enter 'gym'; for a hull, enter 'hull'; for an engine, enter 'engine'; for fuel tanks, enter 'fuel tanks'; and for a water slide, enter 'water slide'. ")
        w=1
        #list of parts and code for graphics and text
        if newestpart == "air scrubber":
            print("[Ben-ni]: Great choice! There's no air in space, so the only air the astronauts have is that which they bring with them. Air scrubbers will turn carbon dioxide, the gas that we breath out, into oxygen, which we can breath in.")
            spaceshipparts.append(newestpart)
            t.pencolor(128,128,128)
            t.penup()
            t.goto(150,-150)
            t.pendown()
            t.dot(50)
            t.pencolor(59,59,59)
            t.dot(25)
            t.penup()
            t.goto(120,-190)
            t.pendown()
            t.pencolor(255,255,255)
            t.write("Air scrubber",font=("Arial",8,"normal"))
        elif newestpart == "food storage":
            print("[Ben-ni]: Good choice! A journey to Mars would take several months at best, and their are no grocery stores on the way, so we have to bring all our food with us.")
            spaceshipparts.append(newestpart)
            t.penup()
            t.goto(110,-30)
            t.pencolor(128,128,128)
            t.fillcolor(50,255,50)
            t.begin_fill()
            t.pendown()
            t.goto(180,-30)
            t.goto(180,-70)
            t.goto(110,-70)
            t.goto(110,-30)
            t.penup()
            t.end_fill()
            t.goto(110,-90)
            t.write("Food storage",font=("Arial",8,"normal"))
        elif newestpart == "gym":
            print("[Ben-ni]: Great decision! Because there is no gravity (the force that pulls us all to the Earth) in space, your muscles and bones aren't constantly working to keep you from being pulled to the Earth, so they weaken. A gym will help us rebuild our muscles.")
            spaceshipparts.append(newestpart)
            t.penup()
            t.goto(10,-30)
            t.pencolor(128,128,128)
            t.fillcolor(128,128,128)
            t.begin_fill()
            t.pendown()
            t.goto(80,-30)
            t.goto(80,-70)
            t.goto(10,-70)
            t.goto(10,-30)
            t.penup()
            t.end_fill()
            t.goto(10,-90)
            t.write("Gym",font=("Arial",8,"normal"))
        elif newestpart == "hull":
            print("[Ben-ni]: Good choice! With out the Earth's atmosphere to stop it, there is lots of dangerous radiation(tiny little particles moving very fast that can damage things) in space. A hull will help protect us against that.")
            spaceshipparts.append(newestpart)
            t.penup()
            t.goto(-20,-130)
            t.pencolor(128,128,128)
            t.fillcolor(255,255,255)
            t.begin_fill()
            t.pendown()
            t.goto(50,-130)
            t.goto(110,-150)
            t.goto(50,-170)
            t.goto(-20,-170)
            t.goto(-20,-130)
            t.penup()
            t.end_fill()
            t.goto(-20,-190)
            t.write("Hull",font=("Arial",8,"normal"))
        elif newestpart == "engine":
            print("[Ben-ni]: Excellent idea! Without engines, you can't go anywhere.")
            spaceshipparts.append(newestpart)
            t.penup()
            t.goto(-140,-30)
            t.pencolor(169,169,169)
            t.fillcolor(169,169,169)
            t.begin_fill()
            t.pendown()
            t.goto(-70,-30)
            t.goto(-70,-70)
            t.goto(-140,-70)
            t.goto(-140,-30)
            t.penup()
            t.end_fill()
            t.fillcolor(255,0,0)
            t.pencolor(255,0,0)
            t.goto(-70,-30)
            t.begin_fill()
            t.pendown()
            t.goto(-10,-50)
            t.goto(-70,-70)
            t.goto(-70,-30)
            t.penup()
            t.end_fill()
            t.goto(-90,-90)
            t.write("Engine",font=("Arial",8,"normal"))
        elif newestpart == "fuel tanks":
            print("[Ben-ni]: Good idea. You need extra fuel to go to Mars, since it's a long way away.")
            spaceshipparts.append(newestpart)
            t.penup()
            t.goto(-140,-130)
            t.pencolor(169,169,169)
            t.fillcolor(169,169,169)
            t.begin_fill()
            t.pendown()
            t.goto(-70,-130)
            t.goto(-70,-140)
            t.goto(-140,-140)
            t.goto(-140,-130)
            t.penup()
            t.end_fill()
            t.goto(-140,-160)
            t.pencolor(169,169,169)
            t.fillcolor(169,169,169)
            t.begin_fill()
            t.pendown()
            t.goto(-70,-160)
            t.goto(-70,-170)
            t.goto(-140,-170)
            t.goto(-140,-160)
            t.penup()
            t.end_fill()
            t.goto(-140,-190)
            t.write("Fuel Tanks",font=("Arial",8,"normal"))
        elif newestpart == "water slide":
            print("[Ben-ni]: Nice try. Water slides are fun, but getting things into space is expensive. You have to buy and then burn a lot of fuel to get anything into space. So I'm not sure adding a water slide in practical.")
        #code for completed rocket with launch sequence
        if "air scrubber" in spaceshipparts and "food storage" in spaceshipparts and "gym" in spaceshipparts and "hull" in spaceshipparts and "engine" in spaceshipparts and "fuel tanks" in spaceshipparts:
            print("[Ben-ni]: Yay! Our spaceship is now complete! Ready for blast off!")
            time.sleep(3)
            t.clear()
            t.penup()
            t.goto(0,-500)
            t.pendown()
            t.st()
            t.color(255,255,255)
            t.pencolor(255,0,0)
            t.seth(90)
            print("10...")
            time.sleep(0.5)
            print("9...")
            time.sleep(0.5)
            print("8...")
            time.sleep(0.5)
            print("7...")
            time.sleep(0.5)
            print("6...")
            time.sleep(0.5)
            print("5...")
            time.sleep(0.5)
            print("4...")
            time.sleep(0.5)
            print("3...")
            time.sleep(0.5)
            print("2...")
            time.sleep(0.5)
            print("1...")
            time.sleep(0.5)
            print("Blast off!!")
            t.speed(1)
            t.forward(1000)
            t.penup()
            t.ht()
            t.goto(0,0)
            t.clear()
            break
    #ask if they want more info
    print("[Ben-ni]: Now that we're in space, and finally on our way to Mars, let's learn a little bit more about Mars, the red planet. Mars is the fourth planet in the solar system, and it has both the tallest mountain(Olympus Mons) and the largest canyon (Valles Marineris). It is also a dangerous world, with huge storms of dust, and air we can't breathe.")
    while True:
        try:
            moreinfomars = str(input("Would you like more info on Mars? ")) 
            moreinfomars = moreinfomars.lower()
            if moreinfomars == "yes" or moreinfomars == "y":
                print("Great!")
                moreinfomars = "yes"
                break
            else:
                break
        except ValueError:
            print("Sorry, didn't quite understand that. For yes, enter 'yes', and for no, enter 'no'.")
    if moreinfomars == "yes":
        webbrowser.open("https://www.nasa.gov/audience/forstudents/k-4/stories/nasa-knows/what-is-mars-k4.html", new=2)
    #inspiring ending sequence
    t.pencolor(71,25,6)
    t.fillcolor(71,25,6)
    t.dot(100)
    t.penup()
    t.goto(0,120)
    t.color(255,255,255)
    t.pencolor(0,0,0)
    print("[Ben-ni]: We're finally here, in orbit around Mars. Isn't it beautiful?")
    time.sleep(0.5)
    print("[Ben-ni]: But unfortuanetly I cannot go to Mars myself. But you can! If you try hard, you can go to Mars in reality, and finish our mission for us.")
    time.sleep(0.5)
    print("Thank for playing the Mars mission module in spaceship, spaceship, SPACESHIP with Ben-ni. Come again soon!")
