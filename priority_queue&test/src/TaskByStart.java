public class TaskByStart extends Task implements Comparable<Task>{

    public TaskByStart(int ID, int start, int deadline, int duration){
        super(ID, start, deadline, duration);
    }

    public int compareTo(Task other){

        if(this.start == other.start){
            return Integer.compare(this.deadline, other.deadline);
        }

        if(this.start < other.start){return -1;}
        else{return 1;}


    }


}
