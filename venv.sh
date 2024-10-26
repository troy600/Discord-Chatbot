#!/usr/bin/bash
exec /usr/bin/python -m venv ./venv
echo "source ./venv/bin/activate" >> activate.sh
echo "use bash activate.sh to activate the venv"
