public class PriorityQueue<Q extends Comparable<Q>>{
    //This queue is formated as a leftist heap
    public LHeapNode<Q> root;
    public PriorityQueue(){
        this.root = null;
    }

    private class LHeapNode<Q> {


        public Q value;
        public LHeapNode<Q> left;
        public LHeapNode<Q> right;
        public int nullPathLength;


        private LHeapNode(Q value){
            this(value, null, null);
        }
        private LHeapNode(Q value, LHeapNode<Q> left, LHeapNode<Q> right){
            this.value = value;
            this.left = left;
            this.right = right;
            nullPathLength = 0;

        }


    }


    /**
     * This class method merges the two heaps together outputting a leftist heap.
     *
     * @param heap1 first heap
     * @param heap2 second heap
     * @return a merged leftist heap as a LHeapNode class
     */
    private LHeapNode<Q> merge(LHeapNode<Q> heap1, LHeapNode<Q> heap2){
        LHeapNode<Q> small;
        if(heap1 == null){return heap2;}
        if(heap2 == null){return heap1;}
        if(heap1.value.compareTo(heap2.value) < 0){
            heap1.right = merge(heap1.right, heap2);
            small = heap1;
        }
        else{
            heap2.right = merge(heap2.right, heap1);
            small = heap2;
        }
        if(getNullPathLength(small.left) < getNullPathLength(small.right)){
            swapChildren(small);
        }
        setNullPathLength(small);
        return small;
    }
    public int getNullPathLength(LHeapNode<Q> node){return getNullPathLengthRecursive(node);}

    private int getNullPathLengthRecursive(LHeapNode<Q> node){

        if(node == null){return -1;}
        if(node.left == null || node.right == null){return 0;}

        int nullPathLength = Math.min(getNullPathLengthRecursive(node.right), getNullPathLengthRecursive(node.left));

        return nullPathLength +1;
    }

    public void setNullPathLength(LHeapNode<Q> node){
       node.nullPathLength = getNullPathLength(node);
    }

    public void swapChildren(LHeapNode<Q> node){
        LHeapNode<Q> leftNode = node.left;
        node.left = node.right;
        node.right = leftNode;
    }



    public void enqueue(Q value) {
        LHeapNode<Q> node = new LHeapNode<>(value);
        root = merge(root, node);
    }

    public Q dequeue() {
        LHeapNode<Q> deletedNode = root;
        if (isEmpty()) {
            System.out.println("Queue is empty.");
        }
        Q deletedNodeValue = deletedNode.value;

        root = merge(root.left, root.right);
        return deletedNodeValue;

    }

    public boolean isEmpty(){
        return root == null;
    }

}
