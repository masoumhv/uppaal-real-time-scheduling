# Real-Time Task Scheduling Verification with UPPAAL

Formal modeling and verification of non-preemptive real-time task scheduling
on a shared CPU using UPPAAL timed automata.

The project models task release times, bounded execution times, and deadlines,
and compares Earliest Deadline First (EDF) with Fixed-Priority Scheduling
(FPS). Verification is performed with UPPAAL and automated using Python,
`verifyta`, and PyUPPAAL.

## Model

Each real-time task is characterized by:

- a release time
- bounded execution time
- a deadline
- `NotReleased`, `Ready`, `Running`, `Finished`, and `Missed` locations

Tasks execute on a shared CPU using non-preemptive scheduling. Once a task
starts executing, it runs until completion before another ready task can
use the CPU.

The project includes schedulable and deliberately unschedulable task sets
to evaluate deadline-miss detection.

## EDF vs. Fixed-Priority Scheduling

EDF and FPS are evaluated using the same synthetic workload:

| Task | Release | Execution | Deadline | FPS Priority |
|---|---:|---:|---:|---:|
| T0 | 0 | 2–3 | 8 | 0 |
| T1 | 1 | 1–2 | 5 | 2 |
| T2 | 1 | 2–3 | 8 | 1 |

Lower numerical values represent higher fixed priority.

Under EDF, T1 is selected before T2 because it has the earlier deadline.
Under the selected fixed-priority assignment, T2 is selected before T1.

The main safety property is:

```text
A[] not (T0.Missed || T1.Missed || T2.Missed)
```

### Verification Results

| Scenario | Policy | Result |
|---|---|---|
| Comparison workload | EDF | SATISFIED |
| Comparison workload | FPS | NOT SATISFIED |
| Unschedulable test case | EDF | NOT SATISFIED |

For the common workload, EDF satisfies the deadline-miss safety property,
while the selected fixed-priority assignment admits an execution in which
a deadline is missed. This result is specific to the modeled workload and
priority assignment.

## Automated Verification

A Python script executes UPPAAL `verifyta` for multiple models and records
the verification results in CSV format.

```text
UPPAAL models → Python → verifyta → verification results → CSV
```

Run the automated verification with:

```bash
python scripts/run_verification.py
```

## PyUPPAAL Experiment

PyUPPAAL is used to programmatically load and modify an existing UPPAAL
model while `verifyta` remains the underlying verification engine.

The included experiment:

- loads the EDF model
- creates a derived model
- changes the T1 deadline from 5 to 4
- verifies the modified model
- parses the generated counterexample

The modified model violates the safety property, and the counterexample
identifies a state in which `T1` reaches `Missed`.

Run the experiment with:

```bash
python scripts/generate_and_verify.py
```

Generated models and diagnostic trace files are excluded from version
control because they can be reproduced by the script.

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
  generate_and_verify.py

results/
  verification_results.csv
```

## Tools

- UPPAAL 5.0
- `verifyta`
- Python
- PyUPPAAL

## Status

The project provides a reproducible formal-verification workflow for
non-preemptive real-time scheduling, including EDF/FPS comparison,
deadline-miss verification, automated experiments, and counterexample
analysis.

The initial EDF models are available as the `v1.0` release.