public class TaskByDeadline extends Task implements Comparable<Task> {
    public TaskByDeadline(int ID, int start, int deadline, int duration){
        super(ID, start, deadline, duration);

    }

    public int compareTo(Task other){

        return Integer.compare(this.deadline, other.deadline);

    }




}
