import json,os,sys,urllib.request as U
E=os.environ["MAKEFUN_ENV_URL"]
def P(p,d):return json.load(U.urlopen(U.Request(E+p,json.dumps(d).encode(),{"content-type":"application/json"})))
V=[0,100,320,330,500,900,0]
K=(-11,-10,-9,-1,1,9,10,11)
D=[0,0,(-21,-19,-12,-8,8,12,19,21),(-11,-9,9,11),(-10,-1,1,10),K,K]
def q(p,i,w):
 r,f=divmod(i-21,10);c=7-abs(2*f-7)-abs(2*r-7);a=(6-r)if w else(r-1)
 if p==1:return a*a*3+a*4+(c if a>2 else 0)
 if p in(2,3):return c*5
 if p==4:return 12 if r==(1 if w else 8)else c
 if p==5:return c*2
 return 0
T={c:[(1 if c>0 else-1)*(V[abs(c)]+q(abs(c),i,c>0))for i in range(120)]for c in range(-6,7)if c}
import random
R=random.Random(7);Z=[[R.getrandbits(64)for i in range(120)]for p in range(13)];ZS=R.getrandbits(64);TT={}
def G(b,s,o):
 for i in range(21,99):
  p=b[i]*s
  if 0<p<7:
   if p==1:
    d=-10*s;j=i+d
    for k in(j-1,j+1):
     if b[k]!=9 and b[k]*s<0:yield i,k,j//10 in(2,9)
    if o==0 and b[j]==0:
     yield i,j,j//10 in(2,9)
     if i//10==(8 if s>0 else 3)and b[j+d]==0:yield i,j+d,0
   else:
    for d in D[p]:
     j=i
     while 1:
      j+=d;c=b[j]
      if c==9 or c*s>0:break
      if c*s<0 or o==0:yield i,j,0
      if c or p in(2,6):break
def A(b,s):
 if 6*s not in b:return 1
 k=b.index(6*s)
 return any(j==k for i,j,p in G(b,-s,1))
class X(Exception):0
N=L=0
def S(b,s,sc,d,a,be,ply,h):
 global N
 N+=1
 if N>L:raise X
 a0=a;bm2=None;tm=(-1,-1);e=TT.get(h)if d>0 else None
 if e and ply:
  tm=e[3]
  if e[0]>=d:
   if e[2]==0:return e[1]
   if e[2]==1:a=max(a,e[1])
   else:be=min(be,e[1])
   if a>=be:return e[1]
 best=-30000
 if d<=0:
  best=s*sc
  if best>=be:return best
  a=max(a,best)
 for i,j,pr in sorted(G(b,s,d<=0),key=lambda m:(m[0]==tm[0] and m[1]==tm[1])*1000+abs(b[m[1]])*10-abs(b[m[0]]),reverse=True):
  c=b[j]
  if abs(c)==6:return 20000-ply
  p=b[i];n=5*s if pr else p
  v=-S2(b,i,j,p,n,c,s,sc,d,a,be,ply,h)
  if v>best:best=v;bm2=(i,j)
  if v>a:a=v
  if a>=be:break
 if d>0 and best==-30000:return(-20000+ply)if A(b,s)else 0
 if d>0:TT[h]=(d,best,0 if a0<best<be else 1 if best>=be else 2,bm2)
 return best
def S2(b,i,j,p,n,c,s,sc,d,a,be,ply,h):
 b[i]=0;b[j]=n
 v=S(b,-s,sc-T[p][i]+T[n][j]-(T[c][j]if c else 0),d-1,-be,-a,ply+1,h^Z[p+6][i]^Z[n+6][j]^(Z[c+6][j]if c else 0)^ZS)
 b[i]=p;b[j]=c
 return v
def M(fen,legal):
 global N,L
 f=fen.split();b=[9]*120
 for r,w in enumerate(f[0].split("/")):
  k=21+r*10
  for ch in w:
   if ch.isdigit():
    for _ in range(int(ch)):b[k]=0;k+=1
   else:b[k]=("pnbrqk".index(ch.lower())+1)*(1 if ch.isupper()else-1);k+=1
 s=1 if f[1]=="w"else-1
 sc=sum(T[b[i]][i]for i in range(21,99)if b[i]and b[i]!=9)
 R=[]
 for u in legal:
  i=21+(8-int(u[1]))*10+ord(u[0])-97;j=21+(8-int(u[3]))*10+ord(u[2])-97
  R.append([0,u,i,j,u[4:]])
 bm=legal[0];N=0;L=150000
 try:
  for d in range(1,12):
   a=-30000;bv=a
   for r in R:
    _,u,i,j,pr=r;p=b[i];c=b[j];n=p
    if pr:n=("pnbrqk".index(pr)+1)*s
    sv=[(k,b[k])for k in(i,j,j+10,j-10,i+3,i-4,i+1,i-1,j+1,j-1)if 0<=k<120]
    b[i]=0;b[j]=n;x=0
    if abs(p)==6 and abs(j-i)==2:
     k=i+3 if j>i else i-4;b[k]=0;b[(i+j)//2]=4*s
    if abs(p)==1 and c==0 and (j-i)%10:b[j+10*s]=0;x=T[-p][j+10*s]
    hh=ZS if s<0 else 0
    for k2 in range(21,99):
     if b[k2]and b[k2]!=9:hh^=Z[b[k2]+6][k2]
    v=-S(b,-s,sc-T[p][i]+T[n][j]-(T[c][j]if c else 0)-x,d-1,-30000,-a,1,hh)
    for k,z in sv:b[k]=z
    r[0]=v
    if v>bv:bv=v;a=v;cur=u
   bm=cur;R.sort(key=lambda r:-r[0])
 except X:0
 return bm
while 1:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":M(g["fen"],g["legal_moves"])})
