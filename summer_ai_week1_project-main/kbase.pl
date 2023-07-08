singing(elon).
playingGuitar(mark).
playingGuitar(satya).
singing(jeff).

playingGuitar(elon):-
    happy(elon).

happy(mark):-
    singing(mark),
    playingGuitar(mark).

happy(satya):-
    singing(satya);
    playingGuitar(satya).

sad(satya):-
    not(playingGuitar(satya)).

grumpy(jeff):-
    singing(jeff)->
        false
        ;
        true.

