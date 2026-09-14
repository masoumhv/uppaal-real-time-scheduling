import subprocess
import csv


VERIFYTA = r"C:\Program Files\UPPAAL-5.0.0\app\bin\verifyta.exe"


def verify_model(model_path, query_path):
    result = subprocess.run(
        [VERIFYTA, model_path, query_path],
        capture_output=True,
        text=True
    )

    output = result.stdout + result.stderr

    if "Formula is satisfied" in output:
        return "SATISFIED"

    if "Formula is NOT satisfied" in output:
        return "NOT SATISFIED"

    return "UNKNOWN"


experiments = [
    {
        "scenario": "Comparison",
        "policy": "EDF",
        "model": r"models\edf_arrivals_3tasks.xml"
    },
    {
        "scenario": "NegativeTest",
        "policy": "EDF",
        "model": r"models\edf_arrivals_3tasks_unschedulable.xml"
    },
    {
        "scenario": "Comparison",
        "policy": "FPS",
        "model": r"models\fps_arrivals_3tasks.xml"
    }
]

query = r"queries\edf_arrivals.q"

results = []

for experiment in experiments:
    result = verify_model(
        experiment["model"],
        query
    )

    results.append([
    experiment["scenario"],
    experiment["policy"],
    experiment["model"],
    result
    ])

    print(
        experiment["scenario"],
        experiment["policy"],
        experiment["model"],
        "->",
        result
    )


with open("results/verification_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
    "Scenario",
    "Policy",
    "Model",
    "Result"
])

    writer.writerows(results)