from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print(data)
    def handle_comment(self, data):
        noOfLine = len(data.split('\n'))
        if noOfLine > 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)

  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
