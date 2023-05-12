import java.util.*;

class GraphNode {
    public int id;
    public int parent;
    public LinkedList<EdgeInfo> successor;
    public boolean visited;

    public GraphNode(int id) {
        this.id = id;
        this.successor = new LinkedList<>();
        this.parent = -1;
        this.visited = false;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(id + ": ");

        for (var edge : successor) {
            sb.append(edge.toString());
        }

        sb.append("\n");
        return sb.toString();
    }

    public void addEdge(int v1, int v2, int capacity) {
        successor.addFirst(new EdgeInfo(v1, v2, capacity));
    }

    public class EdgeInfo {
        int transported; //* keeps track of actual flow along the edge
        int from;        // source of edge
        int to;          // destination of edge
        int capacity;    // capacity of edge

        public EdgeInfo(int from, int to, int capacity) {
            this.from = from;
            this.to = to;
            this.capacity = capacity;
            this.transported = 0;

        }

        public String toString() {
            return "Edge " + from + "->" + to + " (" + capacity + ") ";
        }
    }
}
