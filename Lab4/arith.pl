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

% even(N) is true if N % 2 = 0
even(N) :- mod(N,2) =:= 0.

% odd(N) is true if N % 2 = 1
odd(N) :- mod(N,2) =:= 1.

% div2(N,D) is true if N / 2 = D
div2(N,D) :- /(N,2) =:= D

% divi2(N,D) is true if N / 2 = D (allow using times())
divi2(N,D) :- times(D,2) =:= N

% log(X,B,N) is true iff B^N = X
log(X,B,N) :- pow(B,N,X)

% fib(X,Y) is true iff fib(X) = Y
fib(X,Y) :-

% power(X,N,Y) is true if X^N = Y
power(X,N,Y) :- 

% Example queries:
% Isnumbers are represented as successors of 0. For example, 2 is s(s(0)).
% 2+2=4 is plus(s(s(0)), s(s(0)), s(s(s(s(0)))))
% 3*2=? is times(s(s(s(0))), s(s(0)), X)
