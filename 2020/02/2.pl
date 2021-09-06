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
                 "\n",
                 pass_list(N1),
                 {
                     occurrences_of_term(Char, Pass, Num),
                     between(Min, Max, Num) ->
                         N is N1 + 1; N is N1
                 }.

pass_list_2(0) --> call(eos), !.
pass_list_2(N) --> integer(First),
                   "-",
                   integer(Second),
                   " ",
                   string([Char]),
                   ": ",
                   string(Pass),
                   "\n",
                   pass_list_2(N1),
                   {
                       (nth1(First, Pass, Char) xor nth1(Second, Pass, Char)) ->
                           N is N1 + 1; N is N1
                   }.

xor(L, R) :- (L ; R), \+ (L, R).
