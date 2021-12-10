:- use_module(library(clpfd)).
:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).

solve(Part1, Part2):-
    phrase_from_file(lines(Part1, Part2List), 'input'),
    median(Part2List, Part2).

median(List, Median):-
    length(List, Len),
    msort(List, Sorted),
    Index is Len // 2,
    nth0(Index, Sorted, Median).

lines(0, []) --> call(eos), !.
lines(Corrupt, Incomplete) --> multi_corrupt(N), "\n", lines(Corrupt2, Incomplete), {Corrupt #= Corrupt2 + N}.
lines(Corrupt, [IHead|Incompletes]) --> multi_incomplete(IHead), "\n", lines(Corrupt, Incompletes).


%%%%% Corrupt lines %%%%%%

multi_corrupt(N) --> corrupt(N).
multi_corrupt(N) --> left_bracket, multi_corrupt(N).
multi_corrupt(N) --> corrupt(N), multiple_brackets.
multi_corrupt(N) --> multi_chunk, multi_corrupt(N).

corrupt(3)     --> ("[" | "{" | "<"), possible_multi_chunk, ")".
corrupt(57)    --> ("(" | "{" | "<"), possible_multi_chunk, "]".
corrupt(1197)  --> ("(" | "[" | "<"), possible_multi_chunk, "}".
corrupt(25137) --> ("(" | "[" | "{"), possible_multi_chunk, ">".


%%%%% Incomplete lines %%%%%%

multi_incomplete(N) --> incomplete(N).
multi_incomplete(N) --> multi_chunk, multi_incomplete(N).
multi_incomplete(N) --> incomplete(N1), !, multi_incomplete(N2), {N #= N2*5 + N1}.

incomplete(1) --> "(", possible_multi_chunk.
incomplete(2) --> "[", possible_multi_chunk.
incomplete(3) --> "{", possible_multi_chunk.
incomplete(4) --> "<", possible_multi_chunk.


%%%%% Chunks following the rules %%%%%%

possible_multi_chunk --> [] | multi_chunk.

multi_chunk --> chunk.
multi_chunk --> chunk, multi_chunk.

chunk --> "(", ")".
chunk --> "[", "]".
chunk --> "{", "}".
chunk --> "<", ">".
chunk --> "(", multi_chunk, ")".
chunk --> "[", multi_chunk, "]".
chunk --> "{", multi_chunk, "}".
chunk --> "<", multi_chunk, ">".


%%%%% Brackets %%%%%

multiple_brackets --> any_bracket.
multiple_brackets --> any_bracket, multiple_brackets.

any_bracket --> left_bracket | right_bracket.
left_bracket --> "(" | "[" | "{" | "<".
right_bracket --> ")" | "]" | "}" | ">".
