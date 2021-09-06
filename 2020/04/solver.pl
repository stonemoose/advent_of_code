:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- use_module(library(clpfd)).
:- set_prolog_flag(double_quotes, codes).

passport_list(0) --> call(eos), !.
passport_list(N) --> passport(C), "\n\n", !,  passport_list(N1),
                     {
                         C is 7 ->
                             N is N1 + 1;
                         N is N1
                     }.

passport(1) --> field.
passport(0) --> cid.
passport(C) --> field, seperator, !, passport(C1), {C is C1+1}.
passport(C) --> cid, seperator, !, passport(C).

anything --> [].
anything --> [Char], anything, {\+ member(Char, " \n")}.

seperator --> (" "; "\n").

field --> "byr:", anything.
field --> "iyr:", anything.
field --> "eyr:", anything.
field --> "hgt:", anything.
field --> "hcl:", anything.
field --> "ecl:", anything.
field --> "pid:", anything.

cid --> "cid:", anything.

