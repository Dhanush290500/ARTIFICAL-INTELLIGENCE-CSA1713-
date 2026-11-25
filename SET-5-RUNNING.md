# Set 5: AI Practical Programs

The four Set 5 solutions are kept at the repository root, with no new experiment folder.

## 1. AO* search (Python)

```sh
python3 ao_star_search.py
```

The example graph has OR choices and an AND branch. The program prints the minimum-cost selected solution graph.

## 2. TSP using a genetic algorithm (Python)

```sh
python3 tsp_genetic_algorithm.py
```

The fixed seed makes the example reproducible. The distance matrix and genetic algorithm settings can be edited in the source.

## 3. Hospital patient database (Prolog)

Load `hospital_patient_database.pl` in SWI-Prolog and query:

```prolog
?- patients_with_disease(flu, Names).
?- patients_treated_by(dr_sharma, Names).
```

## 4. Backward chaining (Prolog)

Load `backward_chaining_bird.pl` and ask:

```prolog
?- can_fly(parrot).
```

The rule for `can_fly/1` proves the query by finding `bird(parrot)`; the supplied healthy fact is included as requested.
