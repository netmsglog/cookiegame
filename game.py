import turtle
import random

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


#print(list(wordlist))

screen = turtle.Screen()
SCREENW = 1000
SCREENH = 800
GAP = 20
XDIM = 4
YDIM = 4
FONTSIZE = 48
screen.setup(SCREENW, SCREENH)

BOXWIDTH =  (SCREENW - 2*GAP) / XDIM
BOXHEIGHT = (SCREENH - 2*GAP) / YDIM

turtle.title("Cookie Game")
turtle.speed(0)
turtle.tracer(0,0)
turtle.hideturtle()

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

def draw_grid(clr):
    words = random.sample(list(wordlist), XDIM*YDIM)
    startx =  -BOXWIDTH * ( XDIM / 2)
    starty =  -BOXHEIGHT * ( YDIM / 2 )
    width = BOXWIDTH * XDIM
    height = BOXHEIGHT * YDIM
    for i in range(YDIM + 1):
        draw_line(startx, starty + i*BOXHEIGHT, startx + width, starty + i*BOXHEIGHT, clr)
    for j in range(XDIM + 1):
        draw_line(startx + j*BOXWIDTH, starty, startx + j*BOXWIDTH, starty + height, clr)
    cnt = 0
    for i in range(YDIM):
        for j in range(XDIM):
            x = startx + j*BOXWIDTH + BOXWIDTH/2
            y = starty + i*BOXHEIGHT + BOXHEIGHT/2
            draw_text(words[cnt], x, y, 'blue')
            cnt += 1

draw_grid('red')
turtle.update()

turtle.done()