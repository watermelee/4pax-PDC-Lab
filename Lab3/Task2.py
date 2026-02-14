from concurrent.futures import ProcessPoolExecutor
import os

# Deduction rates
SSS_RATE = 0.045
PHILHEALTH_RATE = 0.025
PAGIBIG_RATE = 0.02
TAX_RATE = 0.10

# Employees data
employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]


def compute_payroll(employee):
    name, salary = employee

    sss = salary * SSS_RATE
    philhealth = salary * PHILHEALTH_RATE
    pagibig = salary * PAGIBIG_RATE
    tax = salary * TAX_RATE

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    return {
        "name": name,
        "salary": salary,
        "total_deduction": total_deduction,
        "net_salary": net_salary,
        "process_id": os.getpid()
    }


if __name__ == "__main__":
    print("=== Data Parallelism Payroll System ===\n")

    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)
    
    for result in results:
        print(f"Employee: {result['name']}")
        print(f"  Salary: {result['salary']:.2f}")
        print(f"  Total Deduction: {result['total_deduction']:.2f}")
        print(f"  Net Salary: {result['net_salary']:.2f}")
        print(f"  Process ID: {result['process_id']}\n")
