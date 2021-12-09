:- use_module(library(clpfd)).
:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).


read_crabs([Crab]) --> integer(Crab), call(eos), !.
read_crabs([Crab|OtherCrabs]) --> integer(Crab), ",", read_crabs(OtherCrabs).

%%%%% Part 1 %%%%%

part_1(Ans):-
    phrase_from_file(read_crabs(Crabs), 'input'),
    median(Crabs, Median),
    fuel_usage_1(Crabs, Ans, Median).

median(List, Median):-
    length(List, Len),
    msort(List, Sorted),
    Index is Len // 2,
    nth0(Index, Sorted, Median).

fuel_usage_1([], 0, _).
fuel_usage_1([Crab|Crabs], Cost, Distance):-
    Cost #= abs(Distance-Crab) + Cost2,
    fuel_usage_1(Crabs, Cost2, Distance).

%% Brute force

part_1_brute(Ans):-
    phrase_from_file(read_crabs(Crabs), 'input'),
    max_list(Crabs, MaxDistance),
    findall(Cost, possible_fuel_usage_1(Crabs, Cost, MaxDistance), Costs),
    min_list(Costs, Ans).

possible_fuel_usage_1(Crabs, Cost, MaxDistance):-
    between(0, MaxDistance, Distance),
    fuel_usage_1(Crabs, Cost, Distance).

%%%%% Part 2 %%%%%

part_2(Ans):-
    phrase_from_file(read_crabs(Crabs), 'input'),
    sum_list(Crabs, Sum), length(Crabs, N),
    Mean is round(Sum / N),
    fuel_usage_2(Crabs, Ans, Mean).

fuel_usage_2([], 0, _).
fuel_usage_2([Crab|Crabs], Cost, Distance):-
    Dist #= abs(Distance-Crab),
    Cost #= Dist * (Dist+1) // 2 + Cost2,
    fuel_usage_2(Crabs, Cost2, Distance).

%% Brute force

part_2_brute(Ans):-
    phrase_from_file(read_crabs(Crabs), 'input'),
    max_list(Crabs, MaxDistance),
    findall(Cost, possible_fuel_usage_2(Crabs, Cost, MaxDistance), Costs),
    min_list(Costs, Ans).

possible_fuel_usage_2(Crabs, Cost, MaxDistance):-
    between(0, MaxDistance, Distance),
    fuel_usage_2(Crabs, Cost, Distance).
