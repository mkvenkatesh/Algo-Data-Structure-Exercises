'''
HTML Tag Checker

Write a program that can check an HTML document for proper opening and closing
tags.

 <html>
     <head>
        <title>
          Example
        </title>
     </head>
     <body>
        <h1>Hello, world</h1>
     </body>
   </html>

'''

from stack import Stack

def html_tag_check(html):
    s = Stack()
    i = 0

    while i < len(html):       
        # get tags
        tag = ""
        if html[i] == "<":
            tag += html[i]
            i += 1
            while i < len(html):
                if not html[i].isspace():
                    tag += html[i]
                if html[i] == ">":
                    break
                i += 1
            if not tag.endswith(">"):
                print("Error: HTML syntax is incorrect. '>' not found for an opening '<'.")
        
            # closing tag
            if tag.startswith("</"):
                if tag.replace("</", "<", 1) == s.peek():
                    s.pop()
            # opening tag
            else:
                s.push(tag)

        i+= 1

    if s.is_empty():
        print("Success: HTML tags are balanced.")
    else:
        print("Error: HTML tags are not balanced. Unmatched tags are listed below.")
        print(s)


# driver code
if __name__ == "__main__":
    html = """
        <html>
        <head>
            <title>
            Example
            </title>
        </head>
        <body>
            <h1>Hello, world</h1>
        </body>
        </html>
    """
    html_tag_check(html)