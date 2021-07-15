# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tourneyOverlayQSyEUb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(681, 290)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        mainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.mainWidget = QWidget(mainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.infoLayout = QHBoxLayout()
        self.infoLayout.setObjectName(u"infoLayout")
        self.setLayout = QVBoxLayout()
        self.setLayout.setObjectName(u"setLayout")
        self.setLabel = QLabel(self.mainWidget)
        self.setLabel.setObjectName(u"setLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.setLabel.sizePolicy().hasHeightForWidth())
        self.setLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.setLabel.setFont(font)
        self.setLabel.setAlignment(Qt.AlignCenter)

        self.setLayout.addWidget(self.setLabel)

        self.setFormLayout = QFormLayout()
        self.setFormLayout.setObjectName(u"setFormLayout")
        self.setRoundLabel = QLabel(self.mainWidget)
        self.setRoundLabel.setObjectName(u"setRoundLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.setRoundLabel.setFont(font1)

        self.setFormLayout.setWidget(0, QFormLayout.LabelRole, self.setRoundLabel)

        self.setRoundInput = QLineEdit(self.mainWidget)
        self.setRoundInput.setObjectName(u"setRoundInput")
        with open('./TourneyOverlay/Set/round.txt', 'r') as file:
            self.setRoundInput.setText(file.read())
        self.setRoundInput.textChanged.connect(self.setRound)

        self.setFormLayout.setWidget(0, QFormLayout.FieldRole, self.setRoundInput)

        self.setGamesLabel = QLabel(self.mainWidget)
        self.setGamesLabel.setObjectName(u"setGamesLabel")
        self.setGamesLabel.setFont(font1)

        self.setFormLayout.setWidget(1, QFormLayout.LabelRole, self.setGamesLabel)

        self.setGamesInput = QLineEdit(self.mainWidget)
        self.setGamesInput.setObjectName(u"setGamesInput")
        with open('./TourneyOverlay/Set/games.txt', 'r') as file:
            self.setGamesInput.setText(file.read())
        self.setGamesInput.textChanged.connect(self.setGames)

        self.setFormLayout.setWidget(1, QFormLayout.FieldRole, self.setGamesInput)


        self.setLayout.addLayout(self.setFormLayout)

        self.commentaryLayout = QVBoxLayout()
        self.commentaryLayout.setObjectName(u"commentaryLayout")
        self.line_5 = QFrame(self.mainWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.commentaryLayout.addWidget(self.line_5)

        self.commentaryLabel = QLabel(self.mainWidget)
        self.commentaryLabel.setObjectName(u"commentaryLabel")
        sizePolicy1.setHeightForWidth(self.commentaryLabel.sizePolicy().hasHeightForWidth())
        self.commentaryLabel.setSizePolicy(sizePolicy1)
        self.commentaryLabel.setFont(font)
        self.commentaryLabel.setAlignment(Qt.AlignCenter)

        self.commentaryLayout.addWidget(self.commentaryLabel)

        self.commentaryFormLayout = QFormLayout()
        self.commentaryFormLayout.setObjectName(u"commentaryFormLayout")
        self.commentary1Label = QLabel(self.mainWidget)
        self.commentary1Label.setObjectName(u"commentary1Label")
        self.commentary1Label.setFont(font1)

        self.commentaryFormLayout.setWidget(0, QFormLayout.LabelRole, self.commentary1Label)

        self.commentary1Input = QLineEdit(self.mainWidget)
        self.commentary1Input.setObjectName(u"commentary1Input")
        with open('./TourneyOverlay/Commentators/1.txt', 'r') as file:
            self.commentary1Input.setText(file.read())
        self.commentary1Input.textChanged.connect(self.setCommentator1)

        self.commentaryFormLayout.setWidget(0, QFormLayout.FieldRole, self.commentary1Input)

        self.commentary2Label = QLabel(self.mainWidget)
        self.commentary2Label.setObjectName(u"commentary2Label")
        self.commentary2Label.setFont(font1)

        self.commentaryFormLayout.setWidget(1, QFormLayout.LabelRole, self.commentary2Label)

        self.commentary2Input = QLineEdit(self.mainWidget)
        self.commentary2Input.setObjectName(u"commentary2Input")
        with open('./TourneyOverlay/Commentators/2.txt', 'r') as file:
            self.commentary2Input.setText(file.read())
        self.commentary2Input.textChanged.connect(self.setCommentator2)

        self.commentaryFormLayout.setWidget(1, QFormLayout.FieldRole, self.commentary2Input)


        self.commentaryLayout.addLayout(self.commentaryFormLayout)


        self.setLayout.addLayout(self.commentaryLayout)


        self.infoLayout.addLayout(self.setLayout)

        self.line_2 = QFrame(self.mainWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.infoLayout.addWidget(self.line_2)

        self.p1Layout = QVBoxLayout()
        self.p1Layout.setObjectName(u"p1Layout")
        self.p1Label = QLabel(self.mainWidget)
        self.p1Label.setObjectName(u"p1Label")
        sizePolicy1.setHeightForWidth(self.p1Label.sizePolicy().hasHeightForWidth())
        self.p1Label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setWeight(50)
        self.p1Label.setFont(font2)
        self.p1Label.setScaledContents(False)
        self.p1Label.setAlignment(Qt.AlignCenter)

        self.p1Layout.addWidget(self.p1Label)

        self.p1FormLayout = QFormLayout()
        self.p1FormLayout.setObjectName(u"p1FormLayout")
        self.p1TagLabel = QLabel(self.mainWidget)
        self.p1TagLabel.setObjectName(u"p1TagLabel")
        self.p1TagLabel.setFont(font1)

        self.p1FormLayout.setWidget(0, QFormLayout.LabelRole, self.p1TagLabel)

        self.p1TagInput = QLineEdit(self.mainWidget)
        self.p1TagInput.setObjectName(u"p1TagInput")
        with open('./TourneyOverlay/Player 1/tag.txt', 'r') as file:
            tag = file.read()
            if ' | ' in tag:
                self.p1TagInput.setText(tag.split(' | ')[1])
            else:
                self.p1TagInput.setText(tag)
        self.p1TagInput.textChanged.connect(self.setP1Tag)

        self.p1FormLayout.setWidget(0, QFormLayout.FieldRole, self.p1TagInput)

        self.p1SponsorLabel = QLabel(self.mainWidget)
        self.p1SponsorLabel.setObjectName(u"p1SponsorLabel")
        self.p1SponsorLabel.setFont(font1)

        self.p1FormLayout.setWidget(1, QFormLayout.LabelRole, self.p1SponsorLabel)

        self.p1SponsorInput = QLineEdit(self.mainWidget)
        self.p1SponsorInput.setObjectName(u"p1SponsorInput")
        with open('./TourneyOverlay/Player 1/tag.txt', 'r') as file:
            tag = file.read()
            if ' | ' in tag:
                self.p1SponsorInput.setText(tag.split(' | ')[0])
        self.p1SponsorInput.textChanged.connect(self.setP1Tag)

        self.p1FormLayout.setWidget(1, QFormLayout.FieldRole, self.p1SponsorInput)

        self.p1SocialLabel = QLabel(self.mainWidget)
        self.p1SocialLabel.setObjectName(u"p1SocialLabel")
        self.p1SocialLabel.setFont(font1)

        self.p1FormLayout.setWidget(2, QFormLayout.LabelRole, self.p1SocialLabel)

        self.p1SocialInput = QLineEdit(self.mainWidget)
        self.p1SocialInput.setObjectName(u"p1SocialInput")
        with open('./TourneyOverlay/Player 1/social.txt', 'r') as file:
            self.p1SocialInput.setText(file.read())
        self.p1SocialInput.textChanged.connect(self.setP1Social)

        self.p1FormLayout.setWidget(2, QFormLayout.FieldRole, self.p1SocialInput)

        self.p1ScoreLabel = QLabel(self.mainWidget)
        self.p1ScoreLabel.setObjectName(u"p1ScoreLabel")
        self.p1ScoreLabel.setFont(font1)

        self.p1FormLayout.setWidget(3, QFormLayout.LabelRole, self.p1ScoreLabel)

        self.p1ScoreInput = QSpinBox(self.mainWidget)
        self.p1ScoreInput.setObjectName(u"p1ScoreInput")
        with open('./TourneyOverlay/Player 1/score.txt', 'r') as file:
            self.p1ScoreInput.setValue(int(file.read()))
        self.p1ScoreInput.valueChanged.connect(self.setP1Score)

        self.p1FormLayout.setWidget(3, QFormLayout.FieldRole, self.p1ScoreInput)


        self.p1Layout.addLayout(self.p1FormLayout)


        self.infoLayout.addLayout(self.p1Layout)

        self.line_4 = QFrame(self.mainWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.infoLayout.addWidget(self.line_4)

        self.p2Layout = QVBoxLayout()
        self.p2Layout.setObjectName(u"p2Layout")
        self.p2Layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.p2Label = QLabel(self.mainWidget)
        self.p2Label.setObjectName(u"p2Label")
        sizePolicy1.setHeightForWidth(self.p2Label.sizePolicy().hasHeightForWidth())
        self.p2Label.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.p2Label.setFont(font3)
        self.p2Label.setAlignment(Qt.AlignCenter)

        self.p2Layout.addWidget(self.p2Label)

        self.p2FormLayout = QFormLayout()
        self.p2FormLayout.setObjectName(u"p2FormLayout")
        self.p2TagLabel = QLabel(self.mainWidget)
        self.p2TagLabel.setObjectName(u"p2TagLabel")
        self.p2TagLabel.setFont(font1)

        self.p2FormLayout.setWidget(0, QFormLayout.LabelRole, self.p2TagLabel)

        self.p2TagInput = QLineEdit(self.mainWidget)
        self.p2TagInput.setObjectName(u"p2TagInput")
        with open('./TourneyOverlay/Player 2/tag.txt', 'w+') as file:
            tag = file.read()
            if ' | ' in tag:
                self.p2TagInput.setText(tag.split(' | ')[1])
            else:
                self.p2TagInput.setText(tag)
        self.p2TagInput.textChanged.connect(self.setP2Tag)

        self.p2FormLayout.setWidget(0, QFormLayout.FieldRole, self.p2TagInput)

        self.p2SponsorLabel = QLabel(self.mainWidget)
        self.p2SponsorLabel.setObjectName(u"p2SponsorLabel")
        self.p2SponsorLabel.setFont(font1)

        self.p2FormLayout.setWidget(1, QFormLayout.LabelRole, self.p2SponsorLabel)

        self.p2SponsorInput = QLineEdit(self.mainWidget)
        self.p2SponsorInput.setObjectName(u"p2SponsorInput")
        with open('./TourneyOverlay/Player 2/tag.txt', 'w+') as file:
            tag = file.read()
            if ' | ' in tag:
                self.p2SponsorInput.setText(tag.split(' | ')[0])
        self.p2SponsorInput.textChanged.connect(self.setP2Tag)

        self.p2FormLayout.setWidget(1, QFormLayout.FieldRole, self.p2SponsorInput)

        self.p2SocialLabel = QLabel(self.mainWidget)
        self.p2SocialLabel.setObjectName(u"p2SocialLabel")
        self.p2SocialLabel.setFont(font1)

        self.p2FormLayout.setWidget(2, QFormLayout.LabelRole, self.p2SocialLabel)

        self.p2SocialInput = QLineEdit(self.mainWidget)
        self.p2SocialInput.setObjectName(u"p2SocialInput")
        with open('./TourneyOverlay/Player 2/social.txt', 'r') as file:
            self.p2SocialInput.setText(file.read())
        self.p2SocialInput.textChanged.connect(self.setP2Social)

        self.p2FormLayout.setWidget(2, QFormLayout.FieldRole, self.p2SocialInput)

        self.p2ScoreLabel = QLabel(self.mainWidget)
        self.p2ScoreLabel.setObjectName(u"p2ScoreLabel")
        self.p2ScoreLabel.setFont(font1)

        self.p2FormLayout.setWidget(3, QFormLayout.LabelRole, self.p2ScoreLabel)

        self.p2ScoreInput = QSpinBox(self.mainWidget)
        self.p2ScoreInput.setObjectName(u"p2ScoreInput")
        with open('./TourneyOverlay/Player 2/score.txt', 'r') as file:
            self.p2ScoreInput.setValue(int(file.read()))
        self.p2ScoreInput.valueChanged.connect(self.setP2Score)

        self.p2FormLayout.setWidget(3, QFormLayout.FieldRole, self.p2ScoreInput)


        self.p2Layout.addLayout(self.p2FormLayout)


        self.infoLayout.addLayout(self.p2Layout)


        self.mainLayout.addLayout(self.infoLayout)

        self.line = QFrame(self.mainWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.mainLayout.addWidget(self.line)

        self.quickActionsLayout = QHBoxLayout()
        self.quickActionsLayout.setObjectName(u"quickActionsLayout")
        self.scoreLayout = QVBoxLayout()
        self.scoreLayout.setObjectName(u"scoreLayout")
        self.p1WinButton = QPushButton(self.mainWidget)
        self.p1WinButton.setObjectName(u"p1WinButton")
        sizePolicy1.setHeightForWidth(self.p1WinButton.sizePolicy().hasHeightForWidth())
        self.p1WinButton.setSizePolicy(sizePolicy1)
        self.p1WinButton.setFont(font1)
        self.p1WinButton.clicked.connect(self.p1Win)

        self.scoreLayout.addWidget(self.p1WinButton)

        self.p2WinButton = QPushButton(self.mainWidget)
        self.p2WinButton.setObjectName(u"p2WinButton")
        sizePolicy1.setHeightForWidth(self.p2WinButton.sizePolicy().hasHeightForWidth())
        self.p2WinButton.setSizePolicy(sizePolicy1)
        self.p2WinButton.setFont(font1)
        self.p2WinButton.clicked.connect(self.p2Win)

        self.scoreLayout.addWidget(self.p2WinButton)

        self.scoreResetButton = QPushButton(self.mainWidget)
        self.scoreResetButton.setObjectName(u"scoreResetButton")
        sizePolicy1.setHeightForWidth(self.scoreResetButton.sizePolicy().hasHeightForWidth())
        self.scoreResetButton.setSizePolicy(sizePolicy1)
        self.scoreResetButton.setFont(font1)
        self.scoreResetButton.clicked.connect(self.resetScores)

        self.scoreLayout.addWidget(self.scoreResetButton)


        self.quickActionsLayout.addLayout(self.scoreLayout)

        self.line_3 = QFrame(self.mainWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.quickActionsLayout.addWidget(self.line_3)

        self.swapLayout = QVBoxLayout()
        self.swapLayout.setObjectName(u"swapLayout")
        self.swapLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.swapLabel = QLabel(self.mainWidget)
        self.swapLabel.setObjectName(u"swapLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.swapLabel.sizePolicy().hasHeightForWidth())
        self.swapLabel.setSizePolicy(sizePolicy2)
        self.swapLabel.setFont(font)
        self.swapLabel.setAlignment(Qt.AlignCenter)

        self.swapLayout.addWidget(self.swapLabel)

        self.swapPlayersButton = QPushButton(self.mainWidget)
        self.swapPlayersButton.setObjectName(u"swapPlayersButton")
        sizePolicy1.setHeightForWidth(self.swapPlayersButton.sizePolicy().hasHeightForWidth())
        self.swapPlayersButton.setSizePolicy(sizePolicy1)
        self.swapPlayersButton.setFont(font1)
        self.swapPlayersButton.clicked.connect(self.swapPlayers)

        self.swapLayout.addWidget(self.swapPlayersButton)

        self.swapCommentatorsButton = QPushButton(self.mainWidget)
        self.swapCommentatorsButton.setObjectName(u"swapCommentatorsButton")
        sizePolicy1.setHeightForWidth(self.swapCommentatorsButton.sizePolicy().hasHeightForWidth())
        self.swapCommentatorsButton.setSizePolicy(sizePolicy1)
        self.swapCommentatorsButton.setFont(font1)
        self.swapCommentatorsButton.clicked.connect(self.swapCommentators)

        self.swapLayout.addWidget(self.swapCommentatorsButton)


        self.quickActionsLayout.addLayout(self.swapLayout)


        self.mainLayout.addLayout(self.quickActionsLayout)


        self.verticalLayout.addLayout(self.mainLayout)

        mainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Tourney Overlay", None))
        self.setLabel.setText(QCoreApplication.translate("mainWindow", u"Set Info", None))
        self.setRoundLabel.setText(QCoreApplication.translate("mainWindow", u"Round:", None))
        self.setRoundInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Grand Finals", None))
        self.setGamesLabel.setText(QCoreApplication.translate("mainWindow", u"Games:", None))
        self.setGamesInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Best of 3", None))
        self.commentaryLabel.setText(QCoreApplication.translate("mainWindow", u"Commentary", None))
        self.commentary1Label.setText(QCoreApplication.translate("mainWindow", u"Commentator 1:", None))
        self.commentary1Input.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Commentator1", None))
        self.commentary2Label.setText(QCoreApplication.translate("mainWindow", u"Commentator 2:", None))
        self.commentary2Input.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Commentator2", None))
        self.p1Label.setText(QCoreApplication.translate("mainWindow", u"Player 1", None))
        self.p1TagLabel.setText(QCoreApplication.translate("mainWindow", u"Tag:", None))
        self.p1TagInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Player1", None))
        self.p1SponsorLabel.setText(QCoreApplication.translate("mainWindow", u"Sponsor:", None))
        self.p1SponsorInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"TO", None))
        self.p1SocialLabel.setText(QCoreApplication.translate("mainWindow", u"Social:", None))
        self.p1SocialInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"@player1", None))
        self.p1ScoreLabel.setText(QCoreApplication.translate("mainWindow", u"Score:", None))
        self.p2Label.setText(QCoreApplication.translate("mainWindow", u"Player 2", None))
        self.p2TagLabel.setText(QCoreApplication.translate("mainWindow", u"Tag:", None))
        self.p2TagInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Player2", None))
        self.p2SponsorLabel.setText(QCoreApplication.translate("mainWindow", u"Sponsor:", None))
        self.p2SponsorInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"TO", None))
        self.p2SocialLabel.setText(QCoreApplication.translate("mainWindow", u"Social:", None))
        self.p2SocialInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"@player2", None))
        self.p2ScoreLabel.setText(QCoreApplication.translate("mainWindow", u"Score:", None))
        self.p1WinButton.setText(QCoreApplication.translate("mainWindow", u"P1 Win", None))
        self.p2WinButton.setText(QCoreApplication.translate("mainWindow", u"P2 Win", None))
        self.scoreResetButton.setText(QCoreApplication.translate("mainWindow", u"Reset Score", None))
        self.swapLabel.setText(QCoreApplication.translate("mainWindow", u"Swap", None))
        self.swapPlayersButton.setText(QCoreApplication.translate("mainWindow", u"Players", None))
        self.swapCommentatorsButton.setText(QCoreApplication.translate("mainWindow", u"Commentators", None))
    # retranslateUi

    def saveValue(self, path, value):
        with open(path, 'w') as file:
            file.write(value)

    def setRound(self):
        self.saveValue('./TourneyOverlay/Set/round.txt', self.setRoundInput.text())

    def setGames(self):
        self.saveValue('./TourneyOverlay/Set/games.txt', self.setGamesInput.text())

    def setP1Tag(self):
        tag = ''
        if self.p1SponsorInput.text():
            tag += self.p1SponsorInput.text() + ' | '
        tag += self.p1TagInput.text()
        self.saveValue('./TourneyOverlay/Player 1/tag.txt', tag)

    def setP1Social(self):
        self.saveValue('./TourneyOverlay/Player 1/social.txt', self.p1SocialInput.text())

    def setP1Score(self):
        self.saveValue('./TourneyOverlay/Player 1/score.txt', str(self.p1ScoreInput.value()))

    def setP2Tag(self):
        tag = ''
        if self.p2SponsorInput.text():
            tag += self.p2SponsorInput.text() + ' | '
        tag += self.p2TagInput.text()
        self.saveValue('./TourneyOverlay/Player 2/tag.txt', tag)

    def setP2Social(self):
        self.saveValue('./TourneyOverlay/Player 2/social.txt', self.p2SocialInput.text())

    def setP2Score(self):
        self.saveValue('./TourneyOverlay/Player 2/score.txt', str(self.p2ScoreInput.value()))

    def setCommentator1(self):
        self.saveValue('./TourneyOverlay/Commentators/1.txt', self.commentary1Input.text())

    def setCommentator2(self):
        self.saveValue('./TourneyOverlay/Commentators/2.txt', self.commentary2Input.text())

    def p1Win(self):
        self.p1ScoreInput.setValue(self.p1ScoreInput.value() + 1)

    def p2Win(self):
        self.p2ScoreInput.setValue(self.p2ScoreInput.value() + 1)

    def resetScores(self):
        self.p1ScoreInput.setValue(0)
        self.p2ScoreInput.setValue(0)

    def swapPlayers(self):
        temp = [self.p1TagInput.text(), self.p1SponsorInput.text(), self.p1SocialInput.text(), self.p1ScoreInput.value()]
        
        self.p1TagInput.setText(self.p2TagInput.text())
        self.p1SponsorInput.setText(self.p2SponsorInput.text())
        self.p1SocialInput.setText(self.p2SocialInput.text())
        self.p1ScoreInput.setValue(self.p2ScoreInput.value())

        self.p2TagInput.setText(temp[0])
        self.p2SponsorInput.setText(temp[1])
        self.p2SocialInput.setText(temp[2])
        self.p2ScoreInput.setValue(temp[3])

    def swapCommentators(self):
        temp = self.commentary1Input.text()

        self.commentary1Input.setText(self.commentary2Input.text())
        self.commentary2Input.setText(temp)

def makeFiles():
    import os
    
    dirs = ['./TourneyOverlay','./TourneyOverlay/Set','./TourneyOverlay/Commentators','./TourneyOverlay/Player 1','./TourneyOverlay/Player 2']
    for dir in dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)
    
    files = ['Set/round.txt','Set/games.txt','Commentators/1.txt','Commentators/2.txt','Player 1/tag.txt','Player 1/social.txt','Player 1/score.txt','Player 2/tag.txt','Player 2/social.txt','Player 2/score.txt']
    for path in files:
        if 'score' in path:
            with open(f'./TourneyOverlay/{path}', 'w+') as file:
                file.write('0')
        else:
            open(f'./TourneyOverlay/{path}', 'w+').close()

if __name__ == "__main__":
        try:
            file = open('./TourneyOverlay/Set/round.txt')
            file.close()
        except FileNotFoundError:
            makeFiles()

        import sys
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = Ui_mainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())