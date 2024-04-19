# Min blanket


In this problem, we have a rectangular hall with a length of 106 meters and a width of 1 meter.
The hall represents the home of Aunt Marjan. It’s raining heavily in the forest, and animals are seeking refuge in Aunt Marjan’s house. There are n animals entering the house from different parts of the forest. Each animal sleeps at a specific distance from the entrance. The animals are so slender that their width is negligible.
Aunt Marjan wants to cover all the animals with the minimum number of blankets. 

The blankets are rectangular with a length of d meters and a width of 1 meter. The blankets can be placed parallel to the width of the hall.
Given the positions where each animal sleeps, your task is to determine the minimum number of blankets Aunt Marjan needs to cover all the animals.

The animals’ sleeping positions are represented by n natural numbers between 1 and 106.🐶


## Explanation

**Key Concepts**

**Sorting**: The code sorts the animal positions in ascending order to facilitate the calculation.

**Iteration**: It iterates over the animal positions to determine where to place blankets based on the distance between animals.

**Blanket Placement**: A new blanket is placed whenever the distance between consecutive animals exceeds the maximum allowed distance d.

## Code Structure
__Function Definition:__ The function minimum_blankets takes n, d, and animal_positions as input parameters.

__Sorting:__ Animal positions are sorted in ascending order.

__Blanket Calculation:__ Blankets are placed based on the distance between animals.
__Result:__ The function returns the total number of blankets needed to cover all animals.
