import pygame

import numpy, random

pixels = []
height = 450 #int(raw_input("Height:"))
width = 300 #int(raw_input("Width:"))
squareSize = 2  # int(raw_input("Square Size:"))
speed = 1# int(raw_input("Speed:"))

testNumber = 0
pygame.init()
screen = pygame.display.set_mode([height* squareSize, width * squareSize])
pygame.key.set_repeat(200, 10)
end = False
Tick = 10
counter = 0
on = False
generations = 0
Past = []
direction = 0
Inactive = False
memLimit = 5
H = False
RANDOM = False

def glider(x,y,d):
    d = d % 4
    if d == 1:
        Live(x, y)
        Live(x + 1, y)
        Live(x - 1, y - 1)
        Live(x, y - 1)
        Live(x - 1, y + 1)
    elif d == 2:
        Live(x, y)
        Live(x - 1, y)
        Live(x + 1, y + 1)
        Live(x, y + 1)
        Live(x + 1, y - 1)
    elif d == 3:
        Live(x, y)
        Live(x - 1, y - 1)
        Live(x + 1, y - 1)
        Live(x, y + 1)
        Live(x + 1, y)
    elif d == 0:
        Live(x, y)
        Live(x + 1, y + 1)
        Live(x - 1, y + 1)
        Live(x, y - 1)
        Live(x - 1, y)


def makeChangeArray(num1, num2):
    if num1 == num2:
        return 0, 0
    elif num1 > num2:
        return 1, 0
    elif num1 < num2:
        return 0, 1


makeChangeArrays = numpy.vectorize(makeChangeArray)


def equals(Feild1, Feild2):
    #print 1
    Feild2, Feild1 = trim(Feild2), trim(Feild1)
    if len(Feild2) == len(Feild1) and (len(Feild1) == 0 or
                                           (isinstance(Feild1 == Feild2, type(True)) and Feild1 == Feild2)) or\
            (not (isinstance(Feild1 == Feild2, type(True))) and (Feild1 == Feild2).all()):
        return True
    elif len(Feild1) == 0 or len(Feild2) == 0 or sum(sum(Feild1)) != sum(sum(Feild2)):
        return False
    if len(Feild2) == len(Feild1):
        Feild1, Feild2 = makeChangeArrays(Feild1, Feild2)
    #print 3
    Feilds2 = split(Feild2)
    Feilds1 = split(Feild1)
    #print 4
    return reduce(lambda test, value: test and value,
                  map(lambda Feild1_, Feilds2_:
                      reduce(lambda test, value: value or test,
                             map(equals, [Feild1_] * len(Feilds2_), Feilds2_),
                             False), Feilds1, [Feilds2] * len(Feilds1)), True)


def trim(Feild):
    if len(Feild) == 0:
        return Feild
    xStart = 0
    yStart = 0
    xEnd = -1
    yEnd = -1
    while xStart < len(Feild) and sum(Feild[xStart, :]) == 0 :
        # print Feild[xStart, :]
        xStart += 1
    while  yStart < len(Feild[0]) and sum(Feild[:, yStart]) == 0:
        # print Feild[:, yStart]
        yStart += 1
    while xStart < len(Feild) + xEnd and sum(Feild[xEnd, :]) == 0 :
        # print Feild[xEnd, :]
        xEnd -= 1
    while yStart < len(Feild[0]) + yEnd and sum(Feild[:, yEnd]) == 0:
        # print Feild[:, yEnd]
        yEnd -= 1
    return Feild[xStart:xEnd + 1, yStart:yEnd + 1]


def trimboth(Feild1, Feild2):
    if len(Feild1) == 0:
        return Feild1, Feild2
    xStart = 0
    yStart = 0
    xEnd = -1
    yEnd = -1
    while xStart < len(Feild1) and sum(Feild1[xStart, :]) == 0 and sum(Feild2[xStart, :]) == 0:
        # print Feild[xStart, :]
        xStart += 1
    while  yStart < len(Feild1[0]) and sum(Feild1[:, yStart]) == 0 and sum(Feild2[:, yStart]) == 0:
        # print Feild[:, yStart]
        yStart += 1
    while xStart < len(Feild1) + xEnd and sum(Feild1[xEnd, :]) == 0 and sum(Feild2[xEnd, :]) == 0:
        # print Feild[xEnd, :]
        xEnd -= 1
    while yStart < len(Feild1[0]) + yEnd and sum(Feild1[:, yEnd]) == 0 and sum(Feild2[:, yEnd]) == 0:
        # print Feild[:, yEnd]
        yEnd -= 1
    return Feild1[xStart:xEnd + 1, yStart:yEnd + 1], Feild2[xStart:xEnd + 1, yStart:yEnd + 1]

def split(Feild):
    if len(Feild) == 0:
        return Feild
    Feild = trim(Feild)
    xSplit = []
    ySplit = []
    xIndex = 0
    yIndex = 0
    xTemp = 0
    yTemp = 0
    count = 0
    while xIndex < len(Feild):
        if sum(Feild[xIndex, :]) == 0 and count % 2 == 0:
            xTemp = xIndex
            count += 1
        elif sum(Feild[xIndex, :]) != 0 and count % 2 != 0:
            xSplit.append([xTemp, xIndex])
            count += 1
        xIndex += 1
    if count % 2 != 0:
        xSplit.append([xTemp, xIndex])

    count = 0
    while yIndex < len(Feild):
        if sum(Feild[yIndex, :]) == 0 and count % 2 == 0:
            yTemp = yIndex
            count += 1
        elif sum(Feild[yIndex, :]) != 0 and count % 2 != 0:
            ySplit.append([yTemp, yIndex])
            count += 1
        yIndex += 1
    if count % 2 != 0:
        ySplit.append([yTemp, yIndex])
    Feilds = []
    out = map(lambda xSplit,yCoor: map(lambda xCoor,yCoor: Feild[xCoor[0]:xCoor[1],yCoor[0]:yCoor[1]],
                                       xSplit, [yCoor] * len(xSplit)),
              [xSplit] * len(ySplit), ySplit)
    for o in out:
        Feilds.extend(o)
    return Feilds


def addRandomGliders(pixels, radius):
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            if pixels[x][y] == 0 and sum(sum(pixels[max(0, x - radius):min(height - 1, x + radius),max(0, y - radius):min(width - 1, y + radius)])) == 0:

                d = random.randint(0,3)
                glider(x,y,d)
            # elif not  pixels[x][y] == 0:
            #     print sum(sum(pixels[max(0, x - radius):min(height - 1, x + radius),max(0, y - radius):max(width - 1, y + radius)]))

def contains(array,feild):
    for f in array:
        if equals(feild, f):
            return True
    return False

def Conway(num, SUM):
    if SUM > 3 or SUM < 2:
        return 0
    elif SUM == 3:
        return 1
    else:
        return num

def ConwayRandom(num, SUM):
    # print SUM, num
    if SUM > 3 or SUM < 2:
        # print ":}"
        if SUM == 0 and num == 0:
            # print ":{"
            return int(random.random() + .001)
        return 0

    elif SUM == 3:
        return 1
    else:
        return num


def draw(num):
    if num == 0:
        return " "
    else:
        return "X"


# def PrintNum(num):
#     #print "[",
#     for i in range(0, num):
#         #print "[" + ", ".join(["0"] * num) + "],"
#     #print "]"


Conways = numpy.vectorize(Conway)
ConwaysRandom = numpy.vectorize(ConwayRandom)
draws = numpy.vectorize(draw)


def runGeneration(feild):

    fields = []

    fields.append(numpy.concatenate((feild[:, -1:], feild[:, :-1]), 1))
    fields.append(numpy.concatenate((feild[:, 1:], feild[:, :1]), 1))

    fields.append(numpy.concatenate((feild[-1:, :], feild[:-1, :]), 0))
    fields.append(numpy.concatenate((feild[1:, :], feild[:1, :]), 0))

    fields.append(numpy.concatenate((feild[-1:, :], feild[:-1, :]), 0))
    fields.append(numpy.concatenate((feild[-1:, :], feild[:-1, :]), 0))
    fields[4] = numpy.concatenate((fields[4][:, -1:], fields[4][:, :-1]), 1)
    fields[5] = numpy.concatenate((fields[5][:, 1:], fields[5][:, :1]), 1)

    fields.append(numpy.concatenate((feild[1:, :], feild[:1, :]), 0))
    fields.append(numpy.concatenate((feild[1:, :], feild[:1, :]), 0))

    fields[6] = numpy.concatenate((fields[6][:, -1:], fields[6][:, :-1]), 1)
    fields[7] = numpy.concatenate((fields[7][:, 1:], fields[7][:, :1]), 1)
    # print sum(fields)
    return Conways(feild, sum(fields))

def runGenerationRandom(feild):

    fields = []

    fields.append(numpy.concatenate((feild[:, -1:], feild[:, :-1]), 1))
    fields.append(numpy.concatenate((feild[:, 1:], feild[:, :1]), 1))

    fields.append(numpy.concatenate((feild[-1:, :], feild[:-1, :]), 0))
    fields.append(numpy.concatenate((feild[1:, :], feild[:1, :]), 0))

    fields.append(numpy.concatenate((feild[-1:, :], feild[:-1, :]), 0))
    fields.append(numpy.concatenate((feild[-1:, :], feild[:-1, :]), 0))
    fields[4] = numpy.concatenate((fields[4][:, -1:], fields[4][:, :-1]), 1)
    fields[5] = numpy.concatenate((fields[5][:, 1:], fields[5][:, :1]), 1)

    fields.append(numpy.concatenate((feild[1:, :], feild[:1, :]), 0))
    fields.append(numpy.concatenate((feild[1:, :], feild[:1, :]), 0))

    fields[6] = numpy.concatenate((fields[6][:, -1:], fields[6][:, :-1]), 1)
    fields[7] = numpy.concatenate((fields[7][:, 1:], fields[7][:, :1]), 1)
    # print sum(fields)
    return ConwaysRandom(feild, sum(fields))

for x in range(0, width):
    pixels.append([])
for x in range(0, width):
    for y in range(0, height):
        pixels[x].append(False)
pixels = numpy.array(pixels)

def Alive(x, y, pixels):
    test = 0
    if x >= 0 and y >= 0:
        try:
            test = pixels[x][y]
        except IndexError:
            test = 0
        return test



def Live(x, y):
    if x >= 0 and y >= 0:
        try:
            pixels[x][y] = 1
        except IndexError:
            pass


# int(raw_input("Test Number:"))

for x in range(0, pixels.__len__()):
    for y in range(0, pixels[0].__len__()):
        number = x * pixels.__len__() + y + 1
        num = 2 ** ((pixels.__len__() * pixels[0].__len__()) / ((number)))
        if testNumber % num < num / 2:
            pixels[x][y] = 1
        else:
            pixels[x][y] = 0
        num = 0


while not end:

    counter += 1

    if counter % speed == 0 and on:
        if RANDOM:
            __Pixels__ = runGenerationRandom(pixels)
        else:
            __Pixels__ = runGeneration(pixels)
        # print pixels == __Pixels__
        #print contains(Past, __Pixels__)
        if not( pixels == __Pixels__).all() and not contains(Past, __Pixels__):
            generations += 1
            Inactive = False
        else:
            if contains(Past,__Pixels__) and not (contains(Past, pixels)):
                generations += 1
                Inactive = False
            else:
                Inactive = True

        # print Inactive

        if not Inactive:
            Past.append(pixels)
            if Past.__len__() > memLimit and not memLimit == 0:
                Past.remove(Past[0])

        pixels = []
        for x in range(0, __Pixels__.__len__()):
            pixels.append([])
        for x in range(0, __Pixels__.__len__()):
            for y in range(0, __Pixels__[0].__len__()):
                pixels[x].append(__Pixels__[x][y])
        pixels = numpy.array(pixels)

        # if counter % (random.randint(3,6) * 50) == 0:
        #     addRandomGliders(pixels, random.randint(10, 50))

    screen.fill([200, 200, 200])

    for i in range(0, len(pixels)):
        for ii in range(0, len(pixels[i])):
            # print pixel
            if pixels[i][ii] == 1:
                pygame.draw.rect(screen, pygame.Color("black"),
                                 pygame.Rect(i * squareSize, ii * squareSize, squareSize, squareSize))

    font = pygame.font.Font(None, 50)
    color = pygame.Color("purple")
    text2 = font.render(str(generations), 1, color)
    screen.blit(text2, [0, 0])
    if H:
        for x in range(0, width):
            color2 = [50, 50, 50]
            if not width < 25:
                if x % int(width / 25) == 0:
                    color2 = [50, 200, 50]
            if x % int(width / 5) == 0:
                color2 = [200, 50, 50]
            elif x % int(width / 2) == 0:
                color2 = [50, 50, 200]
            pygame.draw.line(screen, color2, [x * squareSize, 0], [squareSize * x, height * squareSize])
        for y in range(0, height):
            color2 = [50, 50, 50]
            if not height < 25:
                if y % int(height / 25) == 0:
                    color2 = [50, 200, 50]
            if y % int(height / 5) == 0:
                color2 = [200, 50, 50]
            elif y % int(height / 2) == 0:
                color2 = [50, 50, 200]
            pygame.draw.line(screen, color2, [0, y * squareSize], [squareSize * width, y * squareSize])

    pygame.time.delay(1)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #print "yup"

            end = True
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            targetX = mousex / squareSize
            targetY = mousey / squareSize
        if event.type == pygame.MOUSEBUTTONUP:
            tf = not Alive(targetX, targetY, pixels)
            if not targetX == mousex / squareSize or not targetY == mousey / squareSize:
                # print targetX,mousex/squareSize,targetY,mousey/squareSize
                if targetX >= mousex / squareSize:
                    for x in range(mousex / squareSize, targetX + 1):
                        if targetY >= mousey / squareSize:
                            for y in range(mousey / squareSize, targetY + 1):
                                if tf:
                                    pixels[x][y] = 1
                                else:
                                    pixels[x][y] = 0
                        else:
                            for y in range(targetY, (mousey / squareSize) + 1):
                                if tf:
                                    pixels[x][y] = 1
                                else:
                                    pixels[x][y] = 0
                else:
                    for x in range(targetX, mousex / squareSize + 1):
                        if targetY >= mousey / squareSize:
                            for y in range(mousey / squareSize, targetY + 1):
                                if tf:
                                    pixels[x][y] = 1
                                else:
                                    pixels[x][y] = 0
                        else:
                            for y in range(targetY, (mousey / squareSize) + 1):
                                if tf:
                                    pixels[x][y] = 1
                                else:
                                    pixels[x][y] = 0
            else:
                # print ";)"
                if direction == 0:

                    if Alive(targetX, targetY, pixels):
                        try:
                            pixels[targetX][targetY] = 0
                        except IndexError:
                            pass
                    else:
                        try:
                            pixels[targetX][targetY] = 1
                        except IndexError:
                            pass
                else:
                    if direction == 1:
                        Live(targetX, targetY)
                        Live(targetX + 1, targetY)
                        Live(targetX - 1, targetY - 1)
                        Live(targetX, targetY - 1)
                        Live(targetX - 1, targetY + 1)
                    elif direction == 2:
                        Live(targetX, targetY)
                        Live(targetX - 1, targetY)
                        Live(targetX + 1, targetY + 1)
                        Live(targetX, targetY + 1)
                        Live(targetX + 1, targetY - 1)
                    elif direction == 3:
                        Live(targetX, targetY)
                        Live(targetX - 1, targetY - 1)
                        Live(targetX + 1, targetY - 1)
                        Live(targetX, targetY + 1)
                        Live(targetX + 1, targetY)
                    elif direction == 4:
                        Live(targetX, targetY)
                        Live(targetX + 1, targetY + 1)
                        Live(targetX - 1, targetY + 1)
                        Live(targetX, targetY - 1)
                        Live(targetX - 1, targetY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                direction = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if not Past == []:
                    Past.reverse()

                    pixels = Past[0]
                    Past.__delitem__(0)

                    Past.reverse()

                    generations -= 1
            if event.key == pygame.K_y:
                __Pixels__ = []
                for x in range(0, pixels.__len__()):
                    __Pixels__.append([])
                for x in range(0, pixels.__len__()):
                    for y in range(0, pixels[0].__len__()):
                        __Pixels__[x].append([x, y, pixels[x][y]])

                for x in range(0, pixels.__len__()):
                    for y in range(0, pixels[0].__len__()):

                        trueCounter = 0
                        for x1 in [-1, 0, 1]:
                            for y1 in [-1, 0, 1]:
                                if not x1 == 0 or not y1 == 0:
                                    if Alive((x + x1), (y + y1), pixels):
                                        trueCounter += 1

                                        ##                                if x == 56 and y == 11:
                                        ##                                    print (x+x1),(y+y1)
                                        ##
                                        ##                if x == 56 and y == 11:
                                        ##                    print trueCounter

                        if trueCounter < 2 or trueCounter >= 4:
                            __Pixels__[x][y] = 0
                        elif trueCounter == 2:
                            pass
                        elif trueCounter == 3:
                            __Pixels__[x][y] = 1

                if not pixels == __Pixels__ and not Past.__contains__(__Pixels__):
                    generations += 1
                    Inactive = False
                else:
                    Inactive = True

                # print Inactive

                if not Inactive:
                    Past.append(pixels)
                    if Past.__len__() > memLimit and not memLimit == 0:
                        Past.remove(Past[0])

                pixels = []
                for x in range(0, __Pixels__.__len__()):
                    pixels.append([])
                for x in range(0, __Pixels__.__len__()):
                    for y in range(0, __Pixels__[0].__len__()):
                        pixels[x].append([x, y, __Pixels__[x][y]])

            if event.key == pygame.K_g:
                addRandomGliders(pixels, 20)
            if event.key == pygame.K_UP:
                direction = 1
            if event.key == pygame.K_DOWN:
                direction = 2
            if event.key == pygame.K_RIGHT:
                direction = 3
            if event.key == pygame.K_LEFT:
                direction = 4
            if event.key == pygame.K_n:

                generations = 0
                Past = []
                Inactive = False

                testNumber = int(input("Test Number:"))

                for x in range(0, pixels.__len__()):
                    for y in range(0, pixels[0].__len__()):
                        number = x * pixels.__len__() + y + 1
                        num = 2 ** ((pixels.__len__() * pixels[0].__len__()) / ((number)))
                        if testNumber % num < num / 2:
                            pixels[x][y] = 1
                        else:
                            pixels[x][y] = 0
                        num = 0
            if event.key == pygame.K_r:
                RANDOM = not RANDOM
                print("RANDOM", RANDOM)
            if event.key == pygame.K_m:

                generations = 0
                Past = []
                Inactive = False

                testNumber += 1

                for x in range(0, pixels.__len__()):
                    for y in range(0, pixels[0].__len__()):
                        number = x * pixels.__len__() + y + 1
                        num = 2 ** ((pixels.__len__() * pixels[0].__len__()) / ((number)))
                        if testNumber % num < num / 2:
                            pixels[x][y] = 1
                        else:
                            pixels[x][y] = 0
                        num = 0

            if event.key == pygame.K_x:

                generations = 0
                Past = []
                Inactive = False

                # for pixels1 in pixels:
                #     for pixel in pixels1:
                #         pixel = 0

                pixels = numpy.array([[0] * width] * height)

            if event.key == pygame.K_SPACE:

                if on:
                    on = False
                else:
                    on = True

            if event.key == pygame.K_h:
                H = not H
pygame.quit()
