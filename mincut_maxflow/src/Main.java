import java.io.File;
import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Graph g1 = buildGraph("demands1.txt");

        int flow1 = g1.findMaxFlow(0, 5, true);

        System.out.printf("Total Flow: %d\n", flow1);
        g1.findMinCut(0);

    }

//-- Max Flow: demands1.txt --
//    Flow 2: 0 2 4 5
//    Flow 1: 0 2 3 5
//    Flow 1: 0 1 3 5
//    Flow 2: 0 1 3 4 5
//
//    Edge(0, 2) transports 3 items
//    Edge(0, 1) transports 3 items
//    Edge(1, 3) transports 3 items
//    Edge(2, 4) transports 2 items
//    Edge(2, 3) transports 1 items
//    Edge(3, 5) transports 2 items
//    Edge(3, 4) transports 2 items
//    Edge(4, 5) transports 4 items
//    Total Flow: 6
    public static Graph buildGraph(String filename) {
        try {
            Scanner input = new Scanner(new File(filename));
            int vertexCount = input.nextInt();
            Graph g = new Graph(filename, vertexCount);

            while (input.hasNextInt()) {
                //* First column is source.
                int v1 = input.nextInt();
                //* Second column is destination.
                int v2 = input.nextInt();
                //* Third column is flow capacity.
                int capacity = input.nextInt();
                if (!g.addEdge(v1, v2, capacity)) {
                    throw new Exception();
                }
            }
            input.close();
            System.out.printf("-- %s --\n", filename);
            return g;
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Should throw an exception, but, well, deal with it.
        return null;
    }



}