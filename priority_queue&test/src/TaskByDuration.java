public class TaskByDuration extends Task implements Comparable<Task>{
    public TaskByDuration(int ID, int start, int deadline, int duration){
        super(ID, start, deadline, duration);

    }

    public int compareTo(Task other){

        return Integer.compare(this.duration, other.duration);

    }

}
