port="7272"
cd app/
python3 scripts/update.py &
flask --app app run -p $port
cd ..
