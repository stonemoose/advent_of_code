:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).

toboggan(0, 323) --> call(eos), !.
toboggan(Trees, N) --> string(Line), "\n", !, toboggan(Trees1, N1),
                       {
                           N is N1 - 1,
                           string_length(Line, Len),
                           Place is mod(N * 3, Len),
                           C is "#",
                           (nth0(Place, Line, C) ->
                                Trees is Trees1 + 1;
                            Trees is Trees1)
                       }.

tobogganRD(0, 323, _, _) --> call(eos), !.
tobogganRD(Trees, N, R, D) --> string(Line), "\n", !, tobogganRD(Trees1, N1, R, D),
                               {
                                   N is N1 - 1,
                                   (
                                       \+ 0 is mod(N, D) -> Trees is Trees1;
                                       string_length(Line, Len),
                                       Place is mod(N * R / D, Len),
                                       C is "#",
                                       (nth0(Place, Line, C) ->
                                            Trees is Trees1 + 1;
                                        Trees is Trees1)
                                   )
                               }.
