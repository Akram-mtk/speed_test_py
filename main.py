# pip install speedtest-cli

import speedtest as st

s = st.Speedtest()

ds = s.download()
print(ds/2**20)
us = s.upload()
print(us/2**20)
p = s.results.ping
print(p)
