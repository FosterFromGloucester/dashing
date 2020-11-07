#!/bin/bash -l 
cd /home/pi/dashing/
echo $(date)
echo "Running update to dashboard"
./venv/bin/python dashboard.py >> /home/pi/jobs/dashboard.log 2>&1
echo "Finished update"

