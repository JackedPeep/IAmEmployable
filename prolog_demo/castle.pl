% Define the room facts
room(dunstanburgh, enter, foyer, 1).
room(dunstanburgh, foyer, livingRoom, 1).
room(dunstanburgh, foyer, hall, 2).
room(dunstanburgh, hall, kitchen, 4).
room(dunstanburgh, hall, garage, 3).
room(dunstanburgh, kitchen, exit, 1).

room(windsor, enter, foyer, 1).
room(windsor, foyer, hall, 2).
room(windsor, foyer, dungeon, 1).
room(windsor, hall, throne, 1).
room(windsor, hall, stairs, 4).
room(windsor, stairs, dungeon, 3).
room(windsor, throne, stairs, 1).
room(windsor, dungeon, escape, 5).
room(windsor, escape, exit, 1).

room(alnwick, enter, foyer, 1).
room(alnwick, foyer, hall, 2).
room(alnwick ,hall ,throne ,1 ).
room(alnwick ,hall ,stairs ,4 ).
room(alnwick ,stairs ,dungeon ,3 ).
room(alnwick ,dungeon ,foundry ,5 ).
room(alnwick ,foyer ,passage ,1 ).
room(alnwick ,passage ,foundry ,1 ).
room(alnwick ,foundry ,exit ,4 ).

% Define the path predicate
path(CastleName,CostLimit,A,B,Cost,[B|T]) :-
    room(CastleName,A,B,Cost),
    Cost =< CostLimit,
    T = [].
path(CastleName,CostLimit,A,B,Cost,[X|T]) :-
    room(CastleName,A,X,C),
    C < CostLimit,
    NewCostLimit is CostLimit - C,
    path(CastleName,CostLimit,X,B,D,T),
    Cost is C + D.

% Define the solveRoomsWithinCost predicate
solveRoomsWithinCost(CastleName,CostLimit) :-
    path(CastleName,CostLimit,'enter','exit',Cost,_),
    write('Cost is '), write(Cost), write(' within limit of '), writeln(CostLimit).

% Define the solveRooms predicate
solveRooms(CastleName,[Room|Rooms]) :-
    solveRoomsHelper(CastleName,['enter'|[Room|Rooms]]).

solveRoomsHelper(_,[]).
solveRoomsHelper(CastleName,[A,B|T]) :-
    path(CastleName,_,'enter',B,C,_),
    write(B), write(' '), writeln(C),
    solveRoomsHelper(CastleName,[B|T]).
