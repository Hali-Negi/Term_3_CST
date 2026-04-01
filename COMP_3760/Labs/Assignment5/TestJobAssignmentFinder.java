public class TestJobAssignmentFinder
{
    public static void main(String[] args) throws Exception
    {
        JobAssignmentFinder finder = new JobAssignmentFinder();
        finder.readDataFile("donutdata.txt");

        System.out.println(finder.getGreedyAssignment());
        System.out.println(finder.greedyAssignmentTotalValue());


    }
}
