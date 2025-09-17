# Calculates the gravity in the Pendulum formula by taking length and period as the inputs.

length = float(input("Length: "))
period = float(input("Period: "))

Result = (4*(3.14**2))*(length/(period**2))
print(f"Gravity = {Result}")
