import random
from PyQt5 import QtCore, QtGui, QtWidgets

        
points = 0
lastAnswer = []
        
#making a sort of matrix grid out of classes
class Organ:   
    global organList
    global chosenDose
    def __init__(self, name, oneThird, twoThird, threeThird):
        self.name = name
        self.oneThird = oneThird
        self.twoThird = twoThird
        self.threeThird = threeThird
        
        

#pick one correct answer and 3 incorrect answers
#no repeats, no 0's

def roll():
    print('')
    print('roll')
    global passCoverage
    global correctDoseValue
    global incorrectDoseValue1
    global incorrectDoseValue2
    global correctDoseChoice
    global chosenOrgan
    global organName
    
    chosenOrgan = random.choice(organList)
    fakeoutOrgan1 = random.choice(organList)
    fakeoutOrgan2 = random.choice(organList)

    #Randomize which column each answer is coming from, separately
    doseItems = ['oneThird','twoThird','threeThird']
    #choose one two three thirds, 3 times
    correctDoseChoice = random.choice(doseItems)
    incorrectDoseChoice1 = random.choice(doseItems)
    incorrectDoseChoice2 = random.choice(doseItems)
    
    #Translate this for presenting text to the user
    if correctDoseChoice == 'oneThird':
      passCoverage = 'one third'
    elif correctDoseChoice == 'twoThird':
      passCoverage = 'two thirds'
    elif correctDoseChoice == 'threeThird':
      passCoverage = 'three thirds'  
    
    
    #return the 3 unique answers
    correctDoseValue = getattr(chosenOrgan, correctDoseChoice) #return single int value
    incorrectDoseValue1 = getattr(fakeoutOrgan1, incorrectDoseChoice1)
    incorrectDoseValue2 = getattr(fakeoutOrgan2, incorrectDoseChoice2)
    
    organName = getattr(chosenOrgan, 'name')
        

    
    #remove duplicates
    if correctDoseValue == incorrectDoseValue1 or correctDoseValue == incorrectDoseValue2 or incorrectDoseValue1 ==incorrectDoseValue2:
        roll()
    
    #remove 0
    if correctDoseValue == 0 or incorrectDoseValue1 == 0 or incorrectDoseValue2 ==0:
        roll()
          ####Button randomizer
    
          
    
      

    
    
    

#instantiate organs
brain = Organ('brain', 6000, 5000, 4500)
brainStem = Organ('brainstem', 6000, 5300, 5000)
lensOfEye = Organ('lens of the eye', 0, 0, 1000)
retina = Organ('retina', 0, 0, 4500)
opticNerve = Organ('optic nerve', 0, 0, 5000)
opticChiasm = Organ('optic chiasm', 0, 0, 5000)
ear = Organ('ear mid/external', 5500, 5500, 5500)
parotid = Organ('parotid', 0, 3200, 3200)
larynx = Organ('larynx', 7900, 7000, 7000)
esophagus = Organ('esophagus', 6000, 5800, 5500)
brachialPlexus = Organ('brachial plexus', 6200, 6100, 6000)
spinalCord = Organ('spinal cord', 5000, 5000, 4700)
caudaEquina = Organ('cauda equina', 0, 0, 6000)
lung = Organ('lung', 4500, 3000, 1750)
heart = Organ('heart', 6000, 4500, 4000)
kidney = Organ('kidney', 5000, 3000, 2300)
stomach = Organ('stomach', 6000, 5500, 5000)
bladder = Organ('bladder', 0, 8000, 6500)
smallIntestine = Organ('small intestine', 5000, 0, 4000)
colon = Organ('colon', 5500, 0, 4500)
liver = Organ('liver', 5000, 3500, 3000)
femoralHead = Organ('femoral head', 0, 0, 5200)
skin = Organ('skin', 7000, 6000, 5500)
tmJoint = Organ('tm joint', 6500, 6000, 6000)
ribCage = Organ('rib cage', 5000, 0, 0)

#make a list of all organs
#try getting this automatically somehow, liek get the first attribute in 
#Organ and add it to organList
organList = [brain, brainStem, lensOfEye, retina, opticNerve, opticChiasm, ear, parotid, larynx, esophagus, brachialPlexus, spinalCord, caudaEquina, lung, heart,
              kidney, stomach, bladder, smallIntestine, colon, liver, femoralHead, skin, tmJoint, ribCage]
    
    
###initialize one instance of game
roll()



print(f'correctDoseValue: {correctDoseValue}')
print(f'incorrectDoseValue2: {incorrectDoseValue1}')
print(f'incorrectDoseValue2: {incorrectDoseValue2}')



###############################BUILD WINDOW#########################
#this class helps create the layout
#it also checks for button clicks 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        print('')
        print('setpUi')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ### I can make value sent to buttons be from a list

        
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)       
        self.pushButton.setGeometry(QtCore.QRect(80, 420, 93, 28))
        self.pushButton.setObjectName("pushButton")
        ##test##
        #self.pushButton.setCheckable(True)
        #self.pushButton.toggle()
        self.pushButton.clicked.connect(lambda:self.whichbtn(self.pushButton))
        self.pushButton.clicked.connect(self.btnstate)
        ###endtest####
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 420, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(lambda:self.whichbtn(self.pushButton_2))
        self.pushButton_2.clicked.connect(self.btnstate)
        
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 420, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_3.clicked.connect(lambda:self.whichbtn(self.pushButton_3))
        self.pushButton_3.clicked.connect(self.btnstate)
        
        #changed to qplaintextedit from QLineEdit
        self.pointCounter = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pointCounter.setGeometry(QtCore.QRect(60, 30, 113, 30))
        self.pointCounter.setObjectName("points")
        
        self.question = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(70, 160, 601, 30))
        self.question.setObjectName("question")
        
        #tell correct answer
        self.displayAnswer = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.displayAnswer.setGeometry(QtCore.QRect(70, 260, 601, 60))
        self.displayAnswer.setObjectName('displayAnswer')
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


        
        
        
    def btnstate(self):
        print('')
        print('btnstate')
        if self.pushButton.isChecked():
          print("button pressed")
        else:
          print("button released")
  
      #maybe make playerWasCorrect a function
      
    def playerWasCorrect(self):
        print('')
        print('playerWasCorrect')
        global playerWasCorrect
        global points

        if clickedAns == correctDoseValue:
          print("correct answer")
          playerWasCorrect = True
          points = points + 49
          print(f'{points}')
          print(playerWasCorrect)
          #add correct answer to a list
          lastAnswer.append(correctDoseValue)
          #retrieve the end of that list, which should be the correct answer from last question
          roll()
        
        else:
          points = points - 10
          print("wrong answer")
          playerWasCorrect = False
          lastAnswer.append(correctDoseValue)
          roll()
          
        if points >= 100:
          points = 0
           
        else:
          pass
        
        
        
  
    def whichbtn(self,b):
      print('')
      print('whichbtn')
      global clickedAns
      clickedAns = int(b.text())
      print(f'correctDoseValue is {correctDoseValue}')
      print("clicked button is "+b.text())
      self.playerWasCorrect()
           
      self.update()
      
      
    def update(self):
        print('')
        print('update(self)')
        #roll()

        
        
        
        #update the main window with new button numbers
        Ui_MainWindow.setupUi(self, MainWindow)
        
        
        


        #chanfed pointcounter to setplaintext from settext
        self.pointCounter.setPlainText(f"Points: {points}")
        self.question.setPlainText(f"What is the tolerance dose for {passCoverage} of the {organName}?")
        #correct answer from last question
        if points >= 100:
          self.displayAnswer.setPlainText(f"You won! Try again! Correct answer for last question was: {lastAnswer[-1]}")
        else:
          self.displayAnswer.setPlainText(f"Correct answer for last question was: {lastAnswer[-1]}")

                        
        self.pushButton.setText(f"{noDupAnswerList[0][0]}")
        self.pushButton_2.setText(f"{noDupAnswerList[0][1]}")
        self.pushButton_3.setText(f"{noDupAnswerList[0][2]}")
        


    def retranslateUi(self, MainWindow):      #feeds info to setpUi()
        print('')
        print('retranslateUi')
        global noDupAnswerList
        
        #randomize button placement 
        answerList = [correctDoseValue, incorrectDoseValue1, incorrectDoseValue2]
        noDupAnswerList = []
        for answer in answerList:
          noDupAnswerList.append(random.sample(answerList, 3))
          print(f'nodupanswerlist:{noDupAnswerList}')
        
        print(noDupAnswerList)
        
        
        
        global _translate
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tolerance Doses"))
        self.pushButton.setText(_translate("MainWindow", f"{noDupAnswerList[0][0]}"))
        self.pushButton_2.setText(_translate("MainWindow", f"{noDupAnswerList[0][1]}"))
        self.pushButton_3.setText(_translate("MainWindow", f"{noDupAnswerList[0][2]}"))
        self.pointCounter.setPlainText(_translate("MainWindow", f"Points: {points}"))
        self.question.setPlainText(_translate("MainWindow", f"What is the tolerance dose for {passCoverage} of the {organName}?"))
        #test
        try:
          self.displayAnswer.setPlainText(f"Correct answer for last question was: {lastAnswer[-1]}")
        except:
          self.displayAnswer.setPlainText(_translate("MainWindow", f" Test your knowledge of Tolerance Doses! All numbers are representative of doses in cGy. See last correct answer here after question 1."))
    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    print('app')
    MainWindow = QtWidgets.QMainWindow()
    print('mainwindow')
    ui = Ui_MainWindow()
    print('ui')
    ui.setupUi(MainWindow)
    print('setupui')
    MainWindow.show()
    sys.exit(app.exec_())




