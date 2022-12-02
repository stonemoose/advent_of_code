:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).



read_input(Part1, Part2) --> string_without("\n", Round), eos,
                {
                    score(Round, Part1),
                    score2(Round, Part2)
                }.
read_input(Part1, Part2) --> string_without("\n", Round), "\n", read_input(Sum1, Sum2),
                {
                    score(Round, Value1),
                    score2(Round, Value2),
                    Part1 is Sum1 + Value1,
                    Part2 is Sum2 + Value2
                }.

solve(Part1, Part2):-
    phrase_from_file(read_input(Part1, Part2), 'input').

score("A X", 4).
score("A Y", 8).
score("A Z", 3).
score("B X", 1).
score("B Y", 5).
score("B Z", 9).
score("C X", 7).
score("C Y", 2).
score("C Z", 6).

score2("A X", 2).
score2("A Y", 4).
score2("A Z", 8).
score2("B X", 1).
score2("B Y", 5).
score2("B Z", 9).
score2("C X", 2).
score2("C Y", 6).
score2("C Z", 7).