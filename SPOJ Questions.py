import urllib.request
import requests
user=input("Enter Username")
url='https://www.spoj.com/users/'+str(user)
response=urllib.request.urlopen(url)
src_code=str(response.read())
plain_text=src_code
temp=plain_text.index('Problems solved</dt>\\n\\t\\t\\t\\t\\t\\t\\t\\t<dd>')
plain_text=plain_text[temp:]
temp=plain_text.index('\\n\\t\\t\\t\\t\\t\\t\\t\\t<dd>')
plain_text=plain_text[temp:]
temp=plain_text.index('>')
ans=plain_text[temp+1:]
temp=ans.index('</dd>')
ans=ans[:temp]
print("Problems Solved by",user,"are",ans)

