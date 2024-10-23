text = open('text.txt').read()

split_text = text.split()

html = ""

google = "https://www.google.com/search?q="

def gen_link(keyword):
    return google + keyword

for word in split_text:
    html += (f"<a href='{gen_link(word)}' target='_blank'>{word}</a>")

with open("index.html", "w") as file:
    file.write(html)