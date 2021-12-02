:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).

depth(_, 0) --> call(eos), !.
depth(Last, N) --> integer(Next),
                   "\n",
                   depth(Next, N1),
                   {
                       Next > Last ->
                           N is N1 + 1; N is N1
                   }.
