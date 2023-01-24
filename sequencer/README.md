# Sequencer

You are given a sequence of numbers which are read from a stream (for example, as user input through
the keyboard). <br>
You cannot store the whole sequence in memory so you should process each number only once without
referring to the previous numbers in the sequence. <br>
Write a function that counts the elements of the sequence that equal the maximum element in the whole
sequence.

#### Notes:

● ✅The solution must use recursion - a solution with loops won’t count <br>
● The last element of the sequence is always zero so use ‘0’ as a marker to stop processing the
sequence <br>
● The sequence has at least one element <br>
● The algorithm must print only once, after 0 has been received and the processing of the stream is
finished <br>

#### Example:

The following stream was received - note the last element ‘0’ that marks the end of the stream and
triggers the end of processing: <br>

    input: 1 5 42 -376 5 19 5 3 42 2 0
    output: (42; 2)

(42; 2) => sequence maximum is ‘42’ and we have two ‘42’s in the sequence

<br>
