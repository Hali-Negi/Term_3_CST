import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Graph
{
    private String[] vertexLabels;
    private int[][] matrix;
    private boolean isDirected;
    private boolean[] visitedArray;
    private List<String> dfsOrder;
    private List<String> finishedOrder;
    private List<String> bfsOrder;


    // Constructor: initializes vertex labels, adjacency matrix (all zeroes), and directed flag
    public Graph(String[] vertexLabels,
                 boolean isDirected)
    {
        this.vertexLabels = vertexLabels;
        this.isDirected   = isDirected;
        matrix            = new int[vertexLabels.length][vertexLabels.length];
    }


    // Returns true if the graph is directed, false if undirected
    public boolean isDirected()
    {
        return isDirected;
    }


    // Adds an edge from vertex A to vertex B. If undirected, adds both directions.
    // Silently does nothing if either vertex is not found
    public void addEdge(String A,
                        String B)
    {   //Not found
        int indexA = -1;
        int indexB = -1;

        for (int i = 0; i < vertexLabels.length; i++)
        {
            if (vertexLabels[i].equals(A))
            {
                indexA = i;
            }
            if (vertexLabels[i].equals(B))
            {
                indexB = i;
            }
        }

        if (indexA == -1 ||
            indexB == -1)
        {
            return;
        }
        matrix[indexA][indexB] = 1;
        if (!isDirected)
        {
            matrix[indexB][indexA] = 1;
        }

    }


    // Returns the number of vertices in the graph
    public int size()
    {
        return vertexLabels.length;
    }

    // Returns the string label of the vertex at internal index v
    public String getLabel(int v)
    {
        return vertexLabels[v];
    }


    // Returns a string representation of the adjacency matrix, one line per vertex
    public String toString()
    {
        String result = "";
        for (int i = 0; i < vertexLabels.length; i++)
        {
            result += vertexLabels[i] + ": ";

            for (int j = 0; j < vertexLabels.length; j++)
            {
                result += matrix[i][j] + " ";
            }
            result += "\n";
        }
        return result;
    }


    // Runs DFS on all vertices. Saves DFS order and dead-end order internally.
    // Prints each visited vertex if quiet is false
    public void runDFS(boolean quiet)
    {
        visitedArray  = new boolean[vertexLabels.length];
        dfsOrder      = new ArrayList<>();
        finishedOrder = new ArrayList<>();

        for (int i = 0; i < vertexLabels.length; i++)
        {
            if (!visitedArray[i])
            {
                dfsHelper(i, quiet);
            }
        }
    }

    public List<String> getDFSOrder()
    {
        return dfsOrder;
    }

    public List<String> getFinishedOrder()
    {
        return finishedOrder;
    }

    private void dfsHelper(int v,
                           boolean quiet)
    {
        //1.
        visitedArray[v] = true;
        //2. visit order = forward
        dfsOrder.add(vertexLabels[v]);
        if (!quiet)
        {
            System.out.println("Visiting vertex " + vertexLabels[v]);

        }
        //3.
        for (int j = 0; j < vertexLabels.length; j++)
        {
            if (matrix[v][j] == 1 && !visitedArray[j])
            {
                dfsHelper(j, quiet);
            }
        }
        //4. finished order = reverse
        finishedOrder.add(vertexLabels[v]);
    }

    // Runs DFS starting from vertex v. Only visits vertices reachable from v.
    // Prints each visited vertex if quiet is false
    public void runDFS(String v,
                       boolean quiet)
    {
        int startIndex = -1;
        for (int i = 0; i < vertexLabels.length; i++)
        {
            if (vertexLabels[i].equals(v))
            {
                startIndex = i;

                break;
            }
        }
        if (startIndex == -1)
        {
            System.out.println("Vertex not found");
            return;
        }

        visitedArray  = new boolean[vertexLabels.length];
        dfsOrder      = new ArrayList<>();
        finishedOrder = new ArrayList<>();

        // Recursive DFS helper. Marks vertex as visited, records visit and finish order
        dfsHelper(startIndex, quiet);
    }

    // void runBFS(boolean quiet)
    // 1.Add starting vertex to queue,  2.Mark visited  3.While queue NOT empty:  4.remove first element  5.visit it
    //6. check ALL neighbors  7.add unvisited neighbors to queue
    public void runBFS(boolean quiet)
    {
        visitedArray = new boolean[vertexLabels.length];
        bfsOrder     = new ArrayList<>();
        List<Integer> queue = new LinkedList<>();


        for (int i = 0; i < vertexLabels.length; i++)
        {
            if (!visitedArray[i])
            {
                queue.add(i);
                visitedArray[i] = true;
                while (!queue.isEmpty())
                {
                    int v = queue.remove(0);
                    bfsOrder.add(vertexLabels[v]);

                    if (!quiet)
                    {
                        System.out.println("BFS Visiting vertex " + vertexLabels[v]);

                    }

                    for (int j = 0; j < vertexLabels.length; j++)
                    {
                        if (matrix[v][j] == 1 && !visitedArray[j])
                        {
                            queue.add(j);
                            visitedArray[j] = true;
                        }
                    }
                }
            }

        }

    }

    public List<String> getBFSOrder()
    {
        return bfsOrder;
    }


    // Runs BFS starting from vertex v. Only visits vertices reachable from v.
    // Prints each visited vertex if quiet is false
    public void runBFS(String v,
                       boolean quiet)
    {
        int startIndex = -1;

        visitedArray = new boolean[vertexLabels.length];
        bfsOrder     = new ArrayList<>();
        List<Integer> queue = new LinkedList<>();

        for (int i = 0; i < vertexLabels.length; i++)
        {
            if (vertexLabels[i].equals(v))
            {
                startIndex = i;
                break;
            }
        }
        if (startIndex == -1)
        {
            System.out.println("Vertex not found");
            return;
        }
        queue.add(startIndex);
        visitedArray[startIndex] = true;
        while (!queue.isEmpty())
        {
            int current = queue.remove(0);
            bfsOrder.add(vertexLabels[current]);

            if (!quiet)
            {
                System.out.println("BFS Visiting vertex " + vertexLabels[current]);
            }

            for (int j = 0; j < vertexLabels.length; j++)
            {
                if (matrix[current][j] == 1 && !visitedArray[j])
                {
                    queue.add(j);
                    visitedArray[j] = true;
                }
            }

        }
    }

    // Returns the DFS visit order from the most recent DFS run.
    // Returns a message if no DFS has been run yet
    public String getLastDFSOrder()
    {
        if (dfsOrder == null)
        {
            return "No DFS has been run";
        }
        return dfsOrder.toString();
    }


    // Returns the dead-end (finished) order from the most recent DFS run.
    // Returns a message if no DFS has been run yet
    public String getLastDFSDeadEndOrder()
    {
        if (finishedOrder == null)
        {
            return "No DFS has been run";
        }
        return finishedOrder.toString();
    }


    // Returns the BFS visit order from the most recent BFS run.
    // Returns a message if no BFS has been run yet
    public String getLastBFSOrder()
    {
        if (bfsOrder == null)
        {
            return "No BFS has been run";
        }
        return bfsOrder.toString();
    }

}







