/**
 * Test driver for JobAssignmentFinder.
 * Tests the brute force job assignment algorithm against known results.
 */
public class TestDriver
{

    public static void main(String[] args)
    {
        JobAssignmentFinder finder = new JobAssignmentFinder();

        // Test before loading any file
        System.out.println("=== Testing before loading file ===");
        System.out.println("Size (should be -1): " + finder.getInputSize());
        System.out.println();

        // Test data0.txt - Expected: [2, 3, 4, 1, 0], Value: 37
        System.out.println("=== Testing data0.txt ===");
        finder.readDataFile("src/data/data0.txt");
        System.out.println("Size: " + finder.getInputSize());
        System.out.println("Max Assignment: " + finder.getMaxAssignment());
        System.out.println("Max Value: " + finder.getMaxAssignmentTotalValue());
        System.out.println();

        // Test data1.txt - Expected: [3, 2, 6, 4, 1, 5, 0], Value: 58
        System.out.println("=== Testing data1.txt ===");
        finder.readDataFile("src/data/data1.txt");
        System.out.println("Size: " + finder.getInputSize());
        System.out.println("Max Assignment: " + finder.getMaxAssignment());
        System.out.println("Max Value: " + finder.getMaxAssignmentTotalValue());
        System.out.println();

        // Test data2.txt - Expected: [5, 0, 9, 2, 4, 3, 7, 6, 8, 1], Value: 8658
        System.out.println("=== Testing data2.txt ===");
        finder.readDataFile("src/data/data2.txt");
        System.out.println("Size: " + finder.getInputSize());
        System.out.println("Max Assignment: " + finder.getMaxAssignment());
        System.out.println("Max Value: " + finder.getMaxAssignmentTotalValue());
        System.out.println();

// Test data3.txt - Expected: [7, 5, 8, 4, 1, 0, 9, 3, 6, 2], Value: 335
        System.out.println("=== Testing data3.txt ===");
        finder.readDataFile("src/data/data3.txt");
        System.out.println("Size: " + finder.getInputSize());
        System.out.println("Max Assignment: " + finder.getMaxAssignment());
        System.out.println("Max Value: " + finder.getMaxAssignmentTotalValue());
        System.out.println();


        // Test data4.txt - Expected: [1, 0, 4, 5, 2, 3], Value: 42
        System.out.println("=== Testing data4.txt ===");
        finder.readDataFile("src/data/data4.txt");
        System.out.println("Size: " + finder.getInputSize());
        System.out.println("Max Assignment: " + finder.getMaxAssignment());
        System.out.println("Max Value: " + finder.getMaxAssignmentTotalValue());
        System.out.println();

        // Test data5.txt - Expected: [2, 1, 4, 8, 6, 7, 3, 0, 5], Value: 74
        System.out.println("=== Testing data5.txt ===");
        finder.readDataFile("src/data/data5.txt");
        System.out.println("Size: " + finder.getInputSize());
        System.out.println("Max Assignment: " + finder.getMaxAssignment());
        System.out.println("Max Value: " + finder.getMaxAssignmentTotalValue());
        System.out.println();

        // Test getBenefitMatrix() and getBenefit()
        System.out.println("=== Testing getBenefitMatrix() and getBenefit() ===");
        int[][] matrix = finder.getBenefitMatrix();
        System.out.println("Matrix[0][0]: " + matrix[0][0]);
        System.out.println("getBenefit(0,0): " + finder.getBenefit(0, 0));
        System.out.println();

        // Test benefitMatrixToString()
        System.out.println("=== Testing benefitMatrixToString() ===");
        System.out.println(finder.benefitMatrixToString());


    }

}