import java.util.ArrayList;

/**
 * <p>
 * Lab2 - Generates palindrome sequences using decrease-and-conquer.
 * </p>
 * Author: Hali Imanpanah
 * Student ID: A01424306
 */
public class Lab2
{

    /**
     * Generates all palindromic sequences of the given length using A, B, C.
     * Uses decrease-and-conquer (decrease by 2) pattern.
     *
     * @param n The length of each palindrome sequence
     * @return ArrayList containing all palindromic sequences of length n
     */
    public ArrayList<String> generatePalindromeSequences(int n)
    {
        ArrayList<String> result = new ArrayList<>();

        // Base case 1: length 1
        if (n == 1)
        {
            result.add("A");
            result.add("B");
            result.add("C");
            return result;
        }

        // Base case 2: length 2
        if (n == 2)
        {
            result.add("AA");
            result.add("BB");
            result.add("CC");
            return result;
        }

        // General case: decrease by 2
        // Get all palindromes of length n-2
        ArrayList<String> smaller = generatePalindromeSequences(n - 2);

        // Wrap each smaller palindrome with A, B, C on both sides
        for (String palindrome : smaller)
        {
            result.add("A" + palindrome + "A");
            result.add("B" + palindrome + "B");
            result.add("C" + palindrome + "C");
        }

        return result;
    }
}