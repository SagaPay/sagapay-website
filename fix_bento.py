with open('om-oss.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('background: #F6F9FC;"', 'background: linear-gradient(135deg, #0A2540 0%, #0044FF 100%);"')

with open('om-oss.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("done bento")
