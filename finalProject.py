'''


 '''
from tkinter import *
import json
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import os

root = Tk()
root.title("Hiset")
root.minsize(300, 200)
root.configure(bg='white')
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))

#Used for the width of some of the buttons
width = 15
#Used for the height of some of the buttons
height = 8
#Used to put verticle space between some of the buttons
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

#This function initializes and runs the quiz.
def test(num):
     #Sets a white frame to cover up the root window
     blankFrame = Frame(root, bg='white')
     blankFrame.grid(row=0, rowspan= 7, column=0, sticky='nsew')
     root.grid_columnconfigure(0,weight=1)
     #This frame is what all of the quiz widgets go into
     frame1 = Frame(blankFrame, bg="white")
     frame1.grid(row=0, column=0, sticky="")
     #If the mathPage button was pressed, opens the math.json file and stores the contents within the variable data.
     if num == 1:
          with open('math.json') as f:
               data = json.load(f)
          Label(frame1, text="HiSet Math Practice Test", font=("ariel",16, "bold"), bg="white").grid(row=0, column=1, pady=5)

     #If the englishPage button was pressed, opens the english.json file and stores the contents within the variable data.
     elif num == 2:
          with open('english.json') as f:
               data = json.load(f)
          Label(frame1, text="HiSet English Practice Test", font=("ariel",16, "bold"), bg="white").grid(row=0, column=1, pady=5)

     #If the sciencePage button was pressed, opens the science.json file and stores the contents within the variable data.
     elif num ==3:
          with open('science.json') as f:
               data = json.load(f)
          Label(frame1, text="HiSet Science Practice Test", font=("ariel",16, "bold"), bg="white").grid(row=0, column=1, pady=5)

     #If the socialPage button was pressed, opens the social.json file and stores the contents within the variable data.
     elif num == 4:
          with open('social.json') as f:
               data = json.load(f)
          Label(frame1, text="HiSet Social Studies Practice Test", font=("ariel",16, "bold"), bg="white").grid(row=0, column=1, pady=5)
     
     #Gets the 'question' list from the file that is currently opened and saves it to the question varaiable. 
     #Repeats the same process for options, answer, and explination.
     question = (data['question'])
     options = (data['options'])
     answer = (data[ 'answer'])
     explination = (data['explination'])
     
     #Class that contains the code for the quiz.
     class Quiz:
          def __init__(self):
               
               # sets question number to 0
               self.q_no=0
               #This is used to determine whether an answer button has been clicked for the question.
               self.btn_press = 0
               #This function displays the questions and the images.
               self.display_question()
               # opt_selected holds an integer value which is used for
               # selected option in a question.
               self.opt_selected=IntVar()

               self.display_options()
               self.buttons()
               self.display_options()
               # number of questions
               self.data_size=len(question)
               # keeps count of the correct answers
               self.correct=0
               self.submitted=False
          
          # This function shows the current Question on the screen, and displays the images for associated questions.
          def display_question(self):
               #If the social studies test is open and the question number is seven display this image.
               if num == 4 and self.q_no == 7:
                    img = Image.open("Monroe.png")
                    img = img.resize((200, 200), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    self.panel = Label(frame1, image=img)
                    self.panel.image = img
                    self.panel.grid(row=1, column=1)
               #If the science test is open and the question number is two display this
               if num == 3 and self.q_no == 2:
                    img = Image.open("lithium.png")
                    img = img.resize((200, 200), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    self.panel = Label(frame1, image=img)
                    self.panel.image = img
                    self.panel.grid(row=1, column=1)
               # Sets the Question properties
               self.question = Label(frame1, text=question[self.q_no], wraplength=600,
               font=( 'ariel', 13 ), bg="white", anchor= 'w')
               #places the question on the screen
               self.question.grid(row=2, column=1, pady=10)

               #This function sets and displays the four option buttons
          def display_options(self):
               self.optn1 = Button(frame1, wraplength=600, justify=LEFT, cursor="hand2", font=("ariel",12), text= options[self.q_no][0], command=lambda: [self.check_ans(1)])
               self.optn1.grid(row=3, column = 1, pady=2, ipadx=12)
               self.optn2 = Button(frame1, wraplength=600, justify=LEFT, cursor="hand2", font=("ariel",12), text= options[self.q_no][1], command=lambda: [self.check_ans(2)])
               self.optn2.grid(row=4, column = 1, pady=2, ipadx=12)
               self.optn3 = Button(frame1, wraplength=600, justify=LEFT, cursor="hand2", font=("ariel",12), text= options[self.q_no][2], command=lambda: [self.check_ans(3)])
               self.optn3.grid(row=5, column = 1, pady=2, ipadx=12)
               self.optn4 = Button(frame1, wraplength=600, justify=LEFT, cursor="hand2", font=("ariel",12), text= options[self.q_no][3], command=lambda: [self.check_ans(4)])
               self.optn4.grid(row=6, column = 1, pady=2, ipadx=12)

          # This method is used to display the result.
          # It counts the number of correct and wrong answers and then displays them at the end of the test as a message Box.
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
          
          # This method checks the answer after the user clicks next, adds the user's score, and displays the answers explination.
          def check_ans(self, selected_optn):
               #Displays the explination for the correct answer.
               self.explain = Label(frame1, bg="white", text=explination[self.q_no], wraplength=600,
               font=( 'ariel' ,12 ), anchor= 'w' )
               self.explain.grid(row=9, column=1)
               #Shows that an answer button has been pressed.
               self.btn_press +=1
               # checks for if the selected option is correct
               if self.btn_press == 1:
                    #If the answer is correct add one to the correct count and display correct on the screen
                    if selected_optn== answer[self.q_no]:
                         self.correct += 1
                         self.result = Label(frame1, text="Correct", fg="green", bg="white", font=("ariel",12,"bold"))
                         self.result.grid(row=8, column=1)
                         return True
                    else:
                         #If it was not correct then display incorrect
                         self.result = Label(frame1, text="Incorrect", fg="red", bg="white", font=("ariel",12,"bold"))
                         self.result.grid(row=8, column=1)
                         return False
                    
          #This function creates the back button and next button.
          def buttons(self):
               self.backbtn = Button(frame1, text="Back", command = self.del_frame)
               self.backbtn.grid(row=0, column=0)
               self.next_button = Button(frame1, text="Next",command=self.next_btn,
               width=8,bg="black",fg="white", cursor="hand2", font=("ariel",12,"bold"))
               self.next_button.grid(row=7, column= 1, padx=30, pady=5)

          #Once the back button is clicked it deletes the blankFrame 
          #which gives the illusion that the user is traveling back to the main page
          def del_frame(self):
               blankFrame.destroy()
          
          #This function clears the screen and moves to the next question.
          #If all the questions have been answered it calls a function which opens window that tells the user their final score
          #And deletes blankFrame thus taking the user back to the menu.
          def next_btn(self): 
               #Determines if the user has pressed an button
               if self.btn_press >=  1:
                    # Moves to next Question by incrementing the q_no counter
                    self.q_no += 1
                    #If an image is on the screen clear it
                    if num == 4 and self.q_no == 8 or num == 3 and self.q_no == 3:
                         self.panel.destroy()
                    #Makes the previous question, buttons, explanation, and result dissapear after the user clicks next.
                    self.optn1.destroy()
                    self.optn2.grid_forget()
                    self.optn3.grid_forget()
                    self.optn4.grid_forget()
                    self.explain.grid_forget()
                    self.question.grid_forget()
                    self.result.grid_forget()
                    self.explain.grid_forget()
                    #Resets the button press count to 0
                    self.btn_press=0
                    
                    # checks if the q_no size is equal to the data size
                    if self.q_no==self.data_size:
                         # if it is then it displays the score and the application ends
                         self.display_result()
                         # destroys the frame
                         blankFrame.destroy()
                    else:
                         # if not it shows the next question
                         self.display_question()
                         self.display_options()
    
     quiz = Quiz()
root.mainloop()

#I got the basic starting code for this program from https://www.geeksforgeeks.org/python-mcq-quiz-game-using-tkinter/ 