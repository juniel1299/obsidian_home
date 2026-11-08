from pathlib import Path

def stamp(s,scale):
    v,r=divmod(round(float(s)*scale),scale)
    if scale==1000:
        return f'00:{v//60:02}:{v%60:02},{r:03}'
    return f'0:{v//60:02}:{v%60:02}.{r:02}'

ass=Path('layout.ass').read_text()
srt=[]
for i,line in enumerate(Path('cues.tsv').read_text().splitlines(),1):
    a,b,ko,ja=line.split('\t')
    for style,y,word in [('KO',1385,ko),('JA',1455,ja)]:
        ass+=f'Dialogue: 0,{stamp(a,100)},{stamp(b,100)},{style},,0,0,0,,{{\\pos(540,{y})}}{word}\n'
    srt.append(f'{i}\n{stamp(a,1000)} --> {stamp(b,1000)}\n{ko}\n{ja}\n')
Path('sub.ass').write_text(ass)
Path('../Park_Bom_You_And_I_KO_JA.srt').write_text('\n'.join(srt))
