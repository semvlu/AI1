% isnumber(X) is true if X is a isnumber
isnumber(0).
isnumber(s(X)) :- isnumber(X).

% plus(X,Y,Z) is true if X + Y = Z
plus(0,X,X) :- isnumber(X).
plus(s(X),Y,s(Z)) :- plus(X,Y,Z).

% minus(X,Y,Z) is true if X - Y =Z
minus(X,0,X) :- isnumber(X).
minus(s(X),s(Y),Z) :- minus(X,Y,Z).

% times(X,Y,Z) is true if X * Y = Z
times(X,0,0) :- isnumber(X).
times(X,s(Y),Z) :- times(X,Y,Z1), plus(X,Z1,Z).

% pow(X,Y,Z) is true if X^Y = Z
pow(X,0,s(0)) :- isnumber(X).
pow(X,s(Y),Z) :- pow(X,Y,Z1), times(X,Z1,Z).

% odd and even
even(0).
even(s(s(X))):- even(X).
    
odd(s(0)).
odd(s(s(X))) :- odd(X).

% div2(N,D) and divi2(N,D) are true if N/2 equals D
div2(0,0).
div2(s(s(N)), s(D)) :- div2(N, D).

divi2(N, D) :- times(D, s(s(0)), N).

% logarithms
log(X, B, N) :- pow(B, N, X).

% Fibonacci
fib(0, 0).
fib(s(0), s(0)).
fib(s(s(X)),Y) :- fib(s(X),Y1),fib(X,Y2),plus(Y1,Y2,Y).

% power in O(log N)
power(X,0,s(0)) :- isnumber(X).	
power(X,s(N),Y):- odd(s(N)),times(X,X1,Y),power(X,N,X1).
power(X,N,Y) :- even(N),power(X1,N1,Y),divi2(N,N1),times(X,X,X1).

% lists
member(X,[X|L]).
member(X,[L|TAIL]) :- member(X,TAIL).

concat(L, X, Y) :- append(X, Y, L).

reverse([],[]).
reverse([H|T],R) :- reverse(T,RT),append(RT,[H],R).

palindrome(L) :- reverse(L, L).

    