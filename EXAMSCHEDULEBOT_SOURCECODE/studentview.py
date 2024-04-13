import tkinter as tk
import sqlite3
from nltk.chat.util import Chat, reflections
from prettytable import PrettyTable, prettytable

class ExamSchedulerChatbot:
    def __init__(self, master):
        #windows tab name
        self.master = master
        master.title("Student Chatbot")
        master.configure(bg ="light cyan")
        
        #connection with sqlite
        self.con = sqlite3.connect('exam_two.db')
        self.c = self.con.cursor()

        #creates GUI frame windows 
        self.chat_frame = tk.Frame(master,bg ="light cyan")
        self.chat_frame.pack(side=tk.TOP, padx=10, pady=10)


        #create heading label/title label name
        title_label = tk.Label(self.chat_frame, text="Student Exam Schedule Chatbot", bg="light blue", fg="black", font=("Arial", 14))
        title_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # create chat history text box
        self.chat_history = tk.Text(self.chat_frame, height=30, width=99)
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.pack(side=tk.LEFT, padx=10, pady=10)

        # create scrollbar for chat history
        self.chat_scrollbar = tk.Scrollbar(self.chat_frame)
        self.chat_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # configure scrollbar to work with chat history
        self.chat_scrollbar.config(command=self.chat_history.yview)
        self.chat_history.config(yscrollcommand=self.chat_scrollbar.set)

        # entry field of textbox for user
        self.chat_input = tk.Entry(self.chat_frame, width=50)
        self.chat_input.pack(side=tk.LEFT, padx=10, pady=10)

        # submit button
        self.chat_submit = tk.Button(self.chat_frame, text="Submit", command=self.submit)
        self.chat_submit.pack(side=tk.LEFT, padx=10, pady=10)

        # create clear button
        self.chat_clear = tk.Button(self.chat_frame, text="Clear", command=self.clear)
        self.chat_clear.pack(side=tk.LEFT, padx=10, pady=10)

        # Quit button
        self.chat_quit = tk.Button(self.chat_frame, text="Quit", command=master.quit)
        self.chat_quit.pack(side=tk.RIGHT, padx=10, pady=10)
        #Automatic response by bot
        self.chat("bot: Welcome to Exam Scheduler Chatbot!")
        self.chat("bot: Please enter your Register no:")
        self.context = 'register_no'

    #arrange the message type    
    def chat(self, message="", sender="bot"):
        self.chat_history.config(state=tk.NORMAL)
        tag = 'bot' if sender == 'bot' else 'user'
        justify = 'left' if sender == 'bot' else 'right'
        color = 'black' if sender == 'bot' else 'green'
        self.chat_history.tag_configure(tag, justify=justify, foreground=color)
        self.chat_history.insert(tk.END, message + '\n', tag)
        self.chat_history.config(state=tk.DISABLED)
    
    

     #get_schedule retrieve the table details from sql /database file 
     # this db file has two tables first one named as admin table verify the register no, department, dob
     # second table will execute the output from stud_bio table by merging with admin table 
    def get_schedule(self, register_no):
       query = """
             SELECT 
                exam_schedule.register_no, 
                exam_schedule.full_name, 
                exam_schedule.student_class, 
                exam_schedule.dob_indian,
                
                exam_schedule.paper_code1, 
                exam_schedule.exam_date1, 
                exam_schedule.exam_time1, 
                exam_schedule.location1,
                exam_schedule.paper_code2, 
                exam_schedule.exam_date2, 
                exam_schedule.exam_time2, 
                exam_schedule.location2, 
                exam_schedule.paper_code3, 
                exam_schedule.exam_date3, 
                exam_schedule.exam_time3, 
                exam_schedule.location3,
                
                exam_schedule.ar_papercode, 
                exam_schedule.ar_examdate, 
                exam_schedule.ar_examtime, 
                exam_schedule.ar_location
            FROM 
                exam_schedule 
                INNER JOIN students ON exam_schedule.register_no = students.register_no 
            WHERE 
                exam_schedule.register_no = ?"""
       self.c.execute(query, (register_no,))
       result = self.c.fetchall()
    
    # rest of the code
        #if result is present
       if result:
        #create table
          table1 = PrettyTable(['Register no','Student name','Class', 'DOB'])
          
          table2 = PrettyTable([ 'Paper Code', 'Exam Date', 'Exam Time', 'Location'])
          table3 = PrettyTable([ 'Paper Code 2', 'Exam Date 2', 'Exam Time 2', 'Location 2'])
          table4 = PrettyTable([ 'Paper Code 3', 'Exam Date 3', 'Exam Time 3', 'Location 3'])
        
          table5 = PrettyTable([ 'Paper Code', 'Exam Date', 'Exam Time', 'Location'])
          for row in result:
            table1.add_row([
                row[0],  # department
                row[1],  # Register no 
                row[2],  # Class
                row[3],  #DOB
            ])
           
            table2.add_row([
                row[4],  # Paper Code
                row[5],  # Exam Date
                row[6],  # Exam Time
                row[7],  # Location
            ])    
            table3.add_row([    
                row[8],  # Paper Code 2
                row[9],  # Exam Date 2
                row[10], # Exam Time 2
                row[11], # Location 2
            ])
            table4.add_row([    
                row[12],  # Paper Code 3
                row[13],  # Exam Date 3
                row[14], # Exam Time 3
                row[15], # Location 3
            ])
            table5.add_row([    
                row[16],  # Paper Code 3
                row[17],  # Exam Date 3
                row[18], # Exam Time 3
                row[19], # Location 3
            ])
          #return table as string
          return " Your Exam Schedule:\n  " + str(table1) + "\n\n"+"Current Exams\n" + str(table2) + "\n\n" + str(table3) + "\n\n" + str(table4) + "\n\n" +"Arrear Exams \n" + str(table5)

    
    #if result is absent
       else:
           return "Sorry, no exam schedule found for your register no."

        
        #verify, retrieve, display the data from database file to chatbot windows (output)
    def submit(self):
        user_input = self.chat_input.get() # user's reply
        self.chat_input.delete(0, tk.END)
        response=""
        if self.context == 'register_no':
           self.register_no = user_input # user's reply for Admin name
           response = "Please enter your full name:"
           self.context = 'full_name'
        elif self.context == 'full_name':
           self.full_name = user_input # user's reply for department
           response = "Please enter your class:"
           self.context = 'student_class'
        elif self.context == 'student_class':
           self.admin_class = user_input # user's reply for class
           response = "Please enter your date of birth (dd/mm/yyyy):"
           self.context = 'dob_indian'    
        elif self.context == 'dob_indian':
           self.batch_year = user_input # user's reply for date of birth
           response = self.get_schedule(self.register_no) # gets value using admin_name as main foreign key in sql
           self.context = 'register_no'

        self.chat("You: " + user_input, sender='user') # User response
        self.chat("bot: " + response,sender='bot') # bot response
        self.chat_input.delete(0, tk.END) # deletes the text in entry textbox field

    def clear(self):
        self.chat_input.delete(0, tk.END)
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.delete('2.0', tk.END) # only delete user's input, leave bot's messages
        self.chat_history.config(state=tk.DISABLED)
        self.context = 'register_no'
    # check if there are any bot messages in chat history
        chat_lines = self.chat_history.get('2.0', tk.END).split('\n')
        bot_messages = [line for line in chat_lines if line.startswith('bot:')]
        if len(bot_messages) == 0:
           self.chat(" Please enter your Register no:")
        else:
           self.chat(bot_messages[0])
           self.chat(bot_messages[1])

        
    def run(self):
        self.master.mainloop()
        
root = tk.Tk()
chatbot = ExamSchedulerChatbot(root) #end of gui windows
chatbot.run()
