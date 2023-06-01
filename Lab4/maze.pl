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


path(X,Y) :- link(X,Y).
path(X,Y) :- path(X,Z), link(Z,Y).

path(a,p)
path(a,m)