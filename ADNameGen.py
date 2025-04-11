#/usr/bin/env   python3

import argparse

GREEN = "\033[92m"
RESET = "\033[0m"
MAGNETA = "\033[95m"

banner = rf"""
{MAGNETA}--------------------------------
 ADNameGen - AD Name Combinator

           by @Retxus
--------------------------------{RESET}
"""

def generate_combs(full_name, capitalize=False):
    try:
        name, lastname = full_name.lower().split()
    except ValueError:
        return []

    if capitalize:
        name = name.capitalize()
        lastname = lastname.capitalize()

    initial_name = name[0]
    initial_lastname = lastname[0]

    combinations = [
        f"{name}",
        f"{lastname}",
        f"{name}{lastname}",
        f"{initial_name}{lastname}",
        f"{name}{initial_lastname}",
        f"{name}.{lastname}",
        f"{initial_lastname}.{lastname}",
        f"{lastname}.{name}",
        f"{lastname}.{initial_name}",
    ]
    
    return combinations

def main():
    parser = argparse.ArgumentParser(description="Common user name generator in AD environments.")
    parser.add_argument("-i", "--input", required=True, help="File with full names.")
    parser.add_argument("-o", "--output", required=True, help="File to save the combinations.")
    parser.add_argument("--capitalize", action="store_true", help="Capitalize the first letter of name and lastname.")
    
    args = parser.parse_args()

    print(banner)
    print(f"Reading names from: {GREEN}{args.input}{RESET}")

    with open(args.input, 'r') as f:
            names = [line.strip() for line in f.readlines() if line.strip()]

    result = []
    
    for full_name in names:
        result.extend(generate_combs(full_name, capitalize=args.capitalize))

    result = sorted(set(result))


    with open(args.output, 'w') as f:
        for r in result:
            f.write(r + "\n")

    print(f"\n[*] Generates {GREEN}{len(result)}{RESET} combinations and saved in {GREEN}'{args.output}'{RESET}.")

if __name__ == "__main__":
    main()
