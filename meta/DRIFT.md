# Spec drift audit

Wonde publishes no OpenAPI document — `meta/wonde.openapi.yaml` is hand-authored
against <https://docs.wonde.com/docs/api/sync/>, so it drifts silently as Wonde
edits the docs. This file records the last reconciliation.

## Audited 2026-08-08

Scope: the 24 operations the client already exposed, plus `listSchoolGroups`.
The ~30 further resources in the docs remain deliberately unimplemented — see
`TODO.md`.

| Resource | Drift found | Action |
|---|---|---|
| Classes | `type` url parameter never transcribed | Added as a plain string — it takes a comma-separated list, so an enum would reject valid input |
| Classes | `students.enrolments` missing from the `include` enum (both list and detail operations) | Added |
| Classes | object missing `type`, `priority`, `academic_year`, `year_group` | Added, all `nullable: true` |
| Classes | `alternative` not marked nullable | Marked nullable |
| Students | `classes.enrolments` missing from the `include` enum | Added |
| Students | `upfsm_date_ranges` — no such include; docs say `upfsm_exception_date_ranges` | Corrected |
| Students | `regional_data` missing from the `include` enum | Added |
| Students | object missing `title` and `gender_identity` | Added, both nullable |
| Students | `gender` enumerated `[male, female]`, generating an **enforced** validator | Enum dropped — see below |
| Groups | resource absent entirely | Added `listSchoolGroups` + `Group` schema |
| Employees | none — url parameters and object fields match the docs | — |
| Subjects | none | — |
| Lessons | none | — |
| Schools | none | — |
| Deletions | none | — |

### On the `Student.gender` enum

`enum: [male, female]` generated a real validator in `wonde/models/student.py`
that raises `ValueError` on any other value. The docs list six: male, female,
intersex or indeterminate, not stated/inadequately described, redacted for
privacy, other.

This was latent rather than live — sync works today, so Wonde must be returning
the two common values — but a single student with any of the other four would
have failed that school's entire sync. The spec also contradicted itself, pairing
the lower-case enum with `example: MALE`.

Replaced with a plain nullable string documenting the six values. An enum on a
free-text-ish upstream field is a liability: a new value added by Wonde breaks
parsing for every student in the school.

### Note on nullability

Because no schema in this spec declares a `required:` list, openapi-generator
emits every property as `Optional[X] = None` regardless of `nullable`. So
`nullable` here is documentation accuracy, not parsing behaviour — a missing
`nullable` will not break deserialisation. `Employee` still lacks the `nullable`
markers its docs specify; left alone as it has no runtime effect.

Anything recorded as "none" was checked against the docs and found faithful.
