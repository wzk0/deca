import os
import json

ls=os.listdir('songs')
ls.remove('list.json')
path=[]
os.chdir('songs')
for l in ls:
	for ll in os.listdir(l):
		if ll!='cover.png':
			path.append({'name':ll.replace('.mp3',''),'al':l,'url':'https://ghproxy.com/https://raw.githubusercontent.com/wzk0/deca/main/songs/%s/%s'%(l,ll),'cover':'https://ghproxy.com/https://raw.githubusercontent.com/wzk0/deca/main/songs/%s/cover.png'%l})
with open('list.json','w')as f:
	f.write(json.dumps(path,ensure_ascii=False))