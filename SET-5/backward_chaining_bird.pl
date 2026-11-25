% Facts from the question.
bird(parrot).
healthy(parrot).

% General rule: backward chaining proves flight by seeking the bird fact.
can_fly(Animal) :- bird(Animal).

% Example query in SWI-Prolog:
% ?- can_fly(parrot).
% true.
%
% The healthy/1 fact is included as given; it is not needed to prove flight.
