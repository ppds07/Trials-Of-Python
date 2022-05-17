import requests as req

resp = "https://fast.com/"

a = req.head(resp)

ans = "LAST MODIFIED" + a.headers['last-modified']

print(ans)