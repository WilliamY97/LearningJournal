"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. You have to paint all the houses such that no 
two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0]
is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so
on... Find the minimum cost to paint all houses.

SOLUTION: This is a introductory dynamic programming question. What we do is find the cost of painting a house based off
the sum of painting it that color + the minimum of the paint color required to paint the house before it. The reason being
is that the color we paint a house is dependant on the fact that the house before it can't be painted the same color. We are
essentially identifying all optimal ways (we always choose min of prev colors) of painting houses and then find the one that
has the minimal cost.

F holds the costs of the house before and the res holds the costs of the present house
"""

class Solution(object):
    def minCost(self, costs):
        if not costs: return 0
        
        F = costs[0][:]
        res = [0,0,0]
        
        for i in range(1, len(costs)):
            res[0] = min(F[1],F[2]) + costs[i][0]
            res[1] = min(F[0],F[2]) + costs[i][1]
            res[2] = min(F[0],F[1]) + costs[i][2]
            F = res[:]
        
        return min(F)

#Java Way without any additional space AKA Viterbi Algorithm

public class Solution {
    public int minCost(int[][] costs) {
        int len = costs.length;
        if(len==0) return 0;
        for(int i=1; i<len; i++){
            costs[i][0] += Math.min(costs[i-1][1], costs[i-1][2]);
            costs[i][1] += Math.min(costs[i-1][0], costs[i-1][2]);
            costs[i][2] += Math.min(costs[i-1][0], costs[i-1][1]);
        }
        return Math.min(costs[len-1][0], Math.min(costs[len-1][1], costs[len-1][2]));
    }
}
