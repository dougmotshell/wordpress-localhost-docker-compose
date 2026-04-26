# WordPress Localhost Docker Compose

This project provides a ready-to-use Docker Compose setup for running WordPress, MySQL, and phpMyAdmin locally. It uses environment variables for easy configuration and a Python script to generate the final `docker-compose.yml` file from a template.

## Features
- **WordPress**: Latest version, easily configurable.
- **MySQL**: Customizable database settings.
- **phpMyAdmin**: For database management.
- **Environment-based configuration**: All settings are managed via a `.env` file.
- **Automatic compose file generation**: The `compose_generator.py` script replaces variables in the template with values from `.env`.

## Project Structure
```
.
├── tools/
│   ├── .env                  # Environment variables for the stack
│   ├── compose_generator.py  # Python script to generate docker-compose.yml
│   ├── docker-compose.template.yml # Template file with variables
│   ├── run                   # Bash script to run the generator
│   └── .venv/                # Python virtual environment (not versioned)
├── docker-compose.yml        # Generated file (should not be versioned)
└── README.md                 # This file
```

## Usage

1. **Clone the repository**
2. **Configure environment variables**
   - Edit `tools/.env` to set your desired values.
3. **Generate the docker-compose file**
   - Run the generator script:
     ```sh
     ./tools/run
     ```
   - This will create or update `docker-compose.yml` in the project root.
4. **Start the stack**
   - Run:
     ```sh
     docker-compose up -d
     ```

## Requirements
- Docker and Docker Compose
- Python 3.7+

## Notes
- The `docker-compose.yml` file is generated and should not be edited directly.
- The `.venv` folder is for the Python virtual environment and should not be versioned.
- If you change `.env` or the template, re-run `./tools/run` to update the compose file.

## License
MIT
