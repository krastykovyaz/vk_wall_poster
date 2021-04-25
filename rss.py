import re
import lib
import constants as const
import functools

def hook_channel(channel):
	pass

def hook_entry(reg_exclude, entry):
	result = reg_exclude.match(entry._link)
	if result == None:
		return entry
	else:
		return None

def run():
	gr = lib.GReader()
	# if not gr.login(const.EMAIL, const.PASSWORD):
	# 	print "login failed"
	# 	return
	
	pattern     = 'http://habrahabr.ru/blogs/(%s)/.*'
	w           = 'javascript|php|Flash_Platform'
	reg_exclude = re.compile(pattern % w, re.IGNORECASE)
	fhook_entry = functools.partial(hook_entry, reg_exclude)
  
	xml = gr.read_tag("habrahabr.ru", 300, hook_channel, fhook_entry)

	print("Content-Type: text/xml")
	print(xml)

if __name__=='__main__' :
	run()