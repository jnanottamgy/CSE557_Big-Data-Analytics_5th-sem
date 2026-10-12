import re
B='/tmp/claude-0/-home-user-CSE557-Big-Data-Analytics-5th-sem/c9da8b5d-4313-5c3c-b92d-68621bf949fb/scratchpad'
def grab(path, cap, pfx):
    s=open(path,encoding='utf-8').read()
    i=s.index(cap)
    a=s.rindex('<svg',0,i); b=s.index('</svg>',a)+6
    svg=s[a:b]
    svg=re.sub(r'id="([\w-]+)"',lambda m:'id="%s%s"'%(pfx,m.group(1)),svg)
    svg=re.sub(r'url\(#([\w-]+)\)',lambda m:'url(#%s%s)'%(pfx,m.group(1)),svg)
    svg=re.sub(r'\swidth="\d+"','',svg,count=1)
    return svg
items=[
 ('u1',B+'/build/02_ch1.html','Figure 1.1 — The three types','Unit 1 · Classification of digital data','U1 §1.2','62mm'),
 ('u1',B+'/build/05_ch3b.html','Figure 3.13 — Three multiprocessor','Unit 1 · Shared memory / shared disk / shared nothing','U1 §3.8','52mm'),
 ('u1',B+'/build/05_ch3b.html','Figure 3.14 — Databases and CAP','Unit 1 · CAP theorem with databases','U1 §3.9','70mm'),
 ('u1',B+'/build/04_ch3a.html','Figure 3.5 — Analytics 1.0','Unit 1 · Analytics: hindsight → insight → foresight','U1 §3.3','55mm'),
 ('u2',B+'/u2/build/02_ch1.html','Figure 1.8 — MapReduce logical','Unit 2 · MapReduce logical data flow (max temperature)','U2 §1.5','50mm'),
 ('u2',B+'/u2/build/02_ch1.html','Figure 1.11 — MapReduce data flow with multiple','Unit 2 · Data flow with multiple reducers','U2 §1.7','62mm'),
 ('u2',B+'/u2/build/03_ch2.html','Figure 2.3 — HDFS architecture','Unit 2 · HDFS architecture','U2 §2.4','68mm'),
 ('u2',B+'/u2/build/03_ch2.html','Figure 2.7 — A client reading','Unit 2 · Anatomy of a file read (steps 1–6)','U2 §2.7','78mm'),
 ('u2',B+'/u2/build/03_ch2.html','Figure 2.8 — A client writing','Unit 2 · Anatomy of a file write (steps 1–7)','U2 §2.8','80mm'),
 ('u2',B+'/u2/build/04_ch3a.html','Figure 3.2 — How Hadoop runs a MapReduce job using the classic','Unit 2 · Job run in classic MapReduce (MR1, steps 1–10)','U2 §3.4','98mm'),
 ('u2',B+'/u2/build/04_ch3a.html','Figure 3.4 — How Hadoop runs a MapReduce job using YARN','Unit 2 · Job run on YARN (steps 1–11)','U2 §3.5','102mm'),
 ('u2',B+'/u2/build/05_ch3b.html','Figure 3.7 — Shuffle and sort','Unit 2 · Shuffle and sort','U2 §3.8','72mm'),
 ('u3',B+'/u3/build/02_ch1.html','Figure 1.4 — Apache Spark architecture','Unit 3 · Spark architecture','U3 §1.5','84mm'),
 ('u3',B+'/u3/build/02_ch1.html','Figure 1.2 — The Spark stack','Unit 3 · Spark components (stack)','U3 §1.2','62mm'),
 ('u3',B+'/u3/build/02_ch1.html','Figure 1.5 — Internals of job execution','Unit 3 · Internals of job execution','U3 §1.6','98mm'),
]
out=['\n<!-- ============ DIAGRAM GALLERY ============ -->\n<section class="nv pb gal">\n<div class="band" style="background:#16244a"><b>Must-draw diagrams</b><span>Look → cover → redraw from memory → check. Numbered arrows = exam steps.</span></div>\n']
for n,(u,p,cap,title,ref,mh) in enumerate(items,1):
    svg=grab(p,cap,'g%d_'%n).replace('<svg','<svg style="max-height:%s;width:auto;max-width:100%%"'%mh,1)
    out.append('<div class="avoid %s"><h3>%d. %s <span class="small" style="color:#5b6478;font-weight:400">(%s)</span></h3><div class="fig">%s</div></div>\n'%(u,n,title,ref,svg))
out.append('</section>\n')
open(B+'/rev/05_gallery.html','w',encoding='utf-8').write(''.join(out))
print('ok',len(items))
