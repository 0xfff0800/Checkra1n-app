#!/bin/bash

# Define colors
YELLOW='\033[1;33m'
GREEN='\033[1;32m'
RED='\033[1;31m'
MAGENTA='\033[1;35m'
NC='\033[0m'

# Check if Homebrew is already installed
echo -e "${YELLOW}Checking for Homebrew...${NC}"
if command -v brew >/dev/null 2>&1; then
    echo -e "${GREEN}Homebrew is already installed${NC}"
else
    echo -e "${YELLOW}Installing Homebrew...${NC}"

    # Run Homebrew installation script
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    echo -e "${GREEN}Homebrew installation finished${NC}"
fi

# Install Python and pip
echo -e "${YELLOW}Checking and Installing Python and pip...${NC}"
brew install python

if command -v pip3 >/dev/null 2>&1; then
    echo -e "${GREEN}pip3 is already installed${NC}"
else
    echo -e "${RED}Error: pip3 not found after installing Python${NC}"
    exit 1
fi

# Save Python script to check and install dependencies
echo -e "${YELLOW}Checking and installing project dependencies...${NC}"
cat > check_and_install_reqs.py << 'EOF'
import sys
import pkg_resources
from subprocess import call
from termcolor import colored

requirements = [
    'Flask',
    'Flask-Sijax',
    'mimerender',
    'pymongo',
    'six',
    'bcrypt',
    'termcolor',
    'requests',
    'urllib3',  # this library provides urlretrieve
    'tqdm',
]

for req in requirements:
    try:
        pkg_resources.get_distribution(req)
        print(colored(f"{req} is already installed", 'magenta'))
    except pkg_resources.DistributionNotFound:
        print(colored(f"Installing {req}...", 'yellow'))
        call([sys.executable, '-m', 'pip', 'install', req])
EOF

python3 -m pip install termcolor
python3 check_and_install_reqs.py
rm check_and_install_reqs.py

echo -e "${MAGENTA}Finished checking and installing project dependencies${NC}"
echo -e "${MAGENTA}You are all set!${NC}"
