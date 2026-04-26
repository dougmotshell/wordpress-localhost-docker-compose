import os
import re
from pathlib import Path


# File paths relative to the script location
SCRIPT_DIR = Path(__file__).parent.resolve()
TEMPLATE_FILE = SCRIPT_DIR / 'docker-compose.template.yml'
ENV_FILE = SCRIPT_DIR / '.env'
OUTPUT_FILE = SCRIPT_DIR.parent / 'docker-compose.yml'


# Function to read variables from .env (removes surrounding quotes from values)
def read_env(env_path):
    env_vars = {}
    if not os.path.exists(env_path):
        print(f"File {env_path} not found.")
        return env_vars
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                value = value.strip()
                # Remove surrounding quotes if present
                if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]
                env_vars[key.strip()] = value
    return env_vars

# Function to substitute variables in the template

# Function to substitute all variable names in the template with their values from .env
def substitute_vars(template, env_vars):
    # Replace all occurrences of each variable name with its value (including in keys, values, and volumes)
    result = template
    for var, value in env_vars.items():
        # Replace all occurrences, not just as a word
        result = result.replace(var, value)
    return result

def main():
    # Read variables from .env
    env_vars = read_env(ENV_FILE)
    if not env_vars:
        print("No variables found in .env. Continuing anyway.")

    # Read template
    if not os.path.exists(TEMPLATE_FILE):
        print(f"File {TEMPLATE_FILE} not found.")
        return
    with open(TEMPLATE_FILE, 'r') as f:
        template_content = f.read()

    # Substitute variables
    output_content = substitute_vars(template_content, env_vars)

    # Write new file
    with open(OUTPUT_FILE, 'w') as f:
        f.write(output_content)
    print(f"File {OUTPUT_FILE} generated successfully.")

if __name__ == '__main__':
    main()
