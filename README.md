# bayes_network

This project is part of a programming assignment for the Artificial Intelligence course taught at Trinity College-Hartford.

We were tasked to implement a Bayesian network with two sampling algorithms. I choce prior sampling and rejection sampling.

## Assignment Specifications

"On Patriots’ Day (a holiday observed by several states in the US, including Massachusetts, on
the third Monday in April), the Tortoise and the Hare have their annual footrace in a small
town in eastern Massachusetts. On the morning of the race, either the short or the long
course is chosen at random. Another major factor is the weather, which can be cold and wet,
very hot, or very nice. The short course favors the Hare. The Hare does not like cold and wet
weather, frequently leaving the course and taking shelter. The Tortoise does not like the heat,
although on the long course there are some muddy puddles that it can use to cool off.

Implement this network with the probabilities indicated below (CODED IN). You will need to implement
two algorithms for sampling:  
• PRIOR-SAMPLE, which is run without any evidence to generate a sample for the general
case. Run many times, it should give a probability distribution for the Hare’s winning.  
• Your choice of REJECTION SAMPLING or LIKELIHOOD WEIGHTING, which are run in the presence
of evidence.  
Using these two algorithms, generate answers to the following three queries:  
1. In general, how likely is the Hare to win?  
2. Given that is it coldWet, how likely is the Hare to win?  
3. Given that the Tortoise won on the short course, what is the probability distribution for
the Weather?  
Rather than interpreting queries at the keyboard, these may be hard-coded with a menu  
selection to run one of them."


## Compilation & Input

Compilation should be: "python3 bayes_final.py" at the command line.  

Input: You will br prompted with whether or not you want to specify sample space (default is 100000), please enter 'N' if that is fine, or 'Y' to specify sample size.  
Then, simply input your desired sample and enter 1-4 based on the query you would like to run.  

## General Comments:
All probabilites were generated.
