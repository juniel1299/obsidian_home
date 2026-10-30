from pathlib import Path
from PIL import ImageFont
import json
p=Path(__file__).resolve().parent
cues=[
(0,2.1,'청춘까지 뺏은 현재','青春まで奪った今という時間'),
(2.1,4.35,'탓할 곳은 어디 없네','誰のせいにもできない'),
(4.48,6.42,'Twenty two 세에게 너무 큰 벽','22歳には高すぎる壁'),
(6.42,8.78,'그게 말로 하고 싶어도 어려웠어','言葉にしたくても難しかった'),
(8.78,11.14,'가끔은 어렸을 때로 돌아가','時々、幼い頃に戻りたくなる'),
(11.14,13.22,'불가능하단 건 나도 잘 알아','無理だってことは僕もよく分かってる'),
(13.22,15.02,'그 순간만 고칠 수 있다면','あの瞬間だけやり直せたなら'),
(15.02,17.3,'지금의 나는 더 나았을까','今の僕はもっと良くなっていたかな'),
(17.58,19.3,'달려가는 미터기 돈은 올라가','進むメーター、上がる料金'),
(19.3,21.24,'기사님과 어색하게 눈이 맞아','運転手さんと気まずく目が合う'),
(21.24,22.46,'창문을 열어보지만','窓を開けてみても'),
(22.46,23.66,'기분은 좋아지지 않아','気分は晴れない'),
(23.66,26.52,'그래서 손을 밖으로 쭉 뻗어 쭉 뻗어','だから窓の外へ手を伸ばす、ぐっと伸ばす'),
(26.52,28.68,'흔들리는 택시는 어느새','揺れるタクシーはいつの間にか'),
(28.68,30.94,'목적지에 도달했다고 해','目的地に着いたという'),
(30.94,32.82,'방 하나 있는 내 집 안의','一部屋だけの僕の家の中'),
(32.82,34,'손에 있던 짐들은','手にしていた荷物は'),
(34,36.32,'내가 힘들 때마다','僕がつらい時はいつも'),
(36.32,38.76,'이 노래가 찾아와','この歌がそばに来てくれる'),
(38.76,43.06,'세상이 둥근 것처럼 우리','世界が丸いように、僕らの'),
(43.06,45.4,'인생은 회전목마','人生はメリーゴーランド'),
(45.4,47.84,'우린 계속 달려가','僕らは走り続ける'),
(47.84,51.3,'언제쯤 끝날지 잘 몰라','いつ終わるのかは分からない'),
(51.7,56.6,'빙빙 돌아가는 회전목마처럼','くるくる回るメリーゴーランドのように'),
(57.04,60.2,'영원히 계속될 것처럼','永遠に続いていくかのように'),
(60.6,65.48,'빙빙 돌아올 우리의 시간처럼','巡り巡って戻ってくる僕らの時間のように'),
(65.48,69,'인생은 회전목마','人生はメリーゴーランド')]
def ts(t):
 c=round(t*100);return f'{c//360000}:{c//6000%60:02}:{c//100%60:02}.{c%100:02}'
def st(t):
 m=round(t*1000);return f'{m//3600000:02}:{m//60000%60:02}:{m//1000%60:02},{m%1000:03}'
s=(p/'layout.ass').read_text()
for a,b,k,j in cues:
 for style,text,y,font,size in [('KO',k,1385,'/System/Library/Fonts/AppleSDGothicNeo.ttc',48),('JA',j,1455,'/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc',44)]:
  ft=ImageFont.truetype(font,size);sz=min(size,int(size*900/max(1,ft.getlength(text))))
  s+=f'Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y})\\fs{sz}}}{text}\n'
(p/'layout_with_lyrics.ass').write_text(s)
(p/'lyrics.json').write_text(json.dumps(cues,ensure_ascii=False,indent=2))
(p.parent/'SOKODOMO_Merry_Go_Round_KO_JA.srt').write_text('\n\n'.join(f'{i}\n{st(a)} --> {st(b)}\n{k}\n{j}' for i,(a,b,k,j) in enumerate(cues,1))+'\n')
x=json.loads((p/'sources.json').read_text());x['lyrics']='User supplied Korean lyrics with Japanese translation';(p/'sources.json').write_text(json.dumps(x,ensure_ascii=False,indent=2))
