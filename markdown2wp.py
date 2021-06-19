import markdown

print("はじめるよ")

text='''こんにちはあ'''

md = markdown.Markdown()
html = md.convert(text)
print(html)
