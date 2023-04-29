'''
Notes: Make it centered. Put the question and answers in a frame. Change the frame to red or green once user clicks submit.
Add a finish test option. Make the comments your own. Remove the correct/wrong label. Disable the option buttons once one is clicked.
change the background color of the button to be red or green depending on if user got the question wrong or right.
impliment a back button. Give a warning to the user stating if they press it their data will be lost, then have yes or no option. 
Give a label at the top indicating which test the user is taking.

 '''

from tkinter import *
import json
from tkinter import messagebox as mb
root = Tk()
root.title("Hiset")
root.geometry("600x400")
root.minsize(300, 200)
root.configure(bg='white')
root.configure(pady="10")

width = 15
height = 8
space = 2

Label(root, text="Hiset practice test.", bg="white", font=('arial', 15)).grid(row=0, column = 0, ipady=(13), ipadx=(10))
Label(root, text="Hello and welcome to the Hiset practice test.\n Below you'll find four practice tests to choose from.", 
     bg="white", font=('Helvetica', 11)).grid(row=1, column = 0, ipady=(15), ipadx=(20))

#If one of the four buttons below are pressed it opens up the test function. 
#Each of the four buttons pass a different number into the test function which indicates which json file should open.
mathPage = Button(root, padx=(width + 27), pady=(height), text=("Math Test"), cursor="hand2", font=('Helvetica', 10), command=lambda: test(1)).grid(row=2, column = 0, ipady=space)
englishPage = Button(root, padx=(width + 20), pady=(height), text=("English Test"), cursor="hand2", font=('Helvetica', 10), command=lambda: test(2)).grid(row=3, column = 0, ipady=space)
sciencePage = Button(root, padx=(width + 18), pady=(height), text=("Science Test"), cursor="hand2", font=('Helvetica', 10), command=lambda: test(3)).grid(row=4, column = 0, ipady=space)
socialStudiesPage = Button(root, padx=(width), pady=(height), text=("Social Studies Test"), cursor="hand2", font=('Helvetica', 10), command=lambda: test(4)).grid(row=5, column = 0, ipady=space)
#Quits the program
buttonQuit = Button(root, text='Exit Program', cursor="hand2", command=root.quit).grid(row=6, column = 0, ipady=space)

def test(num):
     #sets a white frame to cover up the root window
     blankFrame = Frame(root, bg='white')
     blankFrame.grid(row=0, rowspan= 7, column=0, sticky='nsew')
     root.grid_columnconfigure(0,weight=1)
     frame1 = Frame(blankFrame )
     frame1.grid(row=0, column=0, sticky="")

     #If the mathPage button was pressed, opens the math.json file and stores the contents within the variable data.
     if num == 1:
          with open('math.json') as f:
               data = json.load(f)
          Label(frame1, text="HiSet Math Practice Test", font=("ariel",16, "bold"), bg="white").grid(row=0, column=0, pady=5)

     #If the englishPage button was pressed, opens the english.json file and stores the contents within the variable data.
     elif num == 2:
          with open('english.json') as f:
               data = json.load(f)
          Label(frame1, text="HiSet English Practice Test", font=("ariel",16, "bold"), bg="white").grid(row=0, column=0, pady=5)

     #If the sciencePage button was pressed, opens the science.json file and stores the contents within the variable data.
     elif num ==3:
          with open('science.json') as f:
               data = json.load(f)
          Label(frame1, text="HiSet Science Practice Test", font=("ariel",16, "bold"), bg="white").grid(row=0, column=0, pady=5)

     #If the socialPage button was pressed, opens the social.json file and stores the contents within the variable data.
     elif num == 4:
          with open('social.json') as f:
               data = json.load(f)
          Label(frame1, text="HiSet Social Studies Practice Test", font=("ariel",16, "bold"), bg="white").grid(row=0, column=0, pady=5)
     
     #Gets the 'question' list from the file that is currently opened and saves it to the question varaiable. 
     #Repeats the same process for options, answer, and explination.
     question = (data['question'])
     options = (data['options'])
     answer = (data[ 'answer'])
     explination = (data['explination'])
     
     #Class that contains the code for the quiz.
     class Quiz:
          def __init__(self):
               # set question number to 0
               self.q_no=0
              
               self.display_question()
               # opt_selected holds an integer value which is used for
               # selected option in a question.
               self.opt_selected=IntVar()
               
               self.display_options()
               self.buttons()
               self.display_options()
               # no of questions
               self.data_size=len(question)
               # keep a counter of correct answers
               self.correct=0
               self.submitted=False
          
           # This function shows the current Question on the screen.
          def display_question(self):
               # setting the Question properties
               self.question = Label(frame1, text=question[self.q_no], wraplength=600,
               font=( 'ariel', 13 ), bg="white", anchor= 'w' )
               #placing the option on the screen
               self.question.grid(row=1, column=0, pady=5)

               #sets and displays the four option buttons
          def display_options(self):
               self.optn1 = Button(frame1, wraplength=600, justify=LEFT, cursor="hand2", font=("ariel",12), text= options[self.q_no][0], command=lambda: [self.check_ans(1)])
               self.optn1.grid(row=2, column = 0, pady=1, ipadx=10)
               self.optn2 = Button(frame1, wraplength=600, justify=LEFT, cursor="hand2", font=("ariel",12), text= options[self.q_no][1], command=lambda: [self.check_ans(2)])
               self.optn2.grid(row=3, column = 0, pady=1, ipadx=10)
               self.optn3 = Button(frame1, wraplength=600, justify=LEFT, cursor="hand2", font=("ariel",12), text= options[self.q_no][2], command=lambda: [self.check_ans(3)])
               self.optn3.grid(row=4, column = 0, pady=1, ipadx=10)
               self.optn4 = Button(frame1, wraplength=600, justify=LEFT, cursor="hand2", font=("ariel",12), text= options[self.q_no][3], command=lambda: [self.check_ans(4)])
               self.optn4.grid(row=5, column = 0, pady=1, ipadx=10)

          # This method is used to display the result.
          # It counts the number of correct and wrong answers and then display them at the end as a message Box.
          def display_result(self):
               # calculates the wrong count
               wrong_count = self.data_size - self.correct
               correct = f"Correct: {self.correct}"
               wrong = f"Wrong: {wrong_count}"
               # calcultaes the percentage of correct answers
               score = int(self.correct / self.data_size * 100)
               result = f"Score: {score}%"
               # Shows a message box to display the result
               mb.showinfo("Result", f"{result}\n{correct}\n{wrong} \n\nReturn to main menu")
          
          # This method checks the Answer after we click on Next.
          def check_ans(self, selected_optn):
               self.explain = Label(frame1, text=explination[self.q_no], wraplength=600,
               font=( 'ariel' ,12 ), anchor= 'w' )
               self.explain.grid(row=8, column=0)
               # checks for if the selected option is correct
               if selected_optn== answer[self.q_no]:
                    self.correct += 1
                    self.result = Label(frame1, text="Correct", fg="green", font=("ariel",12,"bold"))
                    self.result.grid(row=7, column=0)
                    return True
               else:
                    self.result = Label(frame1, text="Incorrect", fg="red", font=("ariel",12,"bold"))
                    self.result.grid(row=7, column=0)
                    return False


          def buttons(self):
               self.next_button = Button(frame1, text="Next",command=self.next_btn,
               width=8,bg="black",fg="white", cursor="hand2", font=("ariel",12,"bold"))
               self.next_button.grid(row=6, column= 0, padx=30, pady=5)
          def next_btn(self): 
               # Moves to next Question by incrementing the q_no counter
               self.q_no += 1
               self.optn1.grid_forget()
               self.optn2.grid_forget()
               self.optn3.grid_forget()
               self.optn4.grid_forget()
               self.explain.grid_forget()
               self.question.grid_forget()
               self.result.grid_forget()

               # checks if the q_no size is equal to the data size
               if self.q_no==self.data_size:
                    # if it is correct then it displays the score
                    self.display_result()
                    # destroys the frame
                    blankFrame.destroy()
               else:
                    # shows the next question
                    self.display_question()
                    self.display_options()
    
     quiz = Quiz()
# Start the GUI
 
root.mainloop()