**Matches using extended regex**

grep -E Perl
- "Perl"

grep -E Pe*r*l
- "Perl"
- "Pl"
- "Pel"
- "Peel" (for however many e's - same for "r") 

grep -E Full-stop.
- "Full-stop" + any character after

grep -E [1-9][0-9][0-9][0-9]
grep -E [1-9][0-9]{3}
- these do the same thing!

**Useful grep options**
-E - Extended regular expressions
-F - Full string matching
-G - default mode

-i - ignore alphabetical case
-v - invert matches
-n - precede matching lines with line number
-c - output the _count_ of the matches only
-o - only output matching patterns, not whole lines