import shutil

import pyuppaal
from pyuppaal import UModel


VERIFYTA = r'"C:\Program Files\UPPAAL-5.0.0\app\bin\verifyta.exe"'

MODEL = r"models\edf_arrivals_3tasks.xml"
TEST_MODEL = r"models\pyuppaal_test.xml"


# Tell PyUPPAAL where verifyta is installed
pyuppaal.set_verifyta_path(VERIFYTA)

# Create a copy so the original model remains unchanged
shutil.copy(MODEL, TEST_MODEL)

# Load the copied model
model = UModel(TEST_MODEL)

# Change T1 deadline from 5 to 4
model.declaration = model.declaration.replace(
    "const int D[N] = {8, 5, 8};",
    "const int D[N] = {8, 4, 8};"
)

# Save the modified model
model.save()

# Verify the same deadline-miss property
model.queries = [
    "A[] not (T0.Missed || T1.Missed || T2.Missed)"
]

result = model.verify()

print(result)

trace = model.easy_verify()

if trace is not None:
    print("\nCounterexample trace:")
    print(trace)