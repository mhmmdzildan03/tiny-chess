import os,json,urllib.request as U
VV=[0,100,320,330,500,900,0];CE=[0,1,2,3,3,2,1,0]
SQ=[21+i+2*(i//8) for i in range(64)]
KN=[21,19,12,8,-8,-12,-19,-21];D8=[10,-10,1,-1,11,9,-9,-11];RD={28:1,21:2,98:4,91:8}
B=[99]*120;TN=1;CA=0;EP=0;ND=0;TT={};KP=[25,95]
def PF(fen):
 global TN,CA,EP
 for s in SQ:B[s]=0
 pt=fen.split();TN=1-2*(pt[1]=='b');s=91
 for ch in pt[0]:
  if ch=='/':s-=18
  elif ch.isdigit():s+=int(ch)
  else:p="pnbrqk".index(ch.lower())+1;B[s]=p if ch<'a' else -p;s+=1
 CA=0
 for ch in pt[2]:CA|={"K":1,"Q":2,"k":4,"q":8}.get(ch,0)
 EP=0 if pt[3]=='-' else (int(pt[3][1])+1)*10+ord(pt[3][0])-96
def AT(s,by):
 if by in (B[s-9*by],B[s-11*by]):return 1
 for d in KN:
  if B[s+d]==by*2:return 1
 for d in D8:
  if B[s+d]==by*6:return 1
  x=s+d
  while B[x]==0:x+=d
  if B[x] in (by*5,by*(3 if abs(d) in (9,11) else 4)):return 1
 return 0
def GEN(co):
 ms=[]
 for s in SQ:
  p=B[s]
  if not p or p*TN<=0:continue
  t=abs(p);r=s//10-2
  if t==1:
   pr=r==(6 if TN>0 else 1)
   def AD(to):
    if pr:
     for x in (5,4,3,2):ms.append((s,to,x))
    else:ms.append((s,to,0))
   for d in (9*TN,11*TN):
    to=s+d;q=B[to]
    if q!=99 and (q*TN<0 or to==EP):AD(to)
   if co:continue
   if not B[s+10*TN]:
    AD(s+10*TN)
    if r==(1 if TN>0 else 6) and not B[s+20*TN]:ms.append((s,s+20*TN,0))
  else:
   for d in (KN,[11,9,-9,-11],[10,-10,1,-1],D8,D8)[t-2]:
    to=s
    while 1:
     to+=d;q=B[to]
     if q==99 or q*TN>0:break
     if not co or q:ms.append((s,to,0))
     if q or t in (2,6):break
   if t==6 and not co and s%70==25:
    for ds in (2,-2):
     bt=(1 if TN>0 else 4)*(2 if ds<0 else 1);em=(s+1,s+2) if ds>0 else (s-1,s-2,s-3)
     if CA&bt and all(not B[x] for x in em):ms.append((s,s+ds,0))
 return ms
def RF(m):
 f,t=m[0],m[1];return (f+3,f+1) if t>f else (f-4,f-1)
def MK(m):
 global TN,CA,EP
 fr,to,pr=m;p=B[fr];cap=B[to];cs=-1
 if abs(p)==1 and to==EP and not cap and fr%10!=to%10:cs=to-10*TN;cap=B[cs]
 u=(cap,CA,EP,cs);B[fr]=0;B[to]=pr*TN if pr else p
 if cap and cs>=0:B[cs]=0
 if abs(p)==6:
  KP[0 if TN>0 else 1]=to
  if abs(to-fr)==2:
   rf,rt=RF(m);B[rt]=B[rf];B[rf]=0
  CA&=-(4 if TN>0 else 13)
 CA&=~(RD.get(fr,0)|RD.get(to,0))
 EP=fr+10*TN if abs(p)==1 and abs(to-fr)==20 else 0;TN=-TN
 return u
def UN(m,u):
 global TN,CA,EP
 TN=-TN;fr,to,pr=m;cap,CA,EP,cs=u;p=B[to]
 if abs(p)==6:
  KP[0 if TN>0 else 1]=fr
  if abs(to-fr)==2:
   rf,rt=RF(m);B[rf]=B[rt];B[rt]=0
 B[fr]=TN if pr else p;B[to]=0
 if cap:B[cs if cs>=0 else to]=cap
def LG(co):
 o=[]
 for m in GEN(co):
  u=MK(m);bad=AT(KP[0 if TN<0 else 1],TN);UN(m,u)
  if not bad:o.append(m)
 return o
def EV():
 tot=0
 for s in SQ:
  p=B[s]
  if not p:continue
  t=abs(p);v=VV[t];f=s%10-1;r=s//10-2
  if t==1:v+=(r if p>0 else 7-r)*6
  elif t in (2,3):v+=(CE[f]+CE[r])*4
  tot+=v if p>0 else -v
 return tot*TN
def SC(m):return 1e6+VV[abs(B[m[1]])]*10-VV[abs(B[m[0]])] if B[m[1]] else 0
def SE(d,a,b):
 global ND
 ND+=1
 if ND>15e4:return EV()
 if not d:
  a=max(a,EV())
  if a>=b:return a
  ms=LG(1);ms.sort(key=SC,reverse=True)
  for m in ms:
   u=MK(m);v=-SE(0,-b,-a);UN(m,u)
   if v>a:a=v
   if a>=b:break
  return a
 ky=(tuple(B),TN);e=TT.get(ky)
 if e and e[0]>=d:return e[1]
 ms=LG(0)
 if not ms:return -1e5 if AT(KP[0 if TN>0 else 1],-TN) else 0
 if e and e[2] in ms:ms.remove(e[2]);ms.insert(0,e[2])
 best=-1e9
 for m in ms:
  u=MK(m);v=-SE(d-1,-b,-a);UN(m,u)
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=b:break
 TT[ky]=(d,best,bm)
 return best
def M(fen,legal):
 global ND,TT
 PF(fen);TT={};ND=0;fb=None
 for d in range(9):
  SE(d,-1e9,1e9)
  if ND>15e4:break
  e=TT.get((tuple(B),TN))
  if e and e[2]:fb=e[2]
 if fb is None:return legal[0]
 fr,to,pr=fb;u=chr(96+fr%10)+str(fr//10-1)+chr(96+to%10)+str(to//10-1)+("nbrq"[pr-2] if pr else "")
 return u if u in legal else legal[0]
def RQ(pth,body):return json.load(U.urlopen(U.Request(os.getenv("MAKEFUN_ENV_URL","")+pth,data=json.dumps(body).encode())))
while 1:
 try:
  g=RQ("/game",{})
  if g.get("status")=="done":break
  if g.get("status")=="your_move":RQ("/move",{"game":g["game"],"move":M(g["fen"],g["legal_moves"])})
 except Exception:pass
