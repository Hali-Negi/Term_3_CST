/**
 * COMP 3760 - Lab 3: Fun with Hashing
 * <p>
 * This class simulates inserting String keys into a hash table
 * using three different hash functions (H1, H2, H3).
 * Collision resolution strategy: Closed hashing with linear probing.
 * <p>
 * For each hash function, this simulator counts:
 * - Number of collisions
 * - Number of probes
 * <p>
 *
 * @author Hali Imanpanah
 * Student ID: A01424306
 *
 */
public class HashSimulator
{
    /**
     * Runs the hash simulation using H1, H2, and H3.
     *
     * @param keys      Array of input String keys
     * @param tableSize Size of hash table
     * @return int[6] array containing:
     * [0] H1 collisions
     * [1] H1 probes
     * [2] H2 collisions
     * [3] H2 probes
     * [4] H3 collisions
     * [5] H3 probes
     */

    public int[] runHashSimulation(String[] keys,
                                   int tableSize)
    {
        int[] results = new int[6];

        // Run with H1
        String[] table = new String[tableSize];
        int collisions = 0;
        int probes = 0;

        for (String key : keys)
        {
            int home = H1(key, tableSize);
            int[] cp = insertWithLinearProbing(table, key, home);
            collisions += cp[0];
            probes += cp[1];
        }
        results[0] = collisions;
        results[1] = probes;

        // Run with H2
        table      = new String[tableSize];
        collisions = 0;
        probes     = 0;

        for (String key : keys)
        {
            int home = H2(key, tableSize);
            int[] cp = insertWithLinearProbing(table, key, home);
            collisions += cp[0];
            probes += cp[1];
        }
        results[2] = collisions;
        results[3] = probes;

        // Run with H3
        table      = new String[tableSize];
        collisions = 0;
        probes     = 0;

        for (String key : keys)
        {
            int home = H3(key, tableSize);
            int[] cp = insertWithLinearProbing(table, key, home);
            collisions += cp[0];
            probes += cp[1];
        }
        results[4] = collisions;
        results[5] = probes;

        return results;
    }

    /**
     * H1 Hash Function
     * A = 1, B = 2, ..., Z = 26
     * Returns (sum of letter values) mod HTsize
     */
    public int H1(String name,
                  int HTsize)
    {
        int sum = 0;
        String s = name.toUpperCase();

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);

            if (c >= 'A' && c <= 'Z')
            {
                sum += (c - 'A' + 1); // A=1, B=2, ... Z=26
            }
        }

        return sum % HTsize;
    }

    /**
     * H2 Hash Function (Polynomial using base 26)
     * <p>
     * Formula:
     * sum( letterValue * 26^i ) mod HTsize
     * <p>
     * Uses long to avoid integer overflow.
     */
    public int H2(String name,
                  int HTsize)
    {
        long hash = 0;
        long power = 1; // 26^0

        String s = name.toUpperCase();

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);

            if (c >= 'A' && c <= 'Z')
            {
                int value = c - 'A' + 1; // A=1..Z=26

                // hash += value * 26^i  (but keep it safe)
                hash = (hash + (value * power) % HTsize) % HTsize;

                // update power = 26^(i+1), but keep it small
                power = (power * 26) % HTsize;
            }
        }

        return (int) hash; // already in 0..HTsize-1
    }

    /**
     * H3 Hash Function (Polynomial Rolling Hash - Base 31)
     * <p>
     * This hash multiplies the current hash value by 31
     * and adds the next letter value.
     * <p>
     * hash = (hash * 31 + letterValue) mod HTsize
     * Standard polynomial rolling hash commonly used
     * in string hashing.
     */
    public int H3(String name,
                  int HTsize)
    {
        long hash = 0;
        String s = name.toUpperCase();

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if (c >= 'A' && c <= 'Z')
            {
                int value = c - 'A' + 1;
                hash = (hash * 31 + value) % HTsize;
            }
        }
        return (int) hash;
    }

    /**
     * Inserts a key into the hash table using
     * closed hashing with linear probing.
     * <p>
     * Collision:
     * Counted once if home bucket is occupied.
     * <p>
     * Probes:
     * Counted for each bucket checked AFTER the collision,
     * including the empty bucket found.
     */
    private int[] insertWithLinearProbing(String[] table,
                                          String key,
                                          int startIndex)
    {
        int collisions = 0;
        int probes = 0;

        // If home bucket is empty, place directly (no collision, no probes)
        if (table[startIndex] == null)
        {
            table[startIndex] = key;
            return new int[]{collisions, probes};
        }

        // Otherwise: exactly ONE collision for this key
        collisions++;

        int index = (startIndex + 1) % table.length;

        // Now probe until we find an empty slot
        while (table[index] != null)
        {
            probes++; // counted buckets examined after the collision
            index = (index + 1) % table.length;
        }

        // We examined an empty bucket too (it counts as a probe)
        probes++;

        table[index] = key;
        return new int[]{collisions, probes};
    }
}