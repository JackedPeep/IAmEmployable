# <tt>Backward Flow Report</tt>

In line 28 of Graph.java inside the addEdge method this line helps us to build the Graph by allowing us to reverse the 'flow'. It does this by adding a new EdgeInfo in the opposite direction with the *capacity* equaling 0. 

```
public boolean addEdge(int source, int destination, int capacity) {
        // A bit of validation
        if (source < 0 || source >= vertices.length) return false;
        if (destination < 0 || destination >= vertices.length) return false;

        // This adds the actual requested edge, along with its capacity
        vertices[source].addEdge(source, destination, capacity);

        // TODO: This is what you have to describe in the required README.TXT file
        //       that you submit as part of this assignment.
28->    vertices[destination].addEdge(destination, source, 0);

        return true;
        }
```

**Backward flow** is important in this case because it allows us to track where the **actual flow** has routed through the Graph. **Backward flow** also allows us to track the cut points for our findMinCut function. 
