import logging
import logstash
import sys
import time
import random_name


#uses random_name to generate a list of 5 random names
def getFakeNames():
        names = random_name.generate(5)
        return names



#takes the list of names and gets a letter count
#for each name and adds it to it's own list
def countLettersInNames(namesList):
    letterCountList = []
    for name in namesList:
        name = name.replace(" ", "")
        letterCount = len(name)
        letterCountList.append(letterCount)

    return(letterCountList)

def totalLetterCount(letterCount):
    totalLetters = 0
    for letters in letterCount:
        totalLetters += letters

    return totalLetters



def main():
    #logger setup
    logger = logging.getLogger('python-logstash-logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logstash.LogstashHandler('18.206.201.72', 5959, version=1))

    #logger.error('python-logstash: test logstash error message')    
    #logger.info('python-logstash: test logstash info message')
    #logger.warning('python-logstash: test logstash warning message')


    namesList = getFakeNames()
    logger.info('Names list generated')

    
    letterCount = countLettersInNames(namesList)
    logger.debug('Letters counted in Names List')
    logger.info('Letters Counted: {0}'.format(letterCount))


    totalLetters = totalLetterCount(letterCount)
    logger.debug('Total Letters: {0}'.format(totalLetters))
    
    extra = {
        'test_string' : 'python version: ' + repr(sys.version_info),
        'test_boolean' : True,
        'test_dict' : { 'a' : 1, 'b' : 'c'},
        'test_float' : 1.23,
        'test_integer' : totalLetters,
        'test_list' : [namesList],
    }

    logger.debug('Extra Fields', extra = extra)


    input("Press enter to continue.")
    
main()