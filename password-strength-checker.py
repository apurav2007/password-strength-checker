########################################################
#        Program to check password strength            #
#                                                      #
#                                                      #
#                 Author - Apurav Gaur                 #
#                                                      #
#                  dated- 2 Nov 2016                   #
#                						               #
########################################################

import re
import getpass
while True:
	#using getpass means that the users input will not be echoed by the terminal
  	password = getpass.getpass('Password: ... ')

    	if 6 <= len(password) <= 12:
    		break
    		print 'The password must be between 6 and 12 characters.\n'

password_scores = {0:'Horrible', 1:'Weak', 2:'Medium', 3:'Strong'}
password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num'], False)
if re.search(r'[A-Z]', password):
	password_strength['has_upper'] = True
if re.search(r'[a-z]', password):
	password_strength['has_lower'] = True
if re.search(r'[0-9]', password):
	password_strength['has_num'] = True

score = len([b for b in password_strength.values() if b])

print 'Password is %s' % password_scores[score]
