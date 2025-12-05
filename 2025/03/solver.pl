#!/usr/bin/env/ swipl

:- use_module(library(dcg/basics)).
:- use_module(library(dcg/high_order)).
:- set_prolog_flag(double_quotes, codes).

:- initialization(main, main).

main() :-
    phrase_from_stream(banks(BatteryBanks), user_input),
    maplist(joltage_value(2), BatteryBanks, Joltages),
    sumlist(Joltages, P1),
    maplist(joltage_value(12), BatteryBanks, Joltages2),
    sumlist(Joltages2, P2),
    format('Part 1: ~d', P1), nl,
    format('Part 2: ~d', P2), nl.


joltage_value(Length, Bank, Joltage):-
    joltage(Bank, Batteries, Length),
    number_string(Joltage, Batteries).

joltage(_, [], 0).
joltage(Bank, [Battery|RestBatteries], Length):-
    Length > 0,
    RestLength is Length - 1,
    length(Buffer, RestLength),
    append(Available, Buffer, Bank),
    max_member(Battery, Available),
    append(_, [Battery|RestBank], Bank),
    joltage(RestBank, RestBatteries, RestLength).


banks(Banks) --> sequence(bank, (blank, \+ eos), Banks), blank.
bank(Bank) --> sequence(digit, Bank).
