import java.math.BigInteger;

/**
 *
 * COMP 3760 – Lab 6: Dynamic Programming
 * <p>
 * Student Name: Hali Imanpanah
 * Student ID: A01424306
 * <p>
 * Description:
 * This program calculates SW(m,n) using recursion and dynamic programming.
 * The DP method is faster because it stores and reuses results.
 * Bonus Donut 1: SW_Big uses BigInteger to compute large values like SW(37,37).
 */

public class Lab6
{
    public long SW_Recursive(int m,
                             int n)
    {
        if (m == 0 ||
            n == 0)
        {
            return 1;
        }

        return SW_Recursive(m - 1, n) +
            SW_Recursive(m, n - 1);

    }

    public void RunRecursive(int low,
                             int high)
    {
        for (int i = low; i <= high; i++)
        {
            long start = System.currentTimeMillis();
            long result = SW_Recursive(i, i);
            long end = System.currentTimeMillis();
            long time = end - start;
            System.out.println("SW_Recursive(" + i + "," + i + ") = " +
                                   result + ", time is " + time + " ms");

        }


    }

    public long SW_DynamicProg(int m,
                               int n)
    {
        long[][] dp = new long[m + 1][n + 1];

        for (int i = 0; i <= m; i++)
        {
            dp[i][0] = 1;
        }

        for (int j = 0; j <= n; j++)
        {
            dp[0][j] = 1;
        }
        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m][n];
    }

    public void RunDynamicProg(int low,
                               int high)
    {
        for (int i = low; i <= high; i++)
        {
            long start = System.currentTimeMillis();
            long result = SW_DynamicProg(i, i);
            long end = System.currentTimeMillis();
            long time = end - start;
            System.out.println("SW_DynamicProg(" + i + "," + i + ") = " +
                                   result + ", time is " + time + " ms");
        }

    }


    // Donut 1 bonus method
    public BigInteger SW_Big(int m,
                             int n)
    {
        BigInteger[][] dp = new BigInteger[m + 1][n + 1];

        for (int i = 0; i <= m; i++)
        {
            dp[i][0] = BigInteger.ONE;
        }

        for (int j = 0; j <= n; j++)
        {
            dp[0][j] = BigInteger.ONE;
        }

        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                dp[i][j] = dp[i - 1][j].add(dp[i][j - 1]);
            }
        }

        return dp[m][n];
    }

}


