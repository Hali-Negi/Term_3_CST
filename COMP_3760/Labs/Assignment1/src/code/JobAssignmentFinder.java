import java.io.*;
import java.util.*;

/**
 * <p>
 * JobAssignmentFinder - Solves the job assignment problem using brute force.
 * Finds the assignment of N people to N jobs that maximizes total benefit.
 * </p>
 * Author: Hali Imanpanah
 * Student ID: A01424306
 */
public class JobAssignmentFinder
{

    // Instance variables
    private int[][] benefitMatrix;             // The N×N benefit matrix
    private int n;                             // Size of the matrix
    private ArrayList<Integer> maxAssignment;  // Best assignment found
    private int maxValue;                      // Value of best assignment

    /**
     * Constructor - initializes the JobAssignmentFinder with no data loaded.
     */
    public JobAssignmentFinder()
    {
        this.n             = -1;  // -1 means no data loaded yet
        this.benefitMatrix = null;
        this.maxAssignment = null;
        this.maxValue      = 0;
    }

    /**
     * Reads a data file and initializes the benefit matrix.
     *
     * @param filename The full path to the data file
     */
    public void readDataFile(String filename)
    {
        try
        {
            // Create a Scanner to read the file
            Scanner scanner = new Scanner(new File(filename));

            n = scanner.nextInt();

            // Create N×N matrix
            benefitMatrix = new int[n][n];

            // Read N rows, each with N numbers
            for (int row = 0; row < n; row++)
            {
                for (int col = 0; col < n; col++)
                {
                    benefitMatrix[row][col] = scanner.nextInt();
                }
            }


            scanner.close();

            // Reset max assignment
            maxAssignment = null;
            maxValue      = 0;

        }
        catch (FileNotFoundException e)
        {
            // Do nothing - just file not found
        }
    }

    /**
     * Returns the size of the benefit matrix (N).
     *
     * @return N if data is loaded, -1 if no data loaded yet
     */
    public int getInputSize()
    {
        return n;
    }

    /**
     * Returns the benefit matrix as a 2D array.
     *
     * @return The N×N benefit matrix
     */
    public int[][] getBenefitMatrix()
    {
        return benefitMatrix;
    }

    /**
     * Returns the benefit for assigning a specific person to a specific job.
     *
     * @param person The person number (0 to N-1)
     * @param job    The job number (0 to N-1)
     * @return The benefit value for that assignment
     */
    public int getBenefit(int person,
                          int job)
    {
        return benefitMatrix[person][job];
    }

    /**
     * Recursive decrease-and-conquer algorithm to generate a list of all
     * permutations of the numbers 0..N-1.
     *
     * @param N The size of permutations to generate
     * @return ArrayList containing all permutations
     */
    private ArrayList<ArrayList<Integer>> getPermutations(int N)
    {
        ArrayList<ArrayList<Integer>> results = new ArrayList<ArrayList<Integer>>();

        if (N == 0)
        {
            ArrayList<Integer> emptyList = new ArrayList<Integer>();
            results.add(emptyList);

        }
        else if (N == 1)
        {
            ArrayList<Integer> singleton = new ArrayList<Integer>();
            singleton.add(0);
            results.add(singleton);

        }
        else
        {
            ArrayList<ArrayList<Integer>> smallList = getPermutations(N - 1);

            for (ArrayList<Integer> perm : smallList)
            {
                for (int i = 0; i < perm.size(); i++)
                {
                    ArrayList<Integer> newPerm = (ArrayList<Integer>) perm.clone();
                    newPerm.add(i, N - 1);
                    results.add(newPerm);
                }

                ArrayList<Integer> newPerm = (ArrayList<Integer>) perm.clone();
                newPerm.add(N - 1);
                results.add(newPerm);
            }
        }

        return results;
    }

    /**
     * Calculates the total benefit value of a given job assignment.
     *
     * @param assignment A permutation representing person-to-job assignment
     * @return The total benefit value
     */
    private int calculateAssignmentValue(ArrayList<Integer> assignment)
    {
        int total = 0;

        // For each person, add the benefit of their assigned job
        for (int person = 0; person < assignment.size(); person++)
        {
            int job = assignment.get(person);  // Which job is this person assigned to?
            total += benefitMatrix[person][job];  // Add the benefit
        }

        return total;
    }

    /**
     * Finds the job assignment with the maximum total benefit.
     * Uses brute force (checks all possible permutations).
     *
     * @return The permutation representing the best assignment
     */
    public ArrayList<Integer> getMaxAssignment()
    {
        // If we already found the answer, return it
        if (maxAssignment != null)
        {
            return maxAssignment;
        }

        // Generate all possible assignments
        ArrayList<ArrayList<Integer>> allPermutations = getPermutations(n);

        // Check each permutation & find the best one
        for (ArrayList<Integer> assignment : allPermutations)
        {
            int value = calculateAssignmentValue(assignment);

            // Is this better than our current best???
            if (value > maxValue)
            {
                maxValue      = value;
                maxAssignment = assignment;
            }
        }

        return maxAssignment;
    }

    /**
     * Returns the total benefit value of the maximum assignment.
     *
     * @return The total value of the best assignment
     */
    public int getMaxAssignmentTotalValue()
    {
        // it Makes sure we've found the max assignment first
        if (maxAssignment == null)
        {
            getMaxAssignment();
        }

        return maxValue;
    }

    /**
     * Returns a string representation of the benefit matrix.
     *
     * @return Formatted string showing the matrix
     */
    public String benefitMatrixToString()
    {
        StringBuilder sb = new StringBuilder();

        sb.append("Benefit Matrix (" + n + "x" + n + "):\n");

        // Loop through each row
        for (int row = 0; row < n; row++)
        {
            // Loop through each column
            for (int col = 0; col < n; col++)
            {
                sb.append(benefitMatrix[row][col] + "\t");
            }
            sb.append("\n");
        }

        return sb.toString();
    }

}