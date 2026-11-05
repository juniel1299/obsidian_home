from pathlib import Path
from PIL import ImageFont
import json
p=Path(__file__).resolve().parent
cues=[(0,4.58,'미친척하고 널 잡아 볼래도','どうかしたふりで君を引き止めようとしても'),(4.58,9.66,'내 몸이 내 말을 잘 듣지를 않아','体が言うことを聞いてくれない'),(9.66,15.38,'차안에 남은 니 향기에 취해','車に残る君の香りに酔って'),(15.38,22,'영영 깨고 싶지 않은걸','永遠に醒めたくないんだ'),(24.32,27.24,'이러지마 제발 (제발)','お願い、こんなことしないで（お願い）'),(27.24,30,'떠나지마 제발 (제발)','行かないで、お願い（お願い）'),(30,33.24,'돌아와 (돌아와)','戻ってきて（戻ってきて）'),(33.24,36.04,'돌아와','戻ってきて'),(36.04,40.44,'니가 떠나간 빈자리 위엔','君が去った空席には'),(40.44,44.66,'차가운 향기만 남아','冷たい香りだけが残る'),(44.66,47.14,'이러지마 제발','お願い、こんなことしないで'),(47.14,50,'떠나지마 제발','行かないで、お願い'),(50,52.92,'돌아와 (돌아와)','戻ってきて（戻ってきて）'),(52.92,55.76,'돌아와 (돌아와)','戻ってきて（戻ってきて）'),(55.76,60.46,'남은 향기만 안고 있을게','残った香りだけを抱きしめているから'),(60.46,65,'돌아와 니 자리로','戻ってきて、君のいた場所へ')]
def ts(t):
 c=round(t*100);return f'{c//360000}:{c//6000%60:02}:{c//100%60:02}.{c%100:02}'
def st(t):
 m=round(t*1000);return f'{m//3600000:02}:{m//60000%60:02}:{m//1000%60:02},{m%1000:03}'
s=(p/'layout.ass').read_text()
for a,b,k,j in cues:
 for style,text,y,font,size in [('KO',k,1385,'/System/Library/Fonts/AppleSDGothicNeo.ttc',48),('JA',j,1455,'/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc',44)]:
  ft=ImageFont.truetype(font,size);sz=min(size,int(size*900/max(1,ft.getlength(text))))
  s+=f'Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y})\\fs{sz}}}{text}\n'
(p/'layout_with_lyrics.ass').write_text(s);(p/'lyrics.json').write_text(json.dumps(cues,ensure_ascii=False,indent=2))
(p.parent/'KWILL_Please_Dont_KO_JA.srt').write_text('\n\n'.join(f'{i}\n{st(a)} --> {st(b)}\n{k}\n{j}' for i,(a,b,k,j) in enumerate(cues,1))+'\n')
