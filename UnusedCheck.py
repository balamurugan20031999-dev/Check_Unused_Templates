import os
import time

print('Execution Starts!!!!!')
# Start timer
start_time = time.perf_counter()

templates_dir = r"C:\Users\balamurugan.appanraj\PycharmProjects\git\UnusedTemplate\sites\templates"
project_dir = r"C:\Users\balamurugan.appanraj\PycharmProjects\git\UnusedTemplate"

templates = []

for root, dirs, files in os.walk(templates_dir):
    for file in files:
        if file.endswith(".html"):
            templates.append(file)

for template in templates:
    found = False

    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith((".py", ".html")):
                filepath = os.path.join(root, file)

                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        if template in f.read():
                            found = True
                            break
                except Exception:
                    pass

        if found:
            break

    if not found:
        print("Possibly unused:", template)

# Stop timer
end_time = time.perf_counter()

print(f"\nStart Time: {start_time:.6f}")
print(f"End Time:   {end_time:.6f}")
print(f"Execution Time: {end_time - start_time:.2f} seconds")
print("Execution Ends!!!!!")