#import os module
import os
import pyttsx3
#loop runs for infinite time
print("HELLO,I AM A CHATTING BOT.")
pyttsx3.speak("HELLO,I AM A CHATTING BOT.")
print("PLAESE, TELL ME",end='')
pyttsx3.speak("PLAESE, TELL ME ")
while True:
	print("How can i help you :",end=' ')
	pyttsx3.speak("How can i help you")
	#input from user
	input_usr = input()
	#converting input srting to lowercase
	input_usr = input_usr.lower()
	#checking condition for right statement
	if ((" run " in input_usr)or (" launch "in input_usr) or (" start " in input_usr) or (" open " in input_usr) or (" execute " in input_usr)):
		if((" not " in input_usr) or ("don't " in input_usr) or ("do not" in input_usr) ):
			print("ok")
			pyttsx3.speak("ok")
			continue
		
		else:
			if (("chrome " in input_usr) or ("browser" in input_usr)or ("google" in input_usr)) :
				os.system("chrome")
			elif  (("notepad" in input_usr) or ("editor" in input_usr)or ("text document" in input_usr)):
				os.system("notepad")
			elif (("filmora" in input_usr) or ("wondershare" in input_usr)or ("video editor" in input_usr)):
				os.system("filmora")
			elif (("splashscreen" in input_usr) or ("splash " in input_usr)):
				os.system("splashscreen")
			elif (("mini player" in input_usr) or ("miniplayer" in input_usr)):
				os.system("PotPlayerMini64")
			elif ((" turbo " in input_usr) or (" turboc " in input_usr)):
				os.system("TC")
			elif (("teams" in input_usr) or ("msteams" in input_usr)):
				os.system("Teams")
			elif (("windows mail" in input_usr) or (" mail " in input_usr)):
				os.system("wabmig")
			elif (("microsoft sql server management studio 18" in input_usr) or ("sql server studio" in input_usr)or ("ms sql server studio" in input_usr)):
				os.system("DTASHELL")
			elif (("microsoft sql server " in input_usr) or (" ms sql server " in input_usr)):
				os.system("SQLPS")
			elif (("python" in input_usr) or ("python3" in input_usr)):
				os.system("python")
			elif (("calculator" in input_usr) or (" calci " in input_usr)):
				os.system("calc")
			elif (("today date" in input_usr) or (" date " in input_usr)):
				os.system("date")
			elif ((" excel " in input_usr) or (" exl " in input_usr)):
				os.system("EXCEL")
			elif ((" misc " in input_usr) or (" msc " in input_usr)):
				os.system("MISC")
			elif (("msouc" in input_usr) or ("ms ouc" in input_usr)):
				os.system("MSOUC")
			elif (("msword" in input_usr) or (" winword " in input_usr)):
				os.system("WINWORD")
			elif (("powerpoint" in input_usr) or (" mspoint " in input_usr)or (" ppt " in input_usr)):
				os.system("POWERPNT")
			elif (("organization chart" in input_usr) or (" orgchart " in input_usr)):
				os.system("ORGCHART")
			elif (("microsoft note" in input_usr) or ("ms note" in input_usr)):
				os.system("ONENOTE")
			elif ((" ms-paint " in input_usr) or (" paint " in input_usr)or (" mspaint " in input_usr)):
				os.system("mspaint")
			#commands run with start
			elif ((" camera " in input_usr) or (" webcam " in input_usr)):
				os.system("start microsoft.windows.camera:")
			elif (("3dbuilder" in input_usr) or ("builder3d" in input_usr) or (" 3d builder " in input_usr)):
				os.system("start com.microsoft.builder3d:")
			elif ((" action center " in input_usr) or (" actioncenter " in input_usr)):
				os.system("start ms-actioncenter:")
			elif ((" alarm " in input_usr) or (" clock " in input_usr)or (" alarm-clock " in input_usr)):
				os.system("start ms-clock:")
			elif ((" calender " in input_usr) or (" cal " in input_usr)or (" cald " in input_usr)):
				os.system("start outlookcal:")
			elif ((" 3d-ms-paint " in input_usr) or (" 3d-paint " in input_usr)or (" 3dpaint " in input_usr)):
				os.system("start ms-paint:")
			elif ((" ms-people " in input_usr) or (" mspeople " in input_usr)or (" people " in input_usr)):
				os.system("start ms-people:")
			elif ((" photos " in input_usr) or (" ms-photos " in input_usr)or (" msphotos " in input_usr)):
				os.system("start ms-photos:")
			elif ((" setting " in input_usr) or (" settings " in input_usr)or (" ms-settings " in input_usr)):
				os.system("start ms-settings:")
			elif ((" ms-screenclip " in input_usr) or (" msscreenclip " in input_usr)or (" screen clip " in input_usr)or (" screen snip " in input_usr)):
				os.system("start ms-screenclip:")
			elif ((" bingweather " in input_usr) or (" weather " in input_usr)):
				os.system("start bingweather:")
			elif ((" ms-availablenetworks " in input_usr) or (" availablenetworks " in input_usr)or (" wifi networks " in input_usr)):
				os.system("start ms-availablenetworks:")
			else:
				print("please,check your statement")
				pyttsx3.speak("please,check your statement")
	elif (("good bye" in input_usr) or ("goodbye" in input_usr) or ("exit" in input_usr) or ("quit" in input_usr)):
		print("Good Bye")
		pyttsx3.speak("Good Bye")
		print("it was nice chatting with you, just text me if you need something")
		pyttsx3.speak("it was nice chatting with you, just text me if you need something")
		break
	else:
		print("Sorry, I don’t understand that.")
		pyttsx3.speak("Sorry, I don’t understand that.")
	

