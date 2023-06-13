link(a,b).
link(b,f).
link(c,d).
link(c,g).
link(d,h).
link(e,f).
link(f,j).
link(g,k).
link(h,l).
link(i,m).
link(j,k).
link(l,p).
link(m,n).
link(n,o).

link(b,a).
link(f,b).
link(d,c).
link(g,c).
link(h,d).
link(f,e).
link(j,f).
link(k,g).
link(l,h).
link(m,i).
link(k,j).
link(p,l).
link(n,m).
link(o,n).

path(X,Y) :- link(X,Y).
path(X,Y) :- path(X,Z), link(Z,Y).