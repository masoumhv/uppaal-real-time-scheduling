# Real-Time Task Scheduling Verification with UPPAAL

Formal modeling and verification of non-preemptive real-time scheduling
on a shared CPU using UPPAAL timed automata.

The project includes Earliest Deadline First (EDF) and Fixed-Priority
Scheduling (FPS), task release times, deadline verification, and automated
verification using Python and UPPAAL `verifyta`.

## Model

The system consists of parameterized real-time tasks and a shared CPU.

Each task includes:

- a release time
- bounded execution time
- a deadline
- `NotReleased`, `Ready`, `Running`, `Finished`, and `Missed` locations

Scheduling is non-preemptive: once a task starts executing, it runs until
completion before another ready task can use the CPU.

## Verification

The main safety property checks that no task reaches the `Missed` location:

```text
A[] not (T0.Missed || T1.Missed || T2.Missed)
```

Verification is performed using the UPPAAL verifier and the command-line
`verifyta` tool.

## Initial EDF Models

The initial version of the project evaluated schedulable and unschedulable
three-task EDF configurations.

| Task Set | Deadlines | Result |
|---|---|---|
| Schedulable | {12, 7, 5} | Property satisfied |
| Unschedulable | {10, 6, 4} | Deadline violation detected |

UPPAAL diagnostic traces were used to inspect deadline violations.

## Arrival-Aware Scheduling

The model was extended with explicit task release times.

Tasks begin in the `NotReleased` location and become ready at their specified
release times. Dispatch is urgent when the CPU is free and an eligible task is
ready.

Both schedulable and unschedulable arrival-aware EDF scenarios are included.

## EDF vs. Fixed-Priority Scheduling

A common synthetic workload is used to compare non-preemptive EDF and FPS.

| Task | Release Time | Execution Time | Deadline | FPS Priority |
|---|---:|---:|---:|---:|
| T0 | 0 | 2–3 | 8 | 0 |
| T1 | 1 | 1–2 | 5 | 2 |
| T2 | 1 | 2–3 | 8 | 1 |

Lower priority values indicate higher fixed priority.

Under EDF, T1 is selected before T2 because it has the earlier deadline.
The deadline-miss safety property is satisfied.

Under FPS, T2 is selected before T1 because T2 has a higher fixed priority.
This ordering admits an execution in which T1 misses its deadline.

### Verification Results

| Scenario | Policy | Result |
|---|---|---|
| Comparison workload | EDF | SATISFIED |
| Comparison workload | FPS | NOT SATISFIED |
| Unschedulable test case | EDF | NOT SATISFIED |

The unschedulable EDF model is included as a separate negative test and is
not part of the EDF–FPS comparison.

## Automated Verification

A Python script executes UPPAAL `verifyta` automatically for multiple models
and stores the verification results in CSV format.

This provides a reproducible workflow for running and recording verification
experiments.

## Repository Structure

```text
models/
  edf_3tasks_schedulable.xml
  edf_3tasks_unschedulable.xml
  edf_arrivals_3tasks.xml
  edf_arrivals_3tasks_unschedulable.xml
  fps_arrivals_3tasks.xml

queries/
  edf_arrivals.q

scripts/
  run_verification.py

results/
  verification_results.csv
```

## v1.0

Initial non-preemptive EDF scheduling model with schedulable and
unschedulable three-task configurations.

## Current Status

The project currently supports:

- non-preemptive EDF scheduling
- explicit task release times
- deadline-miss verification
- fixed-priority scheduling
- EDF–FPS comparison using a common workload
- automated verification through Python and `verifyta`
- CSV-based result collection

