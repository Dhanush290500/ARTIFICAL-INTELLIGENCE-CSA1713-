% Sum integers from 1 through N.
sum_to_n(0, 0) :- !.
sum_to_n(N, Sum) :- N > 0, N1 is N - 1, sum_to_n(N1, S1), Sum is S1 + N.

% Query: ?- sum_to_n(5, Sum).  Sum = 15.