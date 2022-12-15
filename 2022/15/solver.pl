:- use_module(library(pio)).
:- use_module(library(dcg/basics)).
:- set_prolog_flag(double_quotes, codes).

boilerplate(A, B):-
    string_without("\n123456789-", A, B)

read_sensor_beacons([X, Y, BX, XY]) --> 
    boilerplate, "=", integer(X), boilerplate, "=", integer(Y), 
    boilerplate, "=", integer(BX), "=", boilerplate, "=", integer(XY), eos.

read_sensor_beacons([X|OtherSensors]) --> 
    string(_), integer(X), boilerplate, integer(Y), 
    string(_), integer(BX), boilerplate, integer(XY), eol, read_sensor_beacons(OtherSensors).



%%%% Part 1 %%%%

part_1(Ans):-
    phrase_from_file(read_sensor_beacons(SensorBeacons), 'input.txt'),
    Ans = SensorBeacons.

%%%% Part 2 %%%%

part_2(Ans):-
    phrase_from_file(read_sensor_beacons(SensorBeacons), 'input.txt').
