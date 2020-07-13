import urllib
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup
import sys

url = sys.argv[1]

values = {'username' : 'fakeReziba',
          'password' : '', # Add your password here
          'module' : 'Login'
}

data = urllib.parse.urlencode(values).encode('utf-8')
cookies = CookieJar()

opener = urllib.request.build_opener(
    urllib.request.HTTPRedirectHandler(),
    urllib.request.HTTPHandler(debuglevel=0),
    urllib.request.HTTPSHandler(debuglevel=0),
    urllib.request.HTTPCookieProcessor(cookies))

try:
    response = opener.open(url, data)
except:
    print("====================================================================================")
    print("-------------------------","Network Connection not available","-------------------------")
    print("====================================================================================")
    exit()
contents = response.read()
contents = contents.decode('utf-8')
contents = contents.replace('\n',' ')
soup = BeautifulSoup(contents,"lxml")

links = soup.find_all("td", class_="statText")

input=[]
output=[]

ind=0
for i in range(len(links)):
    line = links[i].text
    if line=="Success":
        ind = i
        break

for i in range(ind+1,len(links)):
    if (i-(ind+1))%3==0:
        tc = links[i].text
        input.append(tc)

for i in range(ind+1,len(links)):
	if (i-(ind+1))%3==1:
		tc = links[i].text
		output.append(tc)

input_file_name = "input.txt"
output_file_name = "output.txt"

file_ip = open(input_file_name,"w")
file_op = open(output_file_name,"w")

for e in input:
    file_ip.write(e)
    file_ip.write('\n')

for e in output:
    file_op.write(e)
    file_op.write('\n')

print("===================================================================================================")
print("-------------------------","input.txt and output.txt successfully generated","-------------------------")
print("===================================================================================================")
