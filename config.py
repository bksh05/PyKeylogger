import os

dirname = os.path.dirname(__file__)
# location of the files used 
file = {
	"log_file" : os.path.join(dirname, 'log.txt') ,
	"error_file" : os.path.join(dirname , 'error.txt')
}


smtp = {
	#set any email address from which you want to recieve mails
	"sender" : '' ,  
	#Give the email address to where you want to send the log files
	"recipient" : '' , 
	#username of your smtp server
	"username" : '' , 
	#password of the smtp server
	"password" : ''
}


#After how much time (in seconds) the mail shoud be sent to the sender (60 for one minute)
time = 60