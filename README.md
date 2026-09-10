# Real-Time Task Scheduling Verification with UPPAAL

Formal modeling and verification of non-preemptive EDF scheduling
on a shared CPU using UPPAAL timed automata.

## Model

The system consists of parameterized real-time tasks and a shared CPU.

Each task has:

* bounded execution time
* deadline
* Ready, Running, Finished, and Missed locations

The CPU uses a non-preemptive Earliest Deadline First (EDF) policy.

## Verification

Main safety property:

A\[] not (T0.Missed || T1.Missed || T2.Missed)

The model was evaluated using both schedulable and unschedulable
three-task configurations.

## Results

|Task Set|Deadlines|Result|
|-|-|-|
|Schedulable|{12, 7, 5}|Property satisfied|
|Unschedulable|{10, 6, 4}|Deadline violation (T1)|

UPPAAL diagnostic traces were used to inspect deadline violations.

## Repository

models/
├── edf\_3tasks\_schedulable.xml
└── edf\_3tasks\_unschedulable.xml

## v1.0

Initial non-preemptive EDF scheduling model.

## Next Steps

* Task release/arrival times
* Fixed-Priority Scheduling
* EDF vs. Fixed-Priority comparison





\## EDF vs. Fixed-Priority Scheduling



EDF selects the ready task with the earliest deadline.



Fixed-Priority Scheduling selects the ready task with the highest

pre-assigned static priority.



For the comparison workload, EDF and FPS use the same release times,

execution-time bounds, and deadlines. Under FPS, T1 can miss its deadline

because T2 has a higher fixed priority.

