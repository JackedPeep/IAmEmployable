

public class Queue<E> {

    private class ListNode<E> {
        public E value;
        public ListNode<E> next;

        public ListNode (){
        }

        public ListNode (E o){
            this.value = o;
        }
    }
    private ListNode<E> head = new ListNode<>();
    private ListNode<E> tail;
    private int size;
    private int totalEnqueues;

    public Queue() {this.size = 0; tail = head; totalEnqueues = 0;}

    public int getSize() {return this.size; }
    public boolean isEmpty() {return this.size == 0;}
    public int getTotalEnqueues() {return this.totalEnqueues;}

    public void enqueue(E o) {
        ListNode<E> node = new ListNode<>(o);
        node.next = null;
        if(this.isEmpty()){
            head = node;
            tail.next = null;
        }
        else tail.next = node;
        tail = node;

        this.size++;
        this.totalEnqueues++;
    }

    public E dequeue() {
        if (head == null){
            return null;
        }
        ListNode<E> node = head;
        head = head.next;

        this.size--;
        return node.value;
    }
}