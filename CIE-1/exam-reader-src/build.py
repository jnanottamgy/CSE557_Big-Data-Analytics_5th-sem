import glob, re, subprocess, sys, os
from pypdf import PdfReader
here=os.path.dirname(os.path.abspath(__file__))
parts=sorted(glob.glob(os.path.join(here,'[0-9][0-9]_*.html')))
html=''.join(open(p,encoding='utf-8').read() for p in parts)
import sys as _s; _s.path.insert(0,here)
import figs; html=figs.expand(html)
if '</body>' not in html: html+='\n</body></html>'
out=sys.argv[1] if len(sys.argv)>1 else os.path.join(here,'guide.pdf')
NODE_PATH=subprocess.run(['npm','root','-g'],capture_output=True,text=True).stdout.strip()
env=dict(os.environ, PW=os.path.join(NODE_PATH,'playwright'))
def render(h, pdf):
    f=os.path.join(here,'_guide.html'); open(f,'w',encoding='utf-8').write(h)
    subprocess.run(['node',os.path.join(here,'render.js'),f,pdf],check=True,env=env)
# pass 1: find page numbers of markers
tmp=os.path.join(here,'_pass1.pdf')
render(html.replace('{{pg:','{{PG:'), tmp)
pages={}
n=len(PdfReader(tmp).pages)
for i in range(1,n+1):
    t=subprocess.run(['pdftotext','-f',str(i),'-l',str(i),tmp,'-'],capture_output=True,text=True).stdout
    for m in re.findall(r'@@([\w-]+)@@',t):
        pages.setdefault(m,i)
def sub(m): return str(pages.get(m.group(1),'?'))
html2=re.sub(r'\{\{pg:([\w-]+)\}\}',sub,html)
render(html2,out)
missing=[k for k in re.findall(r'\{\{pg:([\w-]+)\}\}',html) if k not in pages]
print('pages:',len(PdfReader(out).pages),'missing markers:',missing)
