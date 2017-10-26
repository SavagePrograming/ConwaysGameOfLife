import numpy, random

# a = []
# # "Sandwhiches"
# for i in range(0, 10):
#     a.append([])
#     for ii in range(i, i + 10):
#         a[i].append(random.randint(0, 1))
# a = numpy.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


def Conway(num, SUM):
    if SUM > 3 or SUM < 2:
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


def PrintNum(num):
    print "[",
    for i in range(0, num):
        print "[" + ", ".join(["0"] * num) + "],"
    print "]"


Conways = numpy.vectorize(Conway)
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


# d = draws(a)
# print "\n".join(["".join(row) for row in d])
# raw_input("-----------------------------------------")
# done= ""
# while not done == "x":
#     a = runGeneration(a)
#     d = draws(a)
#     print "\n".join(["".join(row) for row in d])
#     done = raw_input("-----------------------------------------")
