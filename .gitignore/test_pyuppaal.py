import pyuppaal
from pyuppaal import UModel


VERIFYTA = r'"C:\Program Files\UPPAAL-5.0.0\app\bin\verifyta.exe"'
MODEL = r"models\edf_arrivals_3tasks.xml"

pyuppaal.set_verifyta_path(VERIFYTA)

model = UModel(MODEL)

print(model.declaration)

print("Templates and locations:")

for template in model.templates:
    print("\nTemplate:", template.name)

    for location in template.locations:
        print("  Location:", location.name)

model.queries = [
    "A[] not (T0.Missed || T1.Missed || T2.Missed)"
]

result = model.verify()

print(result)