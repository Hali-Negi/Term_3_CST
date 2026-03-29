public class Main
{
    public static void main(String[] args)
    {
        String[] vnames = {"a", "b", "c", "d", "e"};
        Graph G = new Graph(vnames, false);

        System.out.println("Is directed: " + G.isDirected());

        G.addEdge("a", "b");
        G.addEdge("a", "d");
        G.addEdge("b", "c");
        G.addEdge("c", "d");

        System.out.println("Size: " + G.size());

        System.out.println("Label 0: " + G.getLabel(0));
        System.out.println("Label 2: " + G.getLabel(2));

        System.out.println("Adjacency Matrix:");
        System.out.println(G.toString());

        // ---- DFS (all vertices) ----
        System.out.println("---- DFS ----");
        G.runDFS(false);

        // ---- DFS from specific vertex ----
        System.out.println("---- DFS from a ----");
        G.runDFS("a", false);

        // ---- BFS (all vertices) ----
        System.out.println("---- BFS ----");
        G.runBFS(false);

        // ---- BFS from specific vertex ----
        System.out.println("---- BFS from a ----");
        G.runBFS("a", false);

        // ---- TEST GETTERS BEFORE ANY TRAVERSAL ----
        System.out.println("---- TEST GETTERS BEFORE ANY TRAVERSAL ----");
        String[] vnames2 = {"a", "b", "c", "d"};
        Graph G2 = new Graph(vnames2, false);
        G2.addEdge("a", "b");
        G2.addEdge("b", "c");

        // Should print "No DFS has been run" / "No BFS has been run"
        System.out.println(G2.getLastDFSOrder());
        System.out.println(G2.getLastDFSDeadEndOrder());
        System.out.println(G2.getLastBFSOrder());

        // ---- TEST GETTERS AFTER TRAVERSAL ----
        System.out.println("---- TEST GETTERS AFTER TRAVERSAL ----");
        G2.runDFS(true);
        System.out.println("DFS order: " + G2.getLastDFSOrder());
        System.out.println("DFS dead end order: " + G2.getLastDFSDeadEndOrder());

        G2.runBFS(true);
        System.out.println("BFS order: " + G2.getLastBFSOrder());

        // ---- TEST GETTERS UPDATE EACH TIME ----
        System.out.println("---- TEST GETTERS UPDATE EACH TIME ----");
        G2.runDFS(true);
        System.out.println("After full DFS: " + G2.getLastDFSOrder());
        G2.runDFS("b", true);
        System.out.println("After DFS from b: " + G2.getLastDFSOrder());

        G2.runBFS(true);
        System.out.println("After full BFS: " + G2.getLastBFSOrder());
        G2.runBFS("b", true);
        System.out.println("After BFS from b: " + G2.getLastBFSOrder());
    }
}