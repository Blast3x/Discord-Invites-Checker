import os
import re
import json
import requests
from urllib.request import Request, urlopen
from requests import get
from ab5 import hgratient



def checker(value):
	os.system("mode 90, 27")
	os.system("title ")
	logo = '''
			discord		invite		checker
						
					by 

				github.com/Blast3x
	'''
	start_color=[255,0,0]
	end_color=[0,0,255]
	content = get(f'https://discord.com/api/v9/invites/{value}?with_counts=true').text
	jsobj = json.loads(content)
	linkcode = str(jsobj["code"])
	linktype = str(jsobj["type"])
	linkexpiry = str(jsobj["expires_at"])
	approxmember = str(jsobj["approximate_member_count"])
	approxpresence = str(jsobj["approximate_presence_count"])
	serverid = str(jsobj["guild"]["id"])
	servername = str(jsobj["guild"]["name"])
	serversplash = str(jsobj["guild"]["splash"])
	serverbanner = str(jsobj["guild"]["banner"])
	serverdesc = str(jsobj["guild"]["description"])
	servericon = str(jsobj["guild"]["icon"])
	serverfeat = str(jsobj["guild"]["features"])
	serververific = str(jsobj["guild"]["verification_level"])
	servervanity = str(jsobj["guild"]["vanity_url_code"])
	servernitro = str(jsobj["guild"]["premium_subscription_count"])
	servernsfw = str(jsobj["guild"]["nsfw"])
	serversnfwlevel = str(jsobj["guild"]["nsfw_level"])
	channelid = str(jsobj["channel"]["id"])
	channelname = str(jsobj["channel"]["name"])
	channeltype = str(jsobj["channel"]["type"])
	'''
	if jsobj["code"] == jsobj["guild"]["vanity_url_code"]:
		code = jsobj["code"]
		expiry = jsobj["expires_at"]
		os.system("cls")
		os.system(f"title 	discord.gg/{code}  expiry: {expiry}")
		print(hgratient(logo,start_color,end_color))
		print(hgratient("  server info",start_color,end_color))
	else:'''
	code = jsobj["code"]
	expiry = jsobj["expires_at"]
	os.system("cls")
	os.system(f"title 	discord.gg/{code}  expiry: {expiry}")
	print(hgratient(logo,start_color,end_color))
	if "inviter" in content:
		print(hgratient("  server info						    user info",start_color,end_color))
		inviterid = str(jsobj["inviter"]["id"])
		inviterusername = str(jsobj["inviter"]["username"])
		inviteravatar = str(jsobj["inviter"]["avatar"])
		inviterdeco = str(jsobj["inviter"]["avatar_decoration"])
		invitertag = str(jsobj["inviter"]["discriminator"])
		inviterflags = str(jsobj["inviter"]["public_flags"])
		print(hgratient("● members: "+approxmember+"					● id: "+inviterid,start_color,end_color),end ="")
		print(hgratient("● online: "+approxpresence+"					● name: "+inviterusername,start_color,end_color),end ="")
		print(hgratient("● server id: "+serverid+"				● tag: "+invitertag,start_color,end_color),end ="")
		print(hgratient("● name: "+servername+"					● flags: "+inviterflags,start_color,end_color),end ="")
	else:
		print(hgratient("  server info",start_color,end_color))
		print(hgratient("● members: "+approxmember,start_color,end_color),end ="")
		print(hgratient("● online: "+approxpresence,start_color,end_color),end ="")
		print(hgratient("● server id: "+serverid,start_color,end_color),end ="")
		print(hgratient("● name: "+servername,start_color,end_color),end ="")
	print(hgratient("● splash: "+serversplash,start_color,end_color),end ="")
	print(hgratient("● banner: "+serverbanner,start_color,end_color),end ="")
	print(hgratient("● description: "+serverdesc,start_color,end_color),end ="")
	print(hgratient("● icon: "+servericon,start_color,end_color),end ="")
	print(hgratient("● verification: "+serververific,start_color,end_color),end ="")
	if servervanity == "None":
		print(hgratient("● vanity url: "+servervanity,start_color,end_color),end ="")
	else:
		print(hgratient("● vanity url: discord.gg/"+servervanity,start_color,end_color),end ="")
	#print(hgratient("● vanity url: discord.gg/"+servervanity,start_color,end_color),end ="")
	print(hgratient("● server booster: "+servernitro,start_color,end_color),end ="")
	print(hgratient("● nsfw: "+servernsfw,start_color,end_color),end ="")
	print(hgratient("● nsfw level: "+serversnfwlevel,start_color,end_color),end ="")
	print(hgratient("			type info for more infos or exit to close",start_color,end_color),end ="")
	inputvar = input("					")
	if inputvar == "info":
		file = open(f"C:\\Users\\Asrock\\Desktop\\tokengrabber\\{servername} infos.txt", "a")
		file.seek(0)
		file.truncate()
		file.write("https://github.com/Blast3x - https://github.com/Blast3x - https://github.com/Blast3x - https://github.com/Blast3x\n")
		file.write(str(jsobj))
		file.close()
		os.system(f"msg * all the infos has been written in {servername} infos.txt")
	if inputvar == "exit":
		exit()

def main():
	os.system("mode 90, 27")
	os.system("title ")
	logo = '''
			discord		invite		checker
						
					by 

				github.com/Blast3x
	'''
	# color in decemal rgb [red,green,blue] (max 255 min 0)
	start_color=[255,0,0]
	end_color=[0,0,255]

	print(hgratient(logo,start_color,end_color))
	print(hgratient("					code",start_color,end_color))
	os.system("echo [40;34m				")
	invite = input("				 ")


	if "invite/" in invite:
		splitted1 = invite.split("invite/")
		va1 = str(splitted1[1])
		checker(va1)

	if ".com/" in invite:
	    splitted2 = invite.split(".com/")
	    va2 = str(splitted2[1])
	    checker(va2)

	if ".gg/" in invite:
	    splitted3 = invite.split(".gg/")
	    va3 = str(splitted3[1])
	    checker(va3)

main()
