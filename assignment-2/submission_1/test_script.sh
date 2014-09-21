#!/bin/bash
# Place this file, your assignment_2.py file, and sample_data_problem_#.txt files into the same directory
# Navigate to directory containing the above in terminal and type
# bash test_script.sh

for i in `seq 1 6`; do
    python assignment_2.py sample_data_problem_$i.txt > output_problem_$i.txt
    echo "comparing" $i
    diff sample_output_problem_$i.txt output_problem_$i.txt  
done
