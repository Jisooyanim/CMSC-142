
#x = x + y;
#y = x - y;
#x = x - y;
#z = x + y;
###############################
import nltk

num = 5
list = []
for i in range(num):
    userInput = input()
    list.append(userInput)
    listNoColon = nltk.sent_tokenize(list)
print(listNoColon)


