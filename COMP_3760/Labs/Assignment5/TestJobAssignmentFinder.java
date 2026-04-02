public class TestJobAssignmentFinder
{
    public static void main(String[] args) throws Exception
    {
        JobAssignmentFinder finder = new JobAssignmentFinder();

        String[] files = {"data11.txt", "data12.txt", "data37.txt", "data148.txt", "donutdata.txt"};

        for (String file : files)
        {
            finder.readDataFile(file);

            System.out.println("****** " + file + " ******");

            System.out.println("Main Greedy Assignment:");
            System.out.println(finder.getGreedyAssignment());

            System.out.println("Main Greedy Total:");
            System.out.println(finder.greedyAssignmentTotalValue());

            System.out.println("Problem 1 Assignment (Job -> Person):");
            System.out.println(finder.getGreedyAssignmentByJob());

            System.out.println("Problem 1 Total:");
            System.out.println(finder.greedyAssignmentByJobTotalValue());

            System.out.println("Exhaustive Assignment:");
            System.out.println(finder.getMaxAssignment());

            System.out.println("Exhaustive Total:");
            System.out.println(finder.getMaxAssignmentTotalValue());

            System.out.println("Global Greedy Assignment:");
            System.out.println(finder.getGreedyAssignmentGlobal());

            System.out.println("Global Greedy Total:");
            System.out.println(finder.greedyAssignmentGlobalTotalValue());

            System.out.println();
        }
    }
}
