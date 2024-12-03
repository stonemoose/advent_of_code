:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).

read_input(Part1, Part2) --> string_without("\n", Report), eos,
                {
                    split_string(Report, " ", "", StringLevels),
                    maplist(number_string, Levels, StringLevels),
                    safe(Levels, P1, P2),
                    Part1 is P1,
                    Part2 is P2
                }.
read_input(Part1, Part2) --> string_without("\n", Report), "\n", read_input(Sum1, Sum2),
                {
                    split_string(Report, " ", "", StringLevels),
                    maplist(number_string, Levels, StringLevels),
                    safe(Levels, P1, P2),
                    Part1 is Sum1 + P1,
                    Part2 is Sum2 + P2
                }.

safe(Levels, 1, 1):-
    (increasing(Levels) ; decreasing(Levels)),
    safeLevels(Levels), !.
safe(Levels, 0, 1):-
    select(_, Levels, Rest),
    (increasing(Rest) ; decreasing(Rest)),
    safeLevels(Rest), !.
safe(_, 0, 0).

    
safeLevels([]).
safeLevels([_]).
safeLevels([First, Second | RestLevels]):-
    abs(First - Second) < 4,
    safeLevels([Second | RestLevels]).


solve(Part1, Part2):-
    phrase_from_file(read_input(Part1, Part2), 'input').


%% Helper

increasing([]).
increasing([_]).
increasing([A, B | Tail]):-
    A < B, 
    increasing([B | Tail]).

decreasing([]).
decreasing([_]).
decreasing([A, B | Tail]):-
    A > B, 
    decreasing([B | Tail]).