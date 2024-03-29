:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).

read_elves([ElfCalories]) --> sum_items(ElfCalories), call(eos), !.
read_elves([ElfCalories|OtherElves]) --> sum_items(ElfCalories), "\n\n", read_elves(OtherElves).

sum_items(Calories) --> integer(Calories). 
sum_items(Calories) --> integer(Item), "\n", sum_items(Calories0), 
                    {
                        Calories is Item + Calories0
                    }.


%%%% Part 1 %%%%

part_1(Ans):-
    phrase_from_file(read_elves(Elves), 'input'),
    max_list(Elves, Ans).

%%%% Part 2 %%%%

part_2(Ans):-
    phrase_from_file(read_elves(Elves), 'input'),
    % max3_list(Elves, N1, N2, N3),
    max_list(Elves, N1),
    delete(Elves, N1, ElvesNoMax),
    max_list(ElvesNoMax, N2),
    delete(ElvesNoMax, N2, ElvesNoMax2),
    max_list(ElvesNoMax2, N3),
    Ans is N1 + N2 + N3.
