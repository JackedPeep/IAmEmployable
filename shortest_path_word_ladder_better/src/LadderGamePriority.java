import java.util.ArrayList;

public class LadderGamePriority extends LadderGame{
    public LadderGamePriority(String dictionaryFile) {
        super(dictionaryFile);
    }

    public void play(String start, String end){
        if (start.length() != end.length()){
            System.out.println("error: Starting word length does not equal ending word length.");
            System.exit(1);
        }
        if (start.equals(end)) {
            System.out.println("error: Starting word is end word. No word ladder needed.");
            System.exit(1);
        }

        //Add start to your initial queue
        AVLTree<WordInfoPriority> WrdQueue = new AVLTree<>();
        int estimatedWork = calcWork(start,end);
        WordInfoPriority startingWord = new WordInfoPriority(start, 0, estimatedWork);
        WrdQueue.insert(startingWord);

        //Main loop(while ladder is !complete && queue is !empty:
        ArrayList<String> oneAwayWords = new ArrayList<>();
        WordInfoPriority newWord = startingWord;
        WordInfoPriority currentWord;


        boolean complete = false;

        ArrayList<WordInfoPriority> pastWords = new ArrayList<>();

        while (!WrdQueue.isEmpty() && !complete) {
            //Remove first word
            currentWord = WrdQueue.deleteMin();
            pastWords.add(currentWord);
            //Find all words 1 away
            oneAwayWords = oneAway(currentWord.getWord(), false);
            for(int i = 0; i < oneAwayWords.size() && !complete;i++){
                boolean found = false;
                ArrayList<String> newHistory = new ArrayList<>();
                newHistory.addAll(currentWord.getHistory());
                int moves = currentWord.getMoves() + 1;
                estimatedWork = moves + calcWork(oneAwayWords.get(i),end);
                newWord = new WordInfoPriority(oneAwayWords.get(i), moves, estimatedWork, newHistory);
                for(int j = 0; j < pastWords.size(); j++){
                    if (pastWords.get(j).getWord() == newWord.getWord()){
                        found = true;
                        if(pastWords.get(j).getMoves() > newWord.getMoves()){
                            pastWords.remove(j);
                            pastWords.add(newWord);
                            if (!oneAwayWords.get(i).equals(end)){
                                WrdQueue.insert(newWord);
                            }
                            else complete = true;
                        }
                    }
                }
                if(!found){
                    if (!oneAwayWords.get(i).equals(end)){
                        WrdQueue.insert(newWord);
                    }
                    else complete = true;
                }


            }


        }
        System.out.println("seeking A* solution from " + start + " -> " + end + " : ");
        if(complete) {
            System.out.println(newWord.getHistory());
            System.out.println(" total enqueues " + WrdQueue.getTotalEnqueues());
        }
        else {
            System.out.println("No ladder was found");
        }
        dictionary[start.length()-1].addAll(originDictionary[start.length()-1]);



    }
    private int calcWork(String currentWord, String targetWord){
        int workLeft = 0;
        for(int i = 0; i < targetWord.length(); i++){
            if(currentWord.charAt(i) != targetWord.charAt(i)){
                workLeft++;
            }
        }
        return workLeft;
    }
}
