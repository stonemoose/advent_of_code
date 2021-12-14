:- use_module(library(clpfd)).
:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, chars).

solve(Part1, Part2):-
    findall(true, walk_part1("start", "end"), P),
    length(P, Part1),
    findall(true, walk_part2("start", "end"), P2),
    length(P2, Part2).

walk_part1(A, B):-
    path(A, B, [A, B]).

walk_part2(A, B):-
    path_part2(A, B, [A, B]).

path(A, B, Visited):-
    connected(A, X),
    (
        B = X;
        (big(X) -> path(X, B, Visited));
        (not(member(X, Visited)), path(X, B, [X|Visited]))
    ).

path_part2(A, B, Visited):-
    connected(A, X),
    (
        B = X;
        not(X = "start"), not(X = "end"),
        (big(X)
        -> path_part2(X, B, Visited)
        ; (member(X, Visited)
          -> list_to_set(Visited, Visited)
          ; true
          ), path_part2(X, B, [X|Visited])
        )
    ).

big([Cave|_]):-
    char_type(Cave, upper).

small([Cave|_]):-
    char_type(Cave, lower).

connected(A, B):-
    edge(A, B);
    edge(B, A).


edge("he", "JK").
edge("wy", "KY").
edge("pc", "XC").
edge("vt", "wy").
edge("LJ", "vt").
edge("wy", "end").
edge("wy", "JK").
edge("end", "LJ").
edge("start", "he").
edge("JK", "end").
edge("pc", "wy").
edge("LJ", "pc").
edge("at", "pc").
edge("xf", "XC").
edge("XC", "he").
edge("pc", "JK").
edge("vt", "XC").
edge("at", "he").
edge("pc", "he").
edge("start", "at").
edge("start", "XC").
edge("at", "LJ").
edge("vt", "JK").
