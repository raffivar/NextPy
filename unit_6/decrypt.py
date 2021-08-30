import base64

item = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW" \
       "1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS" \
       "58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICA" \
       "gIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAg" \
       "ICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgI" \
       "CAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgIC" \
       "AgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB" \
       "8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19f" \
       "X19fX19fX3wvCgo="

item_utf8 = item.encode(encoding='utf-8', errors='strict')
secret = base64.decodebytes(item_utf8).decode()
print(secret)
