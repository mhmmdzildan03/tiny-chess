import os,json,random,urllib.request as U
_r=random.Random(7);Z=[_r.getrandbits(64)for _ in range(1560)];ZS=Z[1559]
VV=[0,100,320,330,500,900,0];CE=[0,1,2,3,3,2,1,0];PW=[0,0,1,1,2,4,0]
SQ=[21+i+2*(i//8)for i in range(64)];KN=[21,19,12,8,-8,-12,-19,-21];D4=[10,-10,1,-1];DG=[11,9,-9,-11];D8=D4+DG;DR=(KN,DG,D4,D8,D8)
B=[99]*120;TT={}
def PF(fen):
 global TN,CA,HK,PH
 for s in SQ:B[s]=0
 pt=fen.split();TN=1-2*(pt[1]=='b');s=91;HK=ZS*(TN<0);PH=0
 for ch in pt[0]:
  if ch=='/':s-=18
  elif ch.isdigit():s+=int(ch)
  else:p="pnbrqk".index(ch.lower())+1;B[s]=p if ch<'a' else -p;HK^=Z[(B[s]+6)*120+s];PH+=PW[p];s+=1
 CA=sum({"K":1,"Q":2,"k":4,"q":8}.get(ch,0)for ch in pt[2])
def AT(s,by):
 if by in(B[s-9*by],B[s-11*by]):return 1
 for d in KN:
  if B[s+d]==by*2:return 1
 for d in D8:
  if B[s+d]==by*6:return 1
  x=s+d
  while not B[x]:x+=d
  if B[x]in(by*5,by*(3 if abs(d)in(9,11)else 4)):return 1
 return 0
def GEN(co):
 ms=[]
 for s in SQ:
  p=B[s]
  if p*TN<=0:continue
  t=abs(p);r=s//10-2
  if t==1:
   pr=r==(6 if TN>0 else 1);tg=[s+d for d in(9*TN,11*TN)if B[s+d]!=99 and B[s+d]*TN<0]
   if not co and not B[s+10*TN]:
    tg.append(s+10*TN)
    if r==(1 if TN>0 else 6)and not B[s+20*TN]:ms.append((s,s+20*TN,0))
   for to in tg:ms.append((s,to,5 if pr else 0))
  else:
   for d in DR[t-2]:
    to=s
    while 1:
     to+=d;q=B[to]
     if q==99 or q*TN>0:break
     if not co or q:ms.append((s,to,0))
     if q or t in(2,6):break
   if t==6 and not co and s%70==25:
    for ds in(2,-2):
     bt=(1 if TN>0 else 4)<<(ds<0);em=(s+1,s+2)if ds>0 else(s-1,s-2,s-3)
     if CA&bt and B[s+3 if ds>0 else s-4]==4*TN and all(not B[x]for x in em):ms.append((s,s+ds,0))
 return ms
def MK(m):
 global TN,CA,HK,PH
 fr,to,pr=m;p=B[fr];cap=B[to]
 u=(cap,CA,HK,PH);HK^=ZS^Z[(p+6)*120+fr];B[fr]=0;np=pr*TN if pr else p;B[to]=np;HK^=Z[(np+6)*120+to]
 if cap:HK^=Z[(cap+6)*120+to];PH-=PW[abs(cap)]
 if pr:PH+=4
 if abs(p)==6:
  if abs(to-fr)==2:
   rf,rt=(to+1,fr+1)if to>fr else(to-2,fr-1);rp=B[rf];B[rt]=rp;B[rf]=0;HK^=Z[(rp+6)*120+rt]^Z[(rp+6)*120+rf]
  CA&=-(4 if TN>0 else 13)
 TN=-TN
 return u
def UN(m,u):
 global TN,CA,HK,PH
 TN=-TN;fr,to,pr=m;cap,CA,HK,PH=u;p=B[to]
 if abs(p)==6 and abs(to-fr)==2:
  rf,rt=(to+1,fr+1)if to>fr else(to-2,fr-1);B[rf]=B[rt];B[rt]=0
 B[fr]=TN if pr else p;B[to]=0
 if cap:B[to]=cap
E=os.getenv("MAKEFUN_ENV_URL")
def EV():
 G=24-PH;tot=0
 for s in SQ:
  p=B[s]
  if not p:continue
  t=abs(p);f=s%10-1;r=s//10-2;rr=r if p>0 else 7-r;c=CE[f]+CE[r];v=VV[t]
  if t==1:v+=rr*rr*(16+G)>>4
  elif t in(2,3):v+=c*(5-(t==3))
  elif t==4:v+=30*(rr==6)
  elif t==6:v+=c*(G-12)>>1
  tot+=v if p>0 else -v
 return tot*TN
def SC(m):return VV[abs(B[m[1]])]*9-VV[abs(B[m[0]])]
def SE(d,a,b,p):
 global ND
 ND+=1
 if ND>2e5:return EV()
 ks=B.index(6*TN)
 if AT(ks,-TN):d+=1
 if not d:
  a=max(a,EV())
  if a>=b:return a
  ms=GEN(1);ms.sort(key=SC,reverse=True)
  for m in ms:
   u=MK(m)
   if AT(m[1]if abs(B[m[1]])==6 else ks,TN):UN(m,u);continue
   v=-SE(0,-b,-a,p+1);UN(m,u)
   if v>a:a=v
   if a>=b:break
  return a
 e=TT.get(HK);tm=e[3]if e else None
 if e and e[0]>=d and(e[1]==0 or(e[2]>=b if e[1]==1 else e[2]<=a)):return e[2]
 ms=GEN(0);ms.sort(key=lambda m:SC(m)+(m==tm)*1e7,reverse=True)
 a0=a;best=-1e9;ln=0
 for m in ms:
  u=MK(m)
  if AT(m[1]if abs(B[m[1]])==6 else ks,TN):UN(m,u);continue
  ln+=1;v=-SE(d-1,-b,-a,p+1);UN(m,u)
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=b:break
 if not ln:return-100000+p if AT(ks,-TN)else 0
 if ND<2e5:TT[HK]=(d,2 if best<=a0 else 1 if best>=b else 0,best,bm)
 return best
def M(fen,legal):
 global ND
 PF(fen);ND=0;fb=None
 for d in range(9):
  SE(d,-1e9,1e9,0)
  if ND>2e5:break
  fb=TT.get(HK,[0,0,0,fb])[3]
 if not fb:return legal[0]
 fr,to,pr=fb;u=chr(96+fr%10)+str(fr//10-1)+chr(96+to%10)+str(to//10-1)+("q"if pr else"")
 return u if u in legal else legal[0]
while 1:
 try:
  g=json.load(U.urlopen(U.Request(E+"/game",data=b"{}")));s=g.get("status")
  if s=="done":break
  if s=="your_move":U.urlopen(U.Request(E+"/move",data=json.dumps({"game":g["game"],"move":M(g["fen"],g["legal_moves"])}).encode()))
 except Exception:pass
