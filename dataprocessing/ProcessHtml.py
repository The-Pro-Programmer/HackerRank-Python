from pprint import pprint
from urllib.request import urlopen


url = "https://securitysaints.com/"
with urlopen(url) as response:
    pprint(dir(response))

