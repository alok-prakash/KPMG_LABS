import requests
requests.get("http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance").json()


alldata = requests.get("http://169.254.169.254/latest/meta-data/").text
datalist = alldata.split('\n')
for data in datalist:
     if requests.get(url+"/"+data).code == 200:
        print(requests.get(url+"/"+data).json)


