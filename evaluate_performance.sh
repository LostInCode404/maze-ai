# Set testing parameters
test_x[0]=11
test_y[0]=11
test_x[1]=25
test_y[1]=25
test_x[2]=51
test_y[2]=51
test_x[3]=101
test_y[3]=101
test_x[4]=201
test_y[4]=201
test_x[5]=351
test_y[5]=351
test_x[6]=501
test_y[6]=501
test_x[7]=751
test_y[7]=751
test_x[8]=1001
test_y[8]=1001

# Initialize variables
data_file="data.txt"
limit=8

# Empty data file to save plots
truncate -s 0 ${data_file}

# Test maze generation time
echo "Testing maze generation time:"
for i in `seq 0 ${limit}`;
    do
    	generate[i]=$( { /usr/bin/time -f "%e" python performance.py --do=generate --x=${test_x[i]} --y=${test_y[i]};} 2>&1 )
    	echo "Size: ${test_x[i]}x${test_y[i]} Time: ${generate[i]}"
    	echo "generate ${test_x[i]}x${test_y[i]} ${generate[i]}" >> ${data_file}
    done  

# Test maze solving time
echo "Testing maze solving time(including optimizer time):"
for i in `seq 0 ${limit}`;
    do
    	python performance.py --do=generate --x=${test_x[i]} --y=${test_y[i]} --save=saved_grid.pickle;
    	solve[i]=$( { /usr/bin/time -f "%e" python performance.py --do=solve --file=saved_grid.pickle;} 2>&1 )
    	echo "Size: ${test_x[i]}x${test_y[i]} Time: ${solve[i]}"
    	echo "solve ${test_x[i]}x${test_y[i]} ${solve[i]}" >> ${data_file}
    done  

# Plot results
python performance.py --do=plot_performance --file=${data_file}

# Remove all compiled python files
echo "Cleaning up..."
rm -rf *.pyc
rm -rf *.pickle
