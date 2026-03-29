package ca.bcit.comp3920;

import java.sql.*;

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Hello World!");

        // MYSQL CONNECTION

        // Load MySQL Driver
        try
        {
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch (ClassNotFoundException e)
        {
            System.out.println("Your MySQL JDBC Driver is not found. Include it in your library path ");
            e.printStackTrace();
        }

        // MySQL connection settings
        final String MYSQL_HOST = "localhost";
        final int MYSQL_PORT = 3306;
        final String MYSQL_DATABASE_NAME = "comp3920Assign1";
        final String MYSQL_USER_NAME = "root";
        final String MYSQL_PASSWORD = "VFX72vfx72!!";

        final String MYSQL_URL = "jdbc:mysql://" + MYSQL_USER_NAME + ":" +
            MYSQL_PASSWORD + "@" + MYSQL_HOST + ":" + MYSQL_PORT + "/" + MYSQL_DATABASE_NAME;

        final Connection connection;
        try
        {
            connection = DriverManager.getConnection(MYSQL_URL);
        }
        catch (SQLException e)
        {
            System.out.println("Connection Failed! Check output console");
            e.printStackTrace();
            return;
        }

        if (connection != null)
        {
            System.out.println("Successfully connected to MySQL! :D");
        }

        // Query and print data from MySQL
        final String SELECT_STATEMENT = """
                                        SELECT address.*, address_type.type
                                        FROM address
                                        JOIN address_type ON address.address_type_id = address_type.address_type_id
                                        """;

        try
        {
            PreparedStatement stmt = connection.prepareStatement(SELECT_STATEMENT,
                                                                 ResultSet.TYPE_SCROLL_INSENSITIVE,
                                                                 ResultSet.CONCUR_READ_ONLY);
            ResultSet resultSet = stmt.executeQuery();
            printResultSet(resultSet);
        }
        catch (SQLException e)
        {
            System.out.println("Error executing query");
            e.printStackTrace();
        }


        // MS SQL CONNECTION


        // Load MSSQL Driver
        try
        {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
        }
        catch (ClassNotFoundException e)
        {
            System.out.println("Your MS SQL JDBC Driver is not found. Include it in your library path.");
            e.printStackTrace();
        }

        // MS SQL connection settings
        final String MSSQL_HOST = "192.168.1.80";   // My VM IP
        final int MSSQL_PORT = 1433;
        final String MSSQL_DATABASE_NAME = "comp3920Assign1";
        final String MSSQL_USER_NAME = "sa";
        final String MSSQL_PASSWORD = "VFX72vfx72!!";

        final String MSSQL_URL =
            "jdbc:sqlserver://" + MSSQL_HOST + ":" + MSSQL_PORT + ";" +
                "instanceName=SQLEXPRESS;" +
                "databaseName=" + MSSQL_DATABASE_NAME + ";" +
                "user=" + MSSQL_USER_NAME + ";" +
                "password=" + MSSQL_PASSWORD + ";" +
                "encrypt=true;" +
                "trustServerCertificate=true;" +
                "loginTimeout=30;";


        final Connection connection2;
        try
        {
            connection2 = DriverManager.getConnection(MSSQL_URL);
        }
        catch (SQLException e)
        {
            System.out.println("Connection Failed! Check output console");
            e.printStackTrace();
            return;
        }

        if (connection2 != null)
        {
            System.out.println("Successfully connected to MS SQL! :D");
        }

        // Query and print data from MS SQL
        try
        {
            PreparedStatement stmt = connection2.prepareStatement(SELECT_STATEMENT,
                                                                  ResultSet.TYPE_SCROLL_INSENSITIVE,
                                                                  ResultSet.CONCUR_READ_ONLY);
            ResultSet resultSet = stmt.executeQuery();
            printResultSet(resultSet);
        }
        catch (SQLException e)
        {
            System.out.println("Error executing query");
            e.printStackTrace();
        }
    }

    public static void printResultSet(ResultSet resultSet) throws SQLException
    {
        ResultSetMetaData rsmd = resultSet.getMetaData();
        int columnsNumber = rsmd.getColumnCount();
        int rows = 0;
        while (resultSet.next())
        {
            rows++;
            if (rows == 1)
            {
                for (int col = 1; col <= columnsNumber; col++)
                {
                    if (col > 1)
                    {
                        System.out.print(",\t\t");
                    }
                    System.out.print(rsmd.getColumnName(col));
                }
                System.out.println("");
            }
            for (int col = 1; col <= columnsNumber; col++)
            {
                if (col > 1)
                {
                    System.out.print(",\t\t");
                }
                System.out.print(resultSet.getString(col));
            }
            System.out.println("");
        }
    }
}
