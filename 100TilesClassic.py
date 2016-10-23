import matplotlib.pyplot as plt
import numpy as np


#The logic is your chance to land on a square is the average the chances of getting the previous six numbers. If you know the chance to land on 0 is 1 and anything lower is 0 then you can just run an average over the numbers. It works out to look kind of like an absolute valued harmonic sequence. Anyways here is the code I used to find it
highscore = [0,0,0]
results = [[0 for col in range(1006)]for row in range(3)]
for square_selection in range(0,3):
    results[square_selection][5] = 1 #First values should be 0,0,0,0,1. Represents chance to get -5:0. Makes the logic work
    for sq in range(6,1006):
        chance = 0
        for roll in range(1,7):
            chance = chance + results[square_selection][sq-roll]/6 #The chance is just the average of the last six rolls
        if highscore.count(sq) == 0: #If it is already labeled a highscore for a previous square_selection then give it no value
            results[square_selection][sq] = chance                
    results[square_selection][5] = 0 #Zero out the 0th square -- you cannot select that square
    highscore[square_selection] = results[square_selection].index(max(results[square_selection])) #Save the highscore of this square_selection


# Plot the results:
#Two subplots, unpack the axes array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(np.arange(6,106,1), results[0][6:106],color='red') #The first placement, without any score weighting
ax1.plot(np.arange(6,106,1), results[1][6:106],color='blue') #The second, after the best square has been removed
ax1.plot(np.arange(6,106,1), results[2][6:106],color='green') #the third, after the best two have been removed

ax1.set_title('100 Spaces')
ax2.scatter(np.arange(1,21,1), results[0][6:26],color='red')
ax2.scatter(np.arange(1,21,1), results[1][6:26],color='blue')
ax2.scatter(np.arange(1,21,1), results[2][6:26],color='green')

ax2.set_title('First 20 Spaces')
ax1.set_xlabel('Spaces')
ax2.set_xlabel('Spaces')
ax1.set_ylabel('Chance')
plt.show()
