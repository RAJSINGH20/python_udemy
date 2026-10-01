import json
from urllib.request import Request, urlopen

userinput = input("enter the Query :")

request = Request(
	"http://localhost:11434/api/chat",
	data=json.dumps({
		"model": "gemma4:26b",
		"messages": [{"role": "user", "content": userinput}],
		"stream": False,
	}).encode("utf-8"),
	headers={"Content-Type": "application/json"},
	method="POST",
)

with urlopen(request) as response:
	result = json.load(response)

print(result["message"]["content"])