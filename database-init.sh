#!/bin/bash
python3 scripts/init_db.py
echo "Database initialized."
python3 scripts/update.py
echo "Database updated with initial data."
