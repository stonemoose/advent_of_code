#!/usr/bin/env/ swipl
% Very slow and unoptomized!

:- use_module(library(clpfd)).
:- use_module(library(dcg/basics)).
:- use_module(library(dcg/high_order)).

:- initialization(main, main).

main() :-
    phrase_from_stream(product_ids(Ranges), user_input),
    sum_invalid(Ranges, P1, P2),
    format('Part 1: ~d', P1), nl,
    format('Part 2: ~d', P2), nl.

%% Parse %%

product_ids(Ranges) --> sequence(range, ",", Ranges), blank.

range([Start, End]) --> number(Start), "-", number(End).

%% Solve %%

sum_invalid(Ranges, P1, P2) :-
    sum_invalid(Ranges, P1, 0, P2, 0).

sum_invalid([], P1, P1, P2, P2).
sum_invalid([[Start, End]|RangeTail], P1, P1_Acc, P2, P2_acc):-
    findall(Id, (between(Start, End, Id), invalid2(Id)), InvalidIdsP1),
    findall(Id, (between(Start, End, Id), invalidN(Id)), InvalidIdsP2),
    sumlist(InvalidIdsP1, Num),
    sumlist(InvalidIdsP2, Num2),
    sum_invalid(RangeTail, P1, P1_Acc+Num, P2, P2_acc+Num2).


invalid2(Id) :-
    number_codes(Id, IdList),
    append(Seq, Seq, IdList).

invalidN(Id) :-
    number_codes(Id, IdList),
    append(Seq, [_|_], IdList),
    length(Seq, SeqLen),
    length(IdList, IdLen),
    0 < SeqLen,
    IdLen mod SeqLen =:= 0,
    N is IdLen // SeqLen,
    repeat(Seq, N, IdList),!.

repeat(List, N, Out) :-
    repeat(List, N, Out, List).

repeat(_, 1, Out, Out).
repeat(List, N, Out, OutAcc) :-
    N > 1,
    M #= N-1,
    append(List, OutAcc, NextOut),
    repeat(List, M, Out, NextOut).
