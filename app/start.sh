port="7272"
python3 scripts/update.py &
flask --app app run -p $port
