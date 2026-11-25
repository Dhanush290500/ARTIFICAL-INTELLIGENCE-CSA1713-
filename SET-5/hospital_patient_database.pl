% Sample hospital records: patient(Name, Age, Disease, Doctor).
patient(aarav, 34, flu, dr_sharma).
patient(meera, 52, diabetes, dr_rao).
patient(isha, 19, flu, dr_sharma).
patient(rahul, 67, hypertension, dr_mehta).
patient(kavya, 45, diabetes, dr_mehta).

% Query patients by disease or by treating doctor.
patients_with_disease(Disease, Names) :-
    findall(Name, patient(Name, _, Disease, _), Names).

patients_treated_by(Doctor, Names) :-
    findall(Name, patient(Name, _, _, Doctor), Names).

% Individual record queries are also available directly, for example:
% ?- patient(Name, Age, flu, Doctor).
