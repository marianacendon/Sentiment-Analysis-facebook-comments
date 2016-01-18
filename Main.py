from tkinter import *
import tkinter.messagebox

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Main function in program
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def callback():
    if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        main.destroy()

def setResult(type, res):
    if (type == "neg"):
        negativeLabel.configure(text = "Negative : " + str(res) + " % \n")
    if (type == "neu"):
        neutralLabel.configure( text = "Neutral  : " + str(res) + " % \n")
    if (type == "pos"):
        positiveLabel.configure(text = "Positive : " + str(res) + " % \n")

def runAnalysis():
    sentences = []
    sentences.append(line.get())
    sid = SentimentIntensityAnalyzer()
    for sentence in sentences:
        # print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            setResult(k, ss[k])
                # print('{0}: {1} \n'.format(k, ss[k]), end='')
    print()

def editedText(event):
    typedText.configure(text = "Your text:\n" + line.get() + event.char)

def runByEnter(event):
    runAnalysis()

# Create main window
main = Tk()
main.title("Sentiment Analysis")
main.geometry("500x300")
main.resizable(width=FALSE, height=FALSE)
main.protocol("WM_DELETE_WINDOW", callback)
main.focus()
center(main)

# addition item on window
label1 = Label(text = "Type your review:")
label1.pack()


line = Entry(main, width=70)
line.bind("<Key>",editedText)
line.bind("<Return>",runByEnter)
line.pack()

typedText = Label(text = "Your text:\n")
typedText.pack()

# analysisButton = Button(main, text = "Analysis", width=10, command = runAnalysis)
# analysisButton.grid(row=50, column=550)
# analysisButton.pack()

result = Label(text = "\nResult\n")
result.pack()
negativeLabel = Label(text = "")
negativeLabel.pack()
neutralLabel  = Label(text = "")
neutralLabel.pack()
positiveLabel = Label(text = "")
positiveLabel.pack()
# Run program
mainloop()