#!/usr/bin/env/ swipl

:- use_module(library(dcg/basics)).
:- use_module(library(dcg/high_order)).

:- initialization(main, main).

main() :-
    phrase_from_stream(instructions(Rotations), user_input),
    find_password(Rotations, P1, P2),
    format('Part 1: ~d', P1), nl,
    format('Part 2: ~d', P2), nl.


instructions(Rs) --> sequence(rotation, (blank, \+ eos), Rs), blank.

rotation([Dir, Num]) --> direction(Dir), number(Num).
direction(left) --> `L`.
direction(right) --> `R`.

find_password(Rotations, P1, P2) :-
    find_password(Rotations,  50, P1, 0, P2, 0).

find_password([], _, P1, P1, P2, P2).
find_password([Rot|RotTail], Pos, P1, P1_Acc, P2, P2_Acc) :-
    rotate(Rot, Pos, NextPos, ZerosPassed),
    NextAll is P2_Acc + ZerosPassed,
    ( NextPos =:= 0 ->
        find_password(RotTail, NextPos, P1, P1_Acc+1, P2, NextAll)
    ;   find_password(RotTail, NextPos, P1, P1_Acc, P2, NextAll)
    ).

rotate([left, Num], Pos, NextPos, Zeros) :-
    NextPos is (Pos - Num) mod 100,
    Zeros is (-Pos mod 100 + Num) // 100.
rotate([right, Num], Pos, NextPos, Zeros) :-
    NextPos is (Pos + Num) mod 100,
    Zeros is (Pos + Num) // 100.
