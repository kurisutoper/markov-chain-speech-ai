import sys
from random import randint

class Chain:
    links = {}

    def newLink(this,value):
        if not this.links.has_key(value):
            this.links[value] = {}

    def addToLink(this,linkvalue,value):
        this.newLink(linkvalue)
        this.newLink(value)
        if this.links[linkvalue].has_key(value):
            this.links[linkvalue][value] += 1
        else:
            this.links[linkvalue][value] = 1

    def interpSentence(this,given):
        given_words = given.split(' ')

        last_word = ""
        for word in given_words:
            if last_word == "":
                this.newLink(word)
            else:
                this.addToLink(last_word,word)
            last_word = word

    def printLinks(this):
        for key in this.links:
            sys.stdout.write(key+" ")
            print(this.links[key])

    def readFromFile(this,filepath):
        with open(filepath) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                this.interpSentence(line)

    def printPathFrom(this,value):
        if this.links.has_key(value):
            sys.stdout.write(value+" ")
            
            #end path at one sentence
            if '!' in value or '?' in value or '.' in value:
                print("")
                return

            totalhits = 0
            for key in this.links[value]:
                totalhits += this.links[value][key]

            randindex = randint(1,totalhits)
            totalhits = 0
            for key in this.links[value]:
                totalhits += this.links[value][key]
                if totalhits >= randindex:
                    this.printPathFrom(key)
                    break
