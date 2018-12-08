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
bel7aGUrl = bel7aG[3] + bel7aG[4] + bel7aG[6] + bel7aG[5]
print('this is my github url', end = '\t')
print(bel7aGUrl)
