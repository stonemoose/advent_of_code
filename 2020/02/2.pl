:- use_module(library(pio)).
:- use_module(library(occurs)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).

pass_list(0) --> call(eos), !.
pass_list(N) --> integer(Min),
                 "-",
                 integer(Max),
                 " ",
                 string([Char]),
                 ": ",
                 string(Pass),
                 "\n", !,
                 pass_list(N1),
                 {
                     occurrences_of_term(Char, Pass, Num),
                     between(Min, Max, Num) ->
                         N is N1 + 1; N is N1
                 }.
