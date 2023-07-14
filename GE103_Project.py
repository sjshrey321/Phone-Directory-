'''Our aim is to create a telephone directory using tkinter which is a special library in python.

This telephone directory will help us to add , edit , display and delete user specified contacts in the database.

Furthermore, to facilitate the backend of our program we are using the sqlite3 library given in python.

We have used Graphical User Interface to help the user have an fluid experience.'''

'''Kindly download the provided 'contacts.db' database and store it in the same directory as the python code.'''

from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()


#Below is the code which we used to create our 'contacts.db' which is a database file.

'''connector = sqlite3.connect('contacts.db')

cur = connector.cursor()

cur.execute(""" CREATE TABLE records (
    first_name text,
    last_name text,
    address text,
    phone_number integer
    )""")


connector.commit()

connector.close()
'''


def confirmation_delete():
    ''' This function will ask the user for confirmation for deletion of contact.'''
    global action1
    #Making action1 global as it will be used in another function aswell.
    action1 = messagebox.askyesno('Delete Contact','Are you sure you want to delete this contact?')
    #Implementing messagebox that will ask yes/no question for deletion.


def confirmation_saved():
    ''' This function will notify the user if the contact has been saved.'''
    action = messagebox.showinfo('Saved','Saved successfully')
    #Implementing messagebox that will give confirmation if the record has been saved. 
    
  
def confirmation_saved2():
    ''' This function will notify the user if the contact has been successfully edited.''' 
    action = messagebox.showinfo('Changes','Changes saved successfully')
    #Implementing messagebox that will give confirmation if the record has been edited.
    

def submit():
    '''We will now create a function which will help us in add new enteries in our database
    We will first insert our new recorded values in the database by using the commands below
    Also as we are submitting the new enteries we want to add , we will clear the entry text boxes side by side'''
    
    # The function below will connect us to the database
    connector = sqlite3.connect('contacts.db')
    
    # cursor performs various functions
    cur = connector.cursor()

    # Below we are inserting the new recored values into our new table
    
    cur.execute ( "INSERT INTO records VALUES (:firstname_e,:lastname_e,:address,:phone_e)",
            {   
                    'firstname_e':firstname_e.get(),
                    'lastname_e':lastname_e.get(),
                    'address':address.get(),
                    'phone_e':phone_e.get(),                    
            } )
    confirmation_saved()
    #This will execute the messagebox function and notify the user that the contact has been saved.

    # This actually is :: dummy variable : key value ( similat to dictionary )

    # The function below will commit changes in our database

    connector.commit()

    # The function below will close further enteries in our database
    connector.close()

    # After submitting the new enteries we want to add , we want to clear the entry text boxes
    # For that we are using the commands :
    firstname_e.delete(0,END)
    lastname_e.delete(0,END)
    address.delete(0,END)
    phone_e.delete(0,END)


def query():
    ''' We will now create a function which will help us in listing all the data stored in our database'''

    connector = sqlite3.connect('contacts.db')
    
    cur = connector.cursor()

    # We will select all our enteries/data from the records (table)
    cur.execute ("SELECT *,oid FROM records ")
    rec=cur.fetchall()
    print(rec)

    # We will now be printing our data in a specific format
    print_rec=""
    count = 0

    print_rec=" "+ 'First Name' +'    '+ 'Last Name '+'     '+ 'Address'+ '     '+ 'Phone Number'+ '     '+' ID '+"\n"
    for i in rec:
        count += 1
        
        print_rec = print_rec +"    "+'   '+str(i[0])+"     "+str(i[1])+"     "+str(i[2])+"     "+str(i[3])+'                        ' + str(i[4]) + ("\n")

    # We will be giving a unique ID to each entry in our database to ease our purpose

    # We will represent our data in form of a Label
    
    query_label= Label(frame4,text = print_rec)
    query_label.grid( row=1,column =1, columnspan=2)
    countlabel= Label(frame4,text = 'Total Contacts : '+str(count))
    countlabel.grid(row=0 , column =2)

    connector.commit()
    connector.close()

def update():

    '''This function will enable us to update the data/records stored in the database.
    This function will be used within the edit function in a new window called 'editor'. '''
    

    connector = sqlite3.connect('contacts.db')
    
    cur = connector.cursor()
    
    # record_id will store th information we give in the search_e entry box
    record_id = search_e.get()

    #This execute command will update the records with the values specified by the user using entry boxes.

    #We will be assigning the values the the respective columns (for eg. first_name is assigned to :first)

    #oid refers to the unique id given to every input.
    cur.execute (""" UPDATE records SET
            first_name = :first,
            last_name = :last,
            address = :address,
            phone_number= :phone_e


    
            WHERE oid = :oid """,

            {'first':firstname_e_editor.get(),
             'last':lastname_e_editor.get(),
             'address':address_editor.get(),
             'phone_e':phone_e_editor.get(),

             'oid':record_id
            })

    #This will display the messagebox that whether the edit has been done successfully or not.
    confirmation_saved2()

    #This will close the edit window after the new info has been updated.
    editor.destroy()
    
    connector.commit()

    connector.close()

def edit():
    ''' We will now create a function to edit the input / contacts 
    Here we will be creating a new window with the name : 'editor' 
    In this new window we will be creating several new labels, buttons and entry boxes to edit our input'''

    # We are making a new window : editor and to avoid any clashes / problems we will make it global
    
    global editor
    editor = Tk()
    editor.title('Update a Contact')

    connector = sqlite3.connect('contacts.db')

    cur = connector.cursor()
    #We are making new entry boxes and to avoid any clashes / problems we will make them global    
    global firstname_e_editor
    global lastname_e_editor
    global address_editor
    global phone_e_editor


    # We will now create text boxes for various purposes
    
    firstname_e_editor = Entry(editor,width=30)
    firstname_e_editor.grid(row=0 , column =1, padx=20)
    lastname_e_editor = Entry(editor,width=30)
    lastname_e_editor.grid(row=1 , column =1, padx=20)
    address_editor = Entry(editor,width=30)
    address_editor.grid(row=2 , column =1, padx=20)
    phone_e_editor = Entry(editor,width=30)
    phone_e_editor.grid(row=3 , column =1, padx=20)
    firstname_e_label = Label(editor, text = "First Name")
    firstname_e_label.grid(row=0 ,column = 0)
    lastname_e_label = Label(editor, text = "Last Name")
    lastname_e_label.grid(row=1 ,column = 0)
    address_label = Label(editor, text = "Address")
    address_label.grid(row=2 ,column = 0)
    phone_e_label = Label(editor, text = "Phone number")
    phone_e_label.grid(row=3 ,column = 0)

    save_button=Button(editor, text = 'Save Changes',command=update)
    save_button.grid(row = 5, column=0,columnspan=2,pady=10,padx=10,ipadx=70)

    # record_id will store the value in the entry box : search_e
    # the get function will call the value we entered
    
    record_id = search_e.get()

    
    cur.execute ("SELECT * FROM records WHERE oid= "+search_e.get())
    # The user will be giving the ID displayed on the interface which he wants to edit.
    # The above function will select element corresponding to the input ID/
    
    record=cur.fetchall()
    # fetch.all() brings all the data in database to record
    
    # The loop below inserts the new inputs given by the user to the record (mentioned above)
    # The positions as per the database

    for record in record:
        firstname_e_editor.insert(0,record[0])
        lastname_e_editor.insert(1,record[1])
        address_editor.insert(2,record[2])
        phone_e_editor.insert(3,record[3])
    print(record)

    
    connector.commit()
    
    connector.close()


def show ():
    '''This function will display the record as specified by the user in the ID entry box using first name.'''
    #Creating a new window for the display of specified records.
    spyder = Tk()
    spyder.title('Contact')

    #Connecting the database using connector(defined earlier.)

    connector = sqlite3.connect('contacts.db')

    #Calling out the cursor.
    cur = connector.cursor()
        
    global firstname_e_editor
    global lastname_e_editor
    global address_editor
    global phone_e_editor

    #This will store the entry given in the Enter ID entry box.
    record_id = search_e.get()

    #Creating various labels for display.(Such as First Name,Address etc.)
    firstname_e_editor = Entry(spyder,width=30)
    firstname_e_editor.grid(row=0 , column =1, padx=20)
    lastname_e_editor = Entry(spyder,width=30)
    lastname_e_editor.grid(row=1 , column =1, padx=20)
    address_editor = Entry(spyder,width=30)
    address_editor.grid(row=2 , column =1, padx=20)
    phone_e_editor = Entry(spyder,width=30)
    phone_e_editor.grid(row=3 , column =1, padx=20)
    firstname_e_label = Label(spyder, text = "First Name")
    firstname_e_label.grid(row=0 ,column = 0)
    lastname_e_label = Label(spyder, text = "Last Name")
    lastname_e_label.grid(row=1 ,column = 0)
    address_label = Label(spyder, text = "Address")
    address_label.grid(row=2 ,column = 0)
    phone_e_label = Label(spyder, text = "Phone number")
    phone_e_label.grid(row=3 ,column = 0)
    
    #Insering the different values in the table.
    cur.execute ("SELECT * FROM records WHERE first_name =?",(search_e.get(),))
    record=cur.fetchall()
    #Looping the insert command.
    for record in record:
        firstname_e_editor.insert(0,record[0])
        lastname_e_editor.insert(1,record[1])
        address_editor.insert(2,record[2])
        phone_e_editor.insert(3,record[3])
    print(record)
     


    
    connector.commit()

    connector.close()

def delete():

    '''This function will delete the user specified record using the ID given by the user in the entry box.'''
    connector = sqlite3.connect('contacts.db')

    cur = connector.cursor()

    #This will display a message box asking whether the user wants to delete or not.
    confirmation_delete()
    #If the user clicks 'yes' , '1' will be updated in action1 variable.
    if action1 == 1:
        #If the user has clicked 1 then deletion will take place.
        
        cur.execute("DELETE from records WHERE oid= "+search_e.get())
        connector.commit()

    #Otherwise it will be ignored.
    else:
        pass
    connector.close()

    '''From here on, we have developed the gui of the program using multiple labels,frames,buttons and entry boxes
    which have their particular size,padding,orientation and text.'''

heading = Label(root,text = 'Telephone Directory',font = ('Helvetica',18,'bold'),width = 60)
heading.grid(row = 0,columnspan = 6)

frame1 = Frame(root,width = 100)
frame1.grid(row  = 1,columnspan = 2,column = 0,ipadx = 2,ipady = 300,pady = 10)

frame2 = Frame(root,width = 100)
frame2.grid(row  = 1,columnspan = 2,sticky = 'ns',column = 2,ipadx = 4,ipady = 300,pady = 10)

frame3 = Frame(root,width = 100)
frame3.grid(row  = 1,columnspan = 2,column = 4,ipadx = 2,ipady = 300,pady = 10,sticky = 'ns')

frame4 = Frame(root,width = 80)
frame4.grid(row  = 1,columnspan = 2,column = 4,ipadx = 135,ipady = 340,pady = 40,sticky = 'w')

firstname = Label(frame1,text = 'First Name :',width = 15)
lastname = Label(frame1,text = 'Last Name :',width = 15)
address = Label(frame1,text = 'Address :',width = 15)
phone = Label(frame1,text = 'Phone Number :',width = 15)

firstname.grid(row = 0,column = 0,sticky = 'w',padx = 2,pady = 2)
lastname.grid(row = 1,column = 0,sticky = 'w',padx = 2,pady = 2)
address.grid(row = 2,column = 0,sticky = 'w',padx = 2,pady = 2)
phone.grid(row = 3,column = 0,sticky = 'w',padx = 2,pady = 2)

firstname_e = Entry(frame1,width = 20)
lastname_e = Entry(frame1,width = 20)
address = Entry(frame1,width = 20)
phone_e = Entry(frame1,width = 20)

firstname_e.grid(row = 0,column = 1,pady = 2)
lastname_e.grid(row = 1,column = 1,pady = 2)
address.grid(row = 2,column = 1,pady = 2)
phone_e.grid(row = 3,column = 1,pady = 2)

submit_button = Button(frame1,width = 35,text = 'Add Contact to Directory',command = submit)
submit_button.grid(row = 4,columnspan = 2,pady = 2)

search = Label(frame2,width = 15,text = 'Enter ID ',anchor = 'w')
search.grid(row = 0,column = 0,sticky = 'w',padx = 1,pady = 2)

search_e = Entry(frame2,width = 20)
search_e.grid(row = 0,column = 1,pady = 2,sticky = 'w')

emp = Label(frame2,width = 35,text = 'To show a record,enter first name otherwise enter ID')
emp.grid(row = 1,columnspan = 2,pady = 2,sticky = 'w')

show_button = Button(frame2,width = 35,text = 'Show Contact',command = show)
show_button.grid(row =2,columnspan = 2,pady = 3)

edit_button = Button(frame2,width = 35,text = 'Edit Contact',command = edit)
edit_button.grid(row = 3,columnspan = 2,pady = 3)

delete_button = Button(frame2,width = 35,text = 'Delete Contact',command = delete)
delete_button.grid(row = 4,columnspan = 2,pady = 3)

listall_button = Button(frame3,width = 35,text = 'List All Contacts',command = query)
listall_button.grid(row = 0,columnspan = 5,sticky = 'e')



root.mainloop()
