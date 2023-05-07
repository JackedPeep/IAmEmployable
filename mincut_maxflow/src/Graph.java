import java.util.*;

public class Graph {
    private final GraphNode[] vertices;  // Adjacency list for graph.
    private final String name;  //The file from which the graph was created.

    public Graph(String name, int vertexCount) {
        this.name = name;

        vertices = new GraphNode[vertexCount];
        for (int i = 0; i < vertexCount; i++) {
            vertices[i] = new GraphNode(i);
            //* ^^ Builds the array of graph nodes' ID matches location in vertices array
        }
    }

    //* NON-RECURSIVE; the Graph.addEdge calls the graphNode.addEdge
    public boolean addEdge(int source, int destination, int capacity) {
        // A bit of validation
        if (source < 0 || source >= vertices.length) return false;
        if (destination < 0 || destination >= vertices.length) return false;

        // This adds the actual requested edge, along with its capacity
        vertices[source].addEdge(source, destination, capacity);

        // TODO: This is what you have to describe in the required README.TXT file
        //       that you submit as part of this assignment.
        vertices[destination].addEdge(destination, source, 0);

        return true;
    }

    /**
     * Algorithm to find max-flow in a network
     */
    public int findMaxFlow(int s, int t, boolean report) {
        if(report){
            System.out.printf("\n-- Max Flow: %s --\n", this.name);
        }
        int flow = 0;
        while (hasAugmentingPath(s, t)) {
            int availableFlow = Integer.MAX_VALUE;
            GraphNode v = vertices[t];
            GraphNode.EdgeInfo directionalEdge;
            while (v.id != s) {
                directionalEdge = findAugmentedEdge(vertices[v.parent], v);
                if (directionalEdge.capacity < availableFlow) {
                    availableFlow = directionalEdge.capacity;
                }
                v = vertices[v.parent];

            }
            v = vertices[t];
            String flowPath = "";
            while (v.id != s) {
                flowPath = v.id + " " + flowPath;
                directionalEdge = findAugmentedEdge(v, vertices[v.parent]);
                directionalEdge.capacity += availableFlow;

                directionalEdge = findAugmentedEdge(vertices[v.parent], v);
                directionalEdge.capacity -= availableFlow;
//                directionalEdge.transported += availableFlow;
                v = vertices[v.parent];
            }

            flow += availableFlow;
            if (report) {
                System.out.println("Flow " + availableFlow + ": " + Integer.toString(s) + " " + flowPath);
            }
        }
        if (report) {
            System.out.println();
            for (GraphNode node: vertices) {
                for (GraphNode.EdgeInfo edge : vertices[node.id].successor) {
//                    if (edge.transported > 0) {
//                        System.out.printf("Edge(%s, %s) transports %s items\n", edge.from, edge.to, edge.transported);
//                    }
                    if (edge.capacity > 0) {
                        System.out.printf("Edge(%s, %s) transports %s items\n", edge.from, edge.to, edge.capacity);
                    }
                }
            }

        }

        return flow;
    }

    private GraphNode.EdgeInfo findAugmentedEdge(GraphNode output, GraphNode input) {
        GraphNode.EdgeInfo augmentedEdge = output.successor.get(0);
        for (GraphNode.EdgeInfo edge : output.successor) {
            if (edge.to == input.id) {
                augmentedEdge = edge;
                break;
            }
        }
        return augmentedEdge;
    }


    /**
     * Algorithm to find an augmenting path in a network
     */
    private boolean hasAugmentingPath(int s, int t) {
        Queue<GraphNode> queue = new LinkedList<>();

        for (GraphNode node : vertices) {
            node.parent = -1;
        }
        queue.add(vertices[s]);

        while (!queue.isEmpty() && vertices[t].parent == -1) {
            GraphNode v = queue.remove();
            for (int i = 0; i < v.successor.size(); i++) {
                GraphNode.EdgeInfo edgeInfo = v.successor.get(i);
                GraphNode w = vertices[edgeInfo.to];
                if (edgeInfo.capacity > 0 && w.parent == -1 && w.id != s) {
                    w.parent = v.id;
                    queue.add(w);
                }
            }

        }
        return vertices[t].parent != -1;
    }

    /**
     * Algorithm to find the min-cut edges in a network
     */
    public void findMinCut(int s) {
        changeVertexID(s);
        findMinCutEdge(s);
    }

    private void changeVertexID(int s) {
        // 2) Find the set of vertices that are reachable from the source vertex in the residual graph; the set R includes s.  Call those vertices R.

        Queue<GraphNode> queue = new LinkedList<>();

        queue.add(vertices[s]);

        while (!queue.isEmpty()) {
            GraphNode v = queue.remove();
            for (int i = 0; i < v.successor.size(); i++) {
                GraphNode.EdgeInfo edgeInfo = v.successor.get(i);
                GraphNode next = vertices[edgeInfo.to];
                v.parent = s;
                if (edgeInfo.capacity > 0 && next.parent != s) {
                    queue.add(next);
                }

            }
        }
    }

    private void findMinCutEdge(int s) {
        // 3) All edges from a vertex in R to a vertex not in R are the minimum cut edges
        System.out.printf("\n-- Min Cut: %s --\n", this.name);
        for(int j = 0; j < vertices.length; j++) {
            GraphNode v = vertices[j];
            if (v.parent != s) {
                for (int i = 0; i < v.successor.size(); i++) {
                    GraphNode.EdgeInfo edgeInfo = v.successor.get(i);
                    GraphNode next = vertices[edgeInfo.to];

                    if (next.parent == s) {
                        System.out.printf("Min Cut Edge: (%s, %s)\n", edgeInfo.to, edgeInfo.from);
                    }

                }
            }

        }

    }


    public String toString() {
        StringBuilder sb = new StringBuilder();

        sb.append("The Graph ").append(name).append(" \n");
        for (var vertex : vertices) {
            sb.append((vertex.toString()));
        }
        return sb.toString();
    }


}