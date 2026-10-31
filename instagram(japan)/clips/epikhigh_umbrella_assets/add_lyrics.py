from pathlib import Path
from PIL import ImageFont
import json
p=Path(__file__).resolve().parent
cues=[(0,3.46,'그대는 내 머리 위에 우산','あなたは私の頭上を覆う傘'),(3.46,7.48,'어깨 위에 차가운 비 내리는 밤','肩に冷たい雨が降る夜'),(7.48,12.18,'내 곁에 그대가 습관이 돼버린 나','隣にいるあなたが当たり前になった私'),(12.18,15.16,'난 그대 없이는 안돼요','私はあなたなしではいられない'),(15.16,17.28,'I need you back in my life','もう一度、私の人生に戻ってきて'),(17.28,20.62,'그대는 내 머리 위에 우산','あなたは私の頭上を覆う傘'),(20.62,24.44,'어깨 위에 차가운 비 내리는 밤','肩に冷たい雨が降る夜'),(24.44,28.98,'내 곁에 그대가 없는 반쪽의 세상','あなたが隣にいない、半分だけの世界'),(28.98,33.1,'그댄 나 없이는 안돼요','あなたは私なしではいられない'),(33.78,37,'Forever in the rain','永遠に雨の中で')]
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
(p.parent/'EPIK_HIGH_Umbrella_KO_JA.srt').write_text('\n\n'.join(f'{i}\n{st(a)} --> {st(b)}\n{k}\n{j}' for i,(a,b,k,j) in enumerate(cues,1))+'\n')
x=json.loads((p/'sources_and_license.json').read_text());x['lyrics']='User supplied original lyrics and Japanese translation burned in';(p/'sources_and_license.json').write_text(json.dumps(x,ensure_ascii=False,indent=2))
