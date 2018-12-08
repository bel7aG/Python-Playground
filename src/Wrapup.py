import random
import sys
import os

# print
print('bel7aG Learn basics of python like an idiot!')

name = 'Belhassen'
surname = 'Gharsallah'
print("\n\nName: ", name, "\nSurname: ", surname, '\n')

#                               Operators for Numbers

                           #   + - * / % // **   #

isThisMyFirstNumber = 1996

print('8 + 4 = ', 8 + 4)
print('8 - 4 = ', 8 - 4)
print('8 / 4 = ', 8 / 4)
print('8 % 4 = ', 8 % 4)
print('8 // 4 = ', 8 // 4)
print('8 ** 4 = ', 8 ** 4)


                            #       String       #

thinkLikeItIsYouFirstString = "\"is python better than Javascript dont think so"

print(thinkLikeItIsYouFirstString)

# Multi line String
bel7aG = '''\nMy Name is Belhssen Gharsallah
you can call me bel7aG\n'''
print('\n', bel7aG, end = '\n\n')

#WARNING "%s %s %s" must be in double quote
print("%s %s %s %s %d %s" % ('python now inspire me', thinkLikeItIsYouFirstString, bel7aG, 'hmmm not bad', 2, 'ES6 still better in my opinion'), end = "\n\n")


                            #         List        #

bel7aG = ['Belhassen', "Gharsallah", 22, 'https', '://', '/bel7aG', 'www.github.com']
bel7aGUrl = bel7aG[3] + bel7aG[-3] + bel7aG[6] + bel7aG[-2]
print('this is my github url', end = '\t')
print(bel7aGUrl, end = '\n\n')

#[:] operator work with strings and list and maybe others wanna see [( [x ):( y[ )]
#[:] with string
bel7aGUrl = bel7aGUrl[0:-1]
print(bel7aGUrl)

#[:] with List
bel7aGCopy = bel7aG[3:5] + bel7aG[5:7]
print(bel7aGCopy)


#We can put List inside an list
listInsideList = [['Python', 'django', 'tensorflow'], ['Javascript', 'NodeJs', 'ReactJs', 'VueJS', 'tensorflowJS', 'threejs']]
print("%s vs %s \n==>%s" % (listInsideList[0][1], listInsideList[1][1], 'Django Lose'), end = '\n\n')

combinedList = [bel7aG, listInsideList]
print(combinedList, end = '\n\n')
print(combinedList[0][0], ' is a ', combinedList[1][1][0], ' Developer', end = '\n\n')

                            #   List methods    #

#   list.append(object) an item inside a list
bel7aG.append('Web Always Win')
print(bel7aG[-1]) #   Web Always Win

#   list.insert(index, object)

bel7aG.insert(0, 'Pythooooniiii')
print(bel7aG[0]) #  Pythooooniiii

#   list.filter(function, list)
newList = list(filter(lambda element: isinstance(element, str), bel7aG)) # just the strings
print("new List", newList, sep = "\n\n", end = "\n\n")

print(newList[-2][-3:len(newList[-2])]) #  com

#   list.sort()
newList.sort()
print(newList)
newList.sort(key = lambda str: str.lower())
print(newList)                                # ==> last two are the same but str.lower faster
newList.sort(key = str.lower)
print(newList)
