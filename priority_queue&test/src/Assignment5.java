import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Assignment5 {
    public static void main(String[] args) {
        simpleQueueTest();
        scheduleTasks("taskset1.txt");
        scheduleTasks("taskset2.txt");
        scheduleTasks("taskset3.txt");
        scheduleTasks("taskset4.txt");
        scheduleTasks("taskset5.txt");
    }

    public static void scheduleTasks(String taskFile) {

        ArrayList<Task> tasksByDeadline = new ArrayList<>();
        ArrayList<Task> tasksByStart = new ArrayList<>();
        ArrayList<Task> tasksByDuration = new ArrayList<>();

        readTasks(taskFile, tasksByDeadline, tasksByStart, tasksByDuration);

        schedule("Deadline Priority : "+ taskFile, tasksByDeadline);
        schedule("Startime Priority : " + taskFile, tasksByStart);
        schedule("Duration priority : " + taskFile, tasksByDuration);
    }

    public static void simpleQueueTest() {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        queue.enqueue(9);
        queue.enqueue(7);
        queue.enqueue(5);
        queue.enqueue(3);
        queue.enqueue(1);
        queue.enqueue(10);

        while (!queue.isEmpty()) {
            System.out.println(queue.dequeue());
        }
    }

    /**
     * Reads the task data from a file, and creates the three different sets of tasks for each
     */
    public static void readTasks(String filename,
                                 ArrayList<Task> tasksByDeadline,
                                 ArrayList<Task> tasksByStart,
                                 ArrayList<Task> tasksByDuration) 
    {
        try {
            Scanner scanner = new Scanner(new File(filename));
            ArrayList<String> list = new ArrayList<String>();

            while (scanner.hasNextLine()) {
                list.add(scanner.nextLine());
            }
            scanner.close();

            ArrayList<Task> taskList = new ArrayList<>();
            for (int i = 0; i < list.size(); i++) {
                int iD = i + 1;
                String[] sList = list.get(i).split("\t");
                int startTime = Integer.parseInt(sList[0]);
                int deadline = Integer.parseInt(sList[1]);
                int duration = Integer.parseInt(sList[2]);

                TaskByDeadline deadTask = new TaskByDeadline(iD, startTime, deadline, duration);
                TaskByDuration durTask = new TaskByDuration(iD, startTime, deadline, duration);
                TaskByStart startTask = new TaskByStart(iD, startTime, deadline, duration);

                tasksByDeadline.add(deadTask);
                tasksByDuration.add(durTask);
                tasksByStart.add(startTask);
            }
        }
        catch (java.io.IOException ex) {
            System.out.println("An error occurred trying to read the tasks: " + ex);
        }
    }

    /**
     * Given a set of tasks, schedules them and reports the scheduling results
     */
    public static void schedule(String label, ArrayList<Task> tasks) {

        boolean done = false;
        int tasksCompleted = 0;
        int lateTasks = 0;
        int lateTime = 0;

        ArrayList<Task> tasks2 = new ArrayList<>();
        for (int i = 0; i < tasks.size(); i++) {
            tasks2.add(tasks.get(i));
        }

        System.out.println(label);
        PriorityQueue<Task> queue = new PriorityQueue<>();

        for(Task addtask : tasks2){
            if(addtask.start == 1){
                queue.enqueue(addtask);
            }
        }
        Task task = queue.dequeue();

        for(int clock = 1; !done; clock++){
            System.out.printf("Time %2s: ", clock);

            if(task.duration == 0){System.out.println("---");}
            else if (task.duration > 1) {
                task.duration--;
                queue.enqueue(task);
                if(task.deadline < clock){
                    lateTime++;
                    int time = clock - task.deadline;
                    System.out.println(task.toString()+ "Late" + time);
                }
                else{
                    System.out.println(task.toString());
                }
            }
            else{
                task.duration--;
                tasksCompleted++;
                if (tasksCompleted == tasks2.size()){
                    done = true;
                }
                if(task.deadline < clock){
                    lateTime++;
                    lateTasks++;
                    int time = clock - task.deadline;
                    System.out.println(task.toString()+ " ** Late" + time);
                }
                else{
                    System.out.println(task.toString()+ " **");
                }

            }



            for(Task addtask : tasks2){
                if(addtask.start == clock + 1){
                    queue.enqueue(addtask);
                }
            }
            if(!queue.isEmpty()) {
                task = queue.dequeue();
            }

        }
        System.out.printf("Tasks late %s Total Late %s\n\n",lateTasks, lateTime);


    }
}
