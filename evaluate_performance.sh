# Some general test sizes
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
test_x[5]=301
test_y[5]=301
test_x[6]=401
test_y[6]=401
test_x[7]=501
test_y[7]=501
test_x[8]=751
test_y[8]=751
test_x[9]=1001
test_y[9]=1001

# Linear in grid edge length
# test_x[0]=101
# test_y[0]=101
# test_x[1]=201
# test_y[1]=201
# test_x[2]=301
# test_y[2]=301
# test_x[3]=401
# test_y[3]=401
# test_x[4]=501
# test_y[4]=501
# test_x[5]=601
# test_y[5]=601
# test_x[6]=701
# test_y[6]=701
# test_x[7]=801
# test_y[7]=801
# test_x[8]=901
# test_y[8]=901
# test_x[9]=1001
# test_y[9]=1001

# Linear in grid size(area or number of cells)
# test_x[0]=315
# test_y[0]=315
# test_x[1]=447
# test_y[1]=447
# test_x[2]=547
# test_y[2]=547
# test_x[3]=633
# test_y[3]=633
# test_x[4]=707
# test_y[4]=707
# test_x[5]=773
# test_y[5]=773
# test_x[6]=835
# test_y[6]=835
# test_x[7]=893
# test_y[7]=893
# test_x[8]=947
# test_y[8]=947
# test_x[9]=1001
# test_y[9]=1001


# Initialize variables
data_file="data.txt"
limit=9

# Empty data file to save plots
truncate -s 0 ${data_file}

# Test maze generation time
echo "Testing maze generation time:"
for i in `seq 0 ${limit}`
    do
    	generate[i]=$( { /usr/bin/time -f "%e" python performance.py --do=generate --x=${test_x[i]} --y=${test_y[i]};} 2>&1 )
    	echo "Size: ${test_x[i]}x${test_y[i]} Time: ${generate[i]}"
    	echo "generate ${test_x[i]}x${test_y[i]} ${generate[i]}" >> ${data_file}
    done  

# Test maze solving time
echo "Testing maze solving time(including optimizer time):"
for i in `seq 0 ${limit}`
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
