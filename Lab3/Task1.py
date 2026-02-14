import threading
from concurrent.futures import ThreadPoolExecutor

salary = 75000

def sss(s):
    amount = s * 0.045  
    print(f"[{threading.current_thread().name}] SSS Deduction: {amount:.2f}")
    return amount

def philhealth(s):
    amount = s * 0.035  # 3.5% of salary
    print(f"[{threading.current_thread().name}] PhilHealth Deduction: {amount:.2f}")
    return amount

def pagibig(s):
    amount = s * 0.02  # 2% of salary
    print(f"[{threading.current_thread().name}] Pag-IBIG Deduction: {amount:.2f}")
    return amount

def tax(s):
    amount = s * 0.15  # 15% of salary
    print(f"[{threading.current_thread().name}] Withholding Tax Deduction: {amount:.2f}")
    return amount

print("=== Concurrent Payroll Deduction Processing ===")
print(f"Employee Salary: {salary:.2f}\n")

with ThreadPoolExecutor(max_workers=4) as executor:

    futures = [
        executor.submit(sss, salary),
        executor.submit(philhealth, salary),
        executor.submit(pagibig, salary),
        executor.submit(tax, salary)
    ]


    results = [future.result() for future in futures]


total_deduction = sum(results)


print("\n=== Deduction Summary ===")
print(f"Total Deduction: {total_deduction:.2f}")
print(f"Net Salary: {salary - total_deduction:.2f}")