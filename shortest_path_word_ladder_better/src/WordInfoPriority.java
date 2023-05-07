import java.util.ArrayList;

public class WordInfoPriority implements Comparable<WordInfoPriority> {
    private String word;
    private int moves;
    private ArrayList<String> history;
    private int priority;

    public int compareTo(WordInfoPriority other){
        return this.priority - other.priority;
    }

    public WordInfoPriority(String word, int moves, int estimatedWork) {
        this.word = word;
        this.moves = moves;
        this.history = new ArrayList<>();
        this.history.add(word);
        this.priority = estimatedWork;
    }

    public WordInfoPriority(String word, int moves, int estimatedWork, ArrayList<String> history) {
        this.word = word;
        this.moves = moves;
        this.history = history;
        this.history.add(word);
        this.priority = estimatedWork;
    }

    public String getWord() {
        return this.word;
    }

    public int getMoves() {
        return this.moves;
    }

    public ArrayList<String> getHistory() {
        return this.history;
    }

    public int getPriority(){
        return this.priority;
    }

    @Override
    public String toString() {
        return String.format("Word %s Moves %d : History[%s]",
                word, moves, history);
    }


}
