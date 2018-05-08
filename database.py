import sqlite3

def db_account_exists(email):
    conn = sqlite3.connect('schedule.db')
    c = conn.cursor()
    c.execute('SELECT * FROM account WHERE email = ?', (email,))
    return c.fetchone()

def db_account_Store(email, password):
    #file name of database needed to be changed 
    conn = sqlite3.connect('schedule.db')
    c = conn.cursor()
    c.execute('INSERT INTO account (email, password) VALUES (?,?)', (email, password))
    conn.commit()

# In[15]:


def db_transaction_account(userEmail,userPassword):
    import random 
    rand = random.choice('0123456789') # Chooses a random element
    rand1 = random.choice('0123456789')
    rand2 = random.choice('0123456789')
    rand3 = random.choice('0123456789')
    userName = ""
    userID = ""
    #UserID is consisted with userNmae and a 3 digits random number 
    for i in userEmail:
        if i == '@':
            break
        else:
            userName = userName + i
    userID = userName + rand + rand1 + rand2 + rand3
    db_information = (userID, userEmail, userPassword)
    return db_information 


# In[13]:


def db_task_Store(task):
    #file name of database needed to be changed 
    conn = sqlite3.connect('schedule.db')
    c = conn.cursor()
    c.execute(('INSERT INTO Account VALUES (?,?,?,?,?,?,?)', task))
    conn.commit()


# In[1]:


def db_transaction_task(userID,account_id, task_Name, type, description, date):
    task = (userID,account_id, task_Name, type, description, date,time)
    return task 


# In[23]:


def db_Login(userEmail, userPassword):
    #file name of database needed to be changed 
    conn = sqlite3.connect('schedule.db')
    c = conn.cursor()
    # c.execute('Select email  From account Where email = %s'%userEmail)
    # email = c.fetchone()[0]
    # if email.strip() == "":
    #     return False 
    # c.execute('Select password From account Where password = %s'%userPassword )
    # password = c.fetchone()[0]
    # if password.strip() == "":
    #     return False 
    c.execute('SELECT password FROM account WHERE email = ?', (userEmail,))
    pw = c.fetchone()[0]
    print(pw, userPassword)
    return pw is not None and pw == userPassword


# In[24]:


def extract_task(Id):
    
    #file name of database needed to be changed 
    conn = sqlite3.connect('schedule.db')
    c = conn.cursor()
    c.execute('Select *  From account Where id = %s'%Id)
    account_id = c.fetchone()[1]
    task_name = c.fetchone()[2]
    task_description = c.fetchone()[3]
    date_time = c.fetchone()[4]
    task = (account_id,task_name,task_description, date_time)
    return task
    

