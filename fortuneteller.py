import os, sys, random, math, time;

timeStamp = time.ctime();
fortunesRead=0;

def mainLoop() :
    print("{Y}es, all other keys run in terror.");
    _answer = raw_input();
    
    if _answer == 'y' :
            getFortune();
            print("Another fortune, my pretty!?\n\n");
            mainLoop();
    else:
            goodBye();


def story(startline, stopline):
    with open("storytext.txt") as f:
        storyLines = f.readlines();
        [l.strip('\n\r') for l in storyLines]
    for i in xrange(startline-1, stopline):
        print(storyLines[i]);
    waitForKey();



def getFortune():
    _fortune = random.choice(open("fortunes.txt").readlines());
    print("Pythonia gazes into her crystal ball, and says...\n");
    print(_fortune);
    global fortunesRead;
    fortunesRead += 1 ;

def recordUsage():
    with open("fortunerecord.txt","a+") as record:
        record.write('On {} you had {} fortunes read to you.\n'.format(timeStamp, fortunesRead));
        record.close();



def goodBye():
    recordUsage();
    print("You run away in fear!!! You hear Pythonia laughing at you as you flee!\n");
    print("Check fortunerecord.txt to see how many fortunes you've been read!\n");
    waitForKey();

def waitForKey():
    raw_input("Press Enter to continue...");



story(0,5);
story(6,9);
story(9,20);
mainLoop();

