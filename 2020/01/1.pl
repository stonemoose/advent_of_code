:- use_module(library(pio)).
:- use_module(library(dcg/basics)).

integers([]) --> call(eos), !.
integers([X|Xs]) --> integer(X), "\n", integers(Xs).

%% part 1
solve1(List, P) :-
    select(X, List, L1),
    select(Y, L1, _),
    2020 is X + Y,
    P is X * Y.

%% part 2
solve2(List, P) :-
    select(X, List, L1),
    select(Y, L1, L2),
    select(Z, L2, _),
    2020 is X + Y + Z,
    P is X * Y * Z.
