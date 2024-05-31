#--*-- coding utf-8 by nexus-br
import time as t
def time():
	timenow = t.localtime()
	now = int(t.strftime("%H"))
	return now
if 6 < time() < 12:
	print("bom dia amigo")
elif 12 < time() <= 18:
	print("boa tarde amigo")
else:
	print("boa noite amigo")