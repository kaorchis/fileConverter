import sys
import markdown

if sys.argv[1] != 'markdown':
    sys.exit(1)

with open(sys.argv[2]) as f:
    contents = f.read()

html = markdown.markdown(contents)

with open(sys.argv[3],'w') as f:
    f.write(html)
