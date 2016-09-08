# PoissonBarrel - The Statistical Analyzer

## Capabilties
There are three supported types of data: frequency, ordinal, and interval. Not
all data types support all of the following capabilities.

### Mean ([Reference](https://en.wikipedia.org/wiki/Mean))
#### Arithmetic mean (AM)
The arithmetic mean (or simply "mean") is the sum of the sampled values divided
by the number of items in the sample.

For example, the arithmetic mean of five values: 4, 36, 45, 50, 75 is:

    (4 + 36 + 45 + 50 + 75)/5 = 210/5 = 42

In terms of Python, this is simply the following:

    xs = [4, 36, 45, 50, 75]
    am = sum(xs)/len(xs)

#### Geometric mean (GM)
The geometric mean is an average that is useful for sets of positive numbers
that are interpreted according to their product and not their sum (as is the
case with the arithmetic mean) e.g. rates of growth.

For example, the geometric mean of five values: 4, 36, 45, 50, 75 is:

    (4 * 36 * 45 * 50 * 75)**(1/5) = 30

In terms of Python, this is simply the following:

    from functools import reduce
    from operator import mul

    xs = [4, 36, 45, 50, 75]
    gm = reduce(mul, xs, 1)**(1.0/len(xs))

#### Harmonic mean (HM)
The harmonic mean is an average which is useful for sets of numbers which are
defined in relation to some unit, for example speed (distance per unit of
time).

For example, the harmonic mean of the five values: 4, 36, 45, 50, 75 is:

    5/(1/4 + 1/36 + 1/45 + 1/50 + 1/75) = 5/(1/3) = 15

In terms of Python, this is simply the following:

    xs = [4, 36, 45, 50, 75]
    hm = len(xs)/sum([1.0/x for x in xs])

### Median
The median is the middle value(s) of a sorted set of values. The median can
be one or two values depending on whether the number of values within the
data set is even or odd.

Computing the median in python:
    
    def median( dataList ):
        
        sortedSet = sorted( dataList )
        
        n = len( sortedSet )
        midIndex = n // 2
        
        if n & 1:
            return sortedSet[ midIndex ]
            
        else:
            med1 = sortedSet[ midIndex - 1 ]
            med2 = sortedSet[ midIndex ]
            
            if med1 == med2:
                return med1
                
            else:
                return ( med1, med2 )
                
Example calls to median:

    >>> median( [ 8, 3, 5 ] )
    5
    >>> median( [ 9, 4, 6, 6 ] )
    6
    >>> median( [ 9, 8, 7, 6 ] )
    (7, 8)
            
### Mode
The mode is the value(s) that most frequently occurs within a data set.
Python Example:
    
    def mode( dataList ):
        
        freqDict = {} 
        modeList = []
        maxFreq = 0

        for val in dataList:

            if val in freqDict:
                freqDict[ val ] += 1

            else:
                freqDict[ val ] = 1

        for val, freq in freqDict.items():

            if maxFreq < freq:
                modeList.clear()
                modeList.append( val )
                maxFreq = freq

            elif maxFreq == freq:
                modeList.append( val )

        return modeList
        
Calling mode() in python:

    >>> mode( [ 9, 9, 8, 8, 8, 10, 11, 15 ] )
    [8]
    >>> mode( [ 1, 1, 2, 3, 3, 5 ] )
    [1, 3]
    
### Standard Deviation
### Variance
### Coefficent of Variance
### Percentiles
### Probability Distribution
A (discrete) probability distribution is a listing of events(values) along with the 
corresponding probability of the event occurring. The probability of each event 
is computed by the frequency of the event in the data set.

Python Example:
    
    #helper function for sorting tuples
    def getKey( tup ):
        return tup[ 0 ]

    def probDist( dataList ):

        probDict = {}
        ONE_OVER_N = 1.0 / len( dataList )

        for val in dataList:

            if val in probDict:
                probDict[ val ] += ONE_OVER_N

            else:
                probDict[ val ] = ONE_OVER_N
                
        return sorted( probDict.items(), key = getKey )
        
        
Calling probDist() from python:
   
    >>> dist = probDist( [ 1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 9 ] )
    >>> for e, p in dist:
	        print( 'Event:', e, 'Probability', p )

    Event: 1 Probability 0.16666666666666666
    Event: 2 Probability 0.08333333333333333
    Event: 3 Probability 0.08333333333333333
    Event: 4 Probability 0.25
    Event: 5 Probability 0.08333333333333333
    Event: 6 Probability 0.08333333333333333
    Event: 7 Probability 0.16666666666666666
    Event: 9 Probability 0.08333333333333333

### Least Square Line
### Chi Square
### Correlation Coefficent
### Sign Test
### Rank Sum Test
### Spearman Rank Correlation Coefficent
