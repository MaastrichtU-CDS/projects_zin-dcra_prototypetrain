#Run the primary master algorithm 
echo "starting master 1" 
cp ./test/master1/input.txt /opt/input.txt
cp ./test/master1/completed-client-tasks.json /opt/completed-client-tasks.json
python3 ./src/demoMasterAlgorithm.py
echo "the tasks created are: "
cat /opt/new-client-tasks.json
rm -f /opt/input.txt
rm -f /opt/output.txt
rm -f /opt/completed-client-tasks.json
rm -f /opt/new-client-tasks.json
echo "\n\n"

#Run the secondary master algorithm 
echo "starting master 2" 
cp ./test/master2/input.txt /opt/input.txt
cp ./test/master2/completed-client-tasks.json /opt/completed-client-tasks.json
python3 ./src/demoMasterAlgorithm.py
echo "the output of the station algoritm is: "
cat /opt/output.txt
rm -f /opt/input.txt
rm -f /opt/output.txt
rm -f /opt/completed-client-tasks.json
rm -f /opt/new-client-tasks.json
echo "\n\n"


#Run the station algorithm
echo "starting station" 
cp ./test/station/input.txt /opt/input.txt
sudo python3 ./src/demoStationAlgorithm.py
echo "the output of the station algoritm is: "
cat /opt/output.txt
rm -f /opt/input.txt
rm -f /opt/output.txt
echo "\n\n"