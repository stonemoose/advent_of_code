:- use_module(library(pio)).
:- use_module(library(dcg/basics)).

integers([]) --> call(eos), !.
integers([X|Xs]) --> integer(X), "\n", integers(Xs).

sum2(List, P) :-
    select(X, List, L1),
    select(Y, L1, _),
    2020 is X + Y,
    P is X * Y.

sum3(List, P) :-
    select(X, List, L1),
    select(Y, L1, L2),
    select(Z, L2, _),
    2020 is X + Y + Z,
    P is X * Y * Z.
