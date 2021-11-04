import turtle
import random
from playsound import playsound

sightwords = '''
a, and, away, big, blue, can, come, down, find, for, funny, go, help, here, I, in, is, it, jump, little, look, make, me, my, not, one, play, red, run, said, see, the, three, to, two, up, we, where, yellow, you,
all, am, are, at, ate, be, black, brown, but, came, did, do, eat, four, get, good, have, he, into, like, must, new, no, now, on, our, out, please, pretty, ran, ride, saw, say, she, so, soon, that, there, they, this, too, under, want, was, well, went, what, white, who, will, with, yes,
after, again, an, any, as, ask, by, could, every, fly, from, give, going, had, has, her, him, his, how, just, know, let, live, may, of, old, once, open, over, put, round, some, stop, take, thank, them, then, think, walk, were, when,
always, around, because, been, before, best, both, buy, call, cold, does, don’t, fast, first, five, found, gave, goes, green, its, made, many, off, or, pull, read, right, sing, sit, sleep, tell, their, these, those, upon, us, use, very, wash, which, why, wish, work, would, write, your,
about, better, bring, carry, clean, cut, done, draw, drink, eight, fall, far, full, got, grow, hold, hot, hurt, if, keep, kind, laugh, light, long, much, myself, never, only, own, pick, seven, shall, show, six, small, start, ten, today, together, try, warm,
apple, baby, back, ball, bear, bed, bell, bird, birthday, boat, box, boy, bread, brother, cake, car, cat, chair, chicken, children, Christmas, coat, corn, cow, day, dog, doll, door, duck, egg, eye, farm, farmer, father, feet, fire, fish, floor, flower, game, garden, girl, goodbye, grass, ground, hand, head, hill, home, horse, house, kitty, leg, letter, man, men, milk, money, morning, mother, name, nest, night, paper, party, picture, pig, rabbit, rain, ring, robin, school, seed, sheep, shoe, sister, snow, song, squirrel, stick, street, sun, table, thing, time, top, toy, tree, watch, water, way, wind, window, wood
'''

wordlist_raw = sightwords.split(',')
wordlist_raw = [x.strip() for x in wordlist_raw]
wordlist = filter(lambda x: x!='', wordlist_raw)
wordlist = list(wordlist)

#print(list(wordlist))

screen = turtle.Screen()
SCREENW = 1000
SCREENH = 800
COOKIE = 'cookie.gif'
GAP = 20
XDIM = 4
YDIM = 3
FONTSIZE = 48
FORNUMS = 4
screen.setup(SCREENW, SCREENH)
newgame = True
BOXWIDTH =  (SCREENW - 2*GAP) / XDIM
BOXHEIGHT = (SCREENH - 2*GAP) / YDIM

turtle.title("Cookie Game")
turtle.speed(0)
turtle.tracer(0,0)
turtle.hideturtle()

c_turtles = {}
for i in range(XDIM):
    for j in range(YDIM):
        c_turtles[(i,j)] = turtle.Turtle()

        #c_turtles[(i,j)].Screen.addshape(COOKIE)
screen = turtle.Screen()
screen.addshape(COOKIE)

pos_list = []
fortune_pos = [(0,0)]
founds = {}

def check_over():
    global founds
    for f in founds:
        if not founds[f]:
            return False
    return True

def draw_cookie(row, col):
    startx =  -BOXWIDTH * ( XDIM / 2)
    starty =  -BOXHEIGHT * ( YDIM / 2 )
    t = c_turtles[(row, col)]
    t.setpos(startx + row*BOXWIDTH + BOXWIDTH/2, starty + col*BOXHEIGHT + BOXHEIGHT/2)
    t.shape(COOKIE)
    t.showturtle()
    

def draw_line(sx, sy, ex, ey, clr):
    turtle.color(clr)
    turtle.up()
    turtle.setpos(sx, sy)
    turtle.down()
    turtle.setpos(ex, ey)
    turtle.up()

def draw_text(txt, x, y, clr):
    turtle.color(clr)
    turtle.setpos(x, y)
    turtle.write(txt, align="center", font=("Arial", FONTSIZE, "bold"))

def erase_word(row, col):
    startx =  -BOXWIDTH * ( XDIM / 2) + row*BOXWIDTH + GAP
    starty =  -BOXHEIGHT * ( YDIM / 2 ) + col*BOXHEIGHT + GAP
    turtle.setpos(startx, starty)
    turtle.fillcolor('light grey')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(BOXWIDTH - GAP * 2)
        turtle.left(90)
        turtle.forward(BOXHEIGHT - GAP * 2)
        turtle.left(90)
    turtle.end_fill()

def setup_grid(clr):
    global fortune_pos
    global newgame
    global founds
    global c_turtles
  
    turtle.clear()
    turtle.speed(0)
    turtle.tracer(0,0)
    turtle.hideturtle()
    for i in range(XDIM):
        for j in range(YDIM):
            c_turtles[(i,j)].clear()
            c_turtles[(i,j)].speed(0)
            #c_turtles[(i,j)].tracer(0,0)
            c_turtles[(i,j)].hideturtle()

    newgame = True
    words = random.sample(wordlist, XDIM*YDIM)
    startx =  -BOXWIDTH * ( XDIM / 2)
    starty =  -BOXHEIGHT * ( YDIM / 2 )
    width = BOXWIDTH * XDIM
    height = BOXHEIGHT * YDIM
    for i in range(YDIM + 1):
        draw_line(startx, starty + i*BOXHEIGHT, startx + width, starty + i*BOXHEIGHT, clr)
    for j in range(XDIM + 1):
        draw_line(startx + j*BOXWIDTH, starty, startx + j*BOXWIDTH, starty + height, clr)
    cnt = 0
    pos_list = []
    founds = {}
    for i in range(YDIM):
        for j in range(XDIM):
            pos_list.append((j,i))
            x = startx + j*BOXWIDTH + BOXWIDTH/2
            y = starty + i*BOXHEIGHT + BOXHEIGHT/2
            draw_text(words[cnt], x, y, 'blue')
            cnt += 1
    fortune_pos = list(random.sample(pos_list,FORNUMS))
    for fp in fortune_pos:
        founds[fp] = False
    #print(fortune_pos)

def grid_click(x,y):
    # print(x,y)
    global fortune_pos
    global newgame
    global founds

    startx =  -BOXWIDTH * ( XDIM / 2)
    starty =  -BOXHEIGHT * ( YDIM / 2 )
    row = int((x - startx ) / BOXWIDTH)
    col = int((y - starty ) / BOXHEIGHT)
    #print('clicked:',row,col)
    turtle.goto(x, y)
    if (row,col) in fortune_pos:
        if check_over():
            setup_grid('red')
            turtle.update()
        else:
            founds[(row,col)] = True
            draw_cookie(row, col)
            if check_over():
                draw_text("All Cookies are Found !!!", 0, 0, 'red')
            turtle.update()
            playsound('cookie.mp3', True)  # unblock playsound not working on windows 11
        
    else:
        erase_word(row, col)
        playsound('ding.wav', True)
    #turtle.write(str(row)+","+str(col))

setup_grid('red')
#draw_cookie(0, 0)
#erase_word(0, 0)
turtle.update()
screen.onclick(grid_click)

screen.mainloop()
