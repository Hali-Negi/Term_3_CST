import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

/**
 * @author Hali Imanpanah
 * Student ID: A01424306
 */

public class Lab3Driver
{
    public static void main(String[] args) throws Exception
    {

        String filename = "5777names.txt";


        // Read all lines (names) from the file
        List<String> lines = Files.readAllLines(Path.of(filename));

        // Convert to plain String[]
        String[] keys = lines.toArray(new String[0]);

        int N = keys.length;

        HashSimulator sim = new HashSimulator();

        int[] sizes = {N, 2 * N, 5 * N, 10 * N, 100 * N};


        for (int size : sizes)
        {
            int[] results = sim.runHashSimulation(keys, size);

            System.out.println("HTsize=" + size);
            System.out.println("H1 collisions=" + results[0] + " probes=" + results[1]);
            System.out.println("H2 collisions=" + results[2] + " probes=" + results[3]);
            System.out.println("H3 collisions=" + results[4] + " probes=" + results[5]);
            System.out.println("----------------------------");
        }
    }
}