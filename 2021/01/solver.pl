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

depth3(_, 0) --> call(eos), !.
depth3([Head|Tail], N) --> integer(Next),
                           "\n",
                           depth3(NextList, N1),
                           {
                               append([Head], Tail, PrevList),
                               append(Tail, [Next], NextList),
                               sum_list(PrevList, First),
                               sum_list(NextList, Second),
                               Second > First ->
                                   N is N1 + 1; N is N1
                           }.
