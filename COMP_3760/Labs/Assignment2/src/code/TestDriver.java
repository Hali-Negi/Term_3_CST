import java.util.ArrayList;

/**
 * Test driver for Lab2.
 */
public class TestDriver
{

    public static void main(String[] args)
    {
        Lab2 lab = new Lab2();

        // Test N = 1 (expected: 3 sequences)
        System.out.println("=== Testing N=1 ===");
        ArrayList<String> result1 = lab.generatePalindromeSequences(1);
        System.out.println("Count: " + result1.size() + " (expected: 3)");
        System.out.println("Sequences: " + result1);
        System.out.println();

        // Test N = 2 (expected: 3 sequences)
        System.out.println("=== Testing N=2 ===");
        ArrayList<String> result2 = lab.generatePalindromeSequences(2);
        System.out.println("Count: " + result2.size() + " (expected: 3)");
        System.out.println("Sequences: " + result2);
        System.out.println();

        // Test N = 3 (expected: 9 sequences)
        System.out.println("=== Testing N=3 ===");
        ArrayList<String> result3 = lab.generatePalindromeSequences(3);
        System.out.println("Count: " + result3.size() + " (expected: 9)");
        System.out.println("Sequences: " + result3);
        System.out.println();

        // Test N = 4 (expected: 9 sequences)
        System.out.println("=== Testing N=4 ===");
        ArrayList<String> result4 = lab.generatePalindromeSequences(4);
        System.out.println("Count: " + result4.size() + " (expected: 9)");
        System.out.println("Sequences: " + result4);
        System.out.println();

        // Test N = 5 (expected: 27 sequences)
        System.out.println("=== Testing N=5 ===");
        ArrayList<String> result5 = lab.generatePalindromeSequences(5);
        System.out.println("Count: " + result5.size() + " (expected: 27)");
        System.out.println("Sequences: " + result5);
    }
}