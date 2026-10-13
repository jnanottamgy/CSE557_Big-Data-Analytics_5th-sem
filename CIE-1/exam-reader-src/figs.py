"""Expand {{fig:key|caption}} placeholders with SVG diagrams taken from the unit guides."""
import re, os

B = '/tmp/claude-0/-home-user-CSE557-Big-Data-Analytics-5th-sem/c9da8b5d-4313-5c3c-b92d-68621bf949fb/scratchpad'
U1, U2, U3 = B + '/build', B + '/u2/build', B + '/u3/build'

# key: (file, anchor text) — anchor is a figure caption (svg just before it) or text inside the svg
REG = {
 # Unit 1
 'u1_dtypes':   (U1 + '/02_ch1.html', 'Types of Data</text>'),
 'u1_three':    (U1 + '/02_ch1.html', 'Figure 1.1 — The three types'),
 'u1_tables':   (U1 + '/02_ch1.html', 'Figure 1.2 — Tables in an RDBMS'),
 'u1_unstr':    (U1 + '/02_ch1.html', 'Figure 1.3 — Forms/sources'),
 'u1_tech':     (U1 + '/02_ch1.html', 'Figure 1.4 — Techniques'),
 'u1_3c':       (U1 + '/03_ch2.html', 'Figure 2.1 — Characteristics of data'),
 'u1_evol':     (U1 + '/03_ch2.html', 'Figure 2.2 — Evolution'),
 'u1_chall':    (U1 + '/03_ch2.html', 'Figure 2.3 — Challenges'),
 'u1_3v':       (U1 + '/03_ch2.html', 'Figure 2.4 — Data: big in volume'),
 'u1_sources':  (U1 + '/03_ch2.html', 'Figure 2.5 — Sources of Big Data'),
 'u1_scale':    (U1 + '/03_ch2.html', 'Figure 2.6 — Scale up'),
 'u1_pyramid':  (U1 + '/04_ch3a.html', 'Figure 3.1 — Transformation of data'),
 'u1_where':    (U1 + '/04_ch3a.html', 'Figure 3.2 — Types of data available'),
 'u1_bda':      (U1 + '/04_ch3a.html', 'Figure 3.3 — What is Big Data Analytics'),
 'u1_movecode': (U1 + '/04_ch3a.html', 'Figure 3.4 — "Moving code to data"'),
 'u1_stairs':   (U1 + '/04_ch3a.html', 'Figure 3.5 — Analytics 1.0'),
 'u1_4appr':    (U1 + '/04_ch3a.html', 'Figure 3.6 — Four approaches'),
 'u1_venn':     (U1 + '/05_ch3b.html', 'Figure 3.7 — The data scientist sits'),
 'u1_ds':       (U1 + '/05_ch3b.html', 'Figure 3.8 — Data scientist'),
 'u1_inmem':    (U1 + '/05_ch3b.html', 'Traditional: data repeatedly fetched from disk</text>'),
 'u1_smp':      (U1 + '/05_ch3b.html', 'Figure 3.9 — Symmetric'),
 'u1_mpp':      (U1 + '/05_ch3b.html', 'Figure 3.10 — Massively'),
 'u1_par':      (U1 + '/05_ch3b.html', 'Figure 3.11 — Parallel system'),
 'u1_dist':     (U1 + '/05_ch3b.html', 'Figure 3.12 — Distributed system'),
 'u1_snsd':     (U1 + '/05_ch3b.html', 'Figure 3.13 — Three multiprocessor'),
 'u1_cap':      (U1 + '/05_ch3b.html', 'Figure 3.14 — Databases and CAP'),
 'u1_capstory': (U1 + '/05_ch3b.html', 'Figure 3.15 — Scenario'),
 # Unit 2
 'u2_disk':     (U2 + '/02_ch1.html', 'Figure 1.1 — Disk capacity'),
 'u2_par':      (U2 + '/02_ch1.html', 'Figure 1.2 — Parallel reading'),
 'u2_comp':     (U2 + '/02_ch1.html', 'Figure 1.3 — Core components'),
 'u2_hist':     (U2 + '/02_ch1.html', 'Figure 1.4 — The journey'),
 'u2_eco':      (U2 + '/02_ch1.html', 'Figure 1.5 — The Hadoop ecosystem'),
 'u2_letters':  (U2 + '/02_ch1.html', 'Figure 1.6 — MapReduce counting'),
 'u2_record':   (U2 + '/02_ch1.html', 'Figure 1.7 — A weather record'),
 'u2_flow':     (U2 + '/02_ch1.html', 'Figure 1.8 — MapReduce logical'),
 'u2_local':    (U2 + '/02_ch1.html', 'Figure 1.9 — (a) data-local'),
 'u2_single':   (U2 + '/02_ch1.html', 'Figure 1.10 — MapReduce data flow with a single'),
 'u2_multi':    (U2 + '/02_ch1.html', 'Figure 1.11 — MapReduce data flow with multiple'),
 'u2_dfs':      (U2 + '/03_ch2.html', 'Figure 2.1 — A distributed file system'),
 'u2_blocks':   (U2 + '/03_ch2.html', 'Figure 2.2 — A 500 MB file'),
 'u2_arch':     (U2 + '/03_ch2.html', 'Figure 2.3 — HDFS architecture'),
 'u2_snn':      (U2 + '/03_ch2.html', 'Figure 2.4 — The Secondary NameNode'),
 'u2_fed':      (U2 + '/03_ch2.html', 'Figure 2.5 — HDFS Federation'),
 'u2_ha':       (U2 + '/03_ch2.html', 'Figure 2.6 — HDFS High Availability'),
 'u2_read':     (U2 + '/03_ch2.html', 'Figure 2.7 — A client reading'),
 'u2_write':    (U2 + '/03_ch2.html', 'Figure 2.8 — A client writing'),
 'u2_jobs':     (U2 + '/04_ch3a.html', 'Figure 3.1 — Key idea'),
 'u2_mr1':      (U2 + '/04_ch3a.html', 'Figure 3.2 — How Hadoop runs a MapReduce job using the classic'),
 'u2_yarnsplit':(U2 + '/04_ch3a.html', 'Figure 3.3 — YARN splits'),
 'u2_yarn':     (U2 + '/04_ch3a.html', 'Figure 3.4 — How Hadoop runs a MapReduce job using YARN'),
 'u2_fail':     (U2 + '/05_ch3b.html', 'Figure 3.5 — Failure detection'),
 'u2_sched':    (U2 + '/05_ch3b.html', 'Figure 3.6 — FIFO vs Fair'),
 'u2_shuffle':  (U2 + '/05_ch3b.html', 'Figure 3.7 — Shuffle and sort'),
 # Unit 3
 'u3_vsmr':     (U3 + '/02_ch1.html', 'Figure 1.1 — Why Spark is faster'),
 'u3_stack':    (U3 + '/02_ch1.html', 'Figure 1.2 — The Spark stack'),
 'u3_jst':      (U3 + '/02_ch1.html', 'Figure 1.3 — An action creates a job'),
 'u3_arch':     (U3 + '/02_ch1.html', 'Figure 1.4 — Apache Spark architecture'),
 'u3_exec':     (U3 + '/02_ch1.html', 'Figure 1.5 — Internals of job execution'),
 'u3_runtime':  (U3 + '/02_ch1.html', 'Figure 1.6 — Run-time flow'),
 'u3_cm':       (U3 + '/03_ch2.html', 'Figure 2.1 — Cluster manager types'),
 'u3_mode':     (U3 + '/03_ch2.html', 'Figure 2.2 — Client vs cluster'),
}

_cache = {}
def _read(p):
    if p not in _cache:
        _cache[p] = open(p, encoding='utf-8').read()
    return _cache[p]

def svg(key, n):
    path, anchor = REG[key]
    s = _read(path)
    i = s.index(anchor)
    a = s.rindex('<svg', 0, i)
    b = s.index('</svg>', a) + 6
    if b < i:  # anchor is a caption after the svg; fine. If anchor inside svg, b > i anyway
        pass
    out = s[a:b]
    pfx = 'f%d_' % n
    out = re.sub(r'id="([\w-]+)"', lambda m: 'id="%s%s"' % (pfx, m.group(1)), out)
    out = re.sub(r'url\(#([\w-]+)\)', lambda m: 'url(#%s%s)' % (pfx, m.group(1)), out)
    out = re.sub(r'(<svg[^>]*?)\sstyle="[^"]*"', r'\1', out, count=1)
    return out

def expand(html):
    n = [0]
    def rep(m):
        n[0] += 1
        key, cap = m.group(1), m.group(2)
        return ('<div class="fig">%s<div class="cap">Figure %d — %s</div></div>'
                % (svg(key, n[0]), n[0], cap))
    return re.sub(r'\{\{fig:([\w]+)\|([^}]*)\}\}', rep, html)

if __name__ == '__main__':
    for i, k in enumerate(REG, 1):
        s = svg(k, i)
        print(k, len(s), s[:60].replace('\n', ' '))
