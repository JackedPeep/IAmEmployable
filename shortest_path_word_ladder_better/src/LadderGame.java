import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

//Make class abstract
abstract class LadderGame {

    //Could be wrong, this is supposed to be a class variable you store the dictionary in.
    ArrayList<String>[] dictionary;
    ArrayList<String>[] originDictionary;

    public LadderGame(String dictionaryFile) {
        readDictionary(dictionaryFile);
    }

    //Make play abstract
   public abstract void play(String start, String end);

    public ArrayList<String> oneAway(String word, boolean withRemoval) {
        ArrayList<String> words = new ArrayList<>();
        for (int i = 0; i < dictionary[word.length() - 1].size(); i++) {

            if (difference(word, dictionary[word.length() - 1].get(i))) {
                words.add(dictionary[word.length() - 1].get(i));
            }
        }
        if(withRemoval) {
            for (int i = 0; i < words.size(); i++) {
                dictionary[word.length() - 1].remove(word);
                dictionary[word.length() - 1].remove(words.get(i));
            }
        }

        return words;
    }

    public void listWords(int length, int howMany) {
        for(int i = 0; i < howMany; i++){
            System.out.println(dictionary[length-1].get(i));
        }
        //Create a For loop that prints the following:
            //Dictionary[length][i]
    }

    /*
        Reads a list of words from a file, putting all words of the same length into the same array.
     */
    private void readDictionary(String dictionaryFile) {
        File file = new File(dictionaryFile);
        ArrayList<String> allWords = new ArrayList<>();

        // Track the longest word, because that tells us how big to make the array.
        int longestWord = 0;
        try (Scanner input = new Scanner(file)) {
            //
            // Start by reading all the words into memory.
            while (input.hasNextLine()) {
                String word = input.nextLine().toLowerCase();
                allWords.add(word);
                longestWord = Math.max(longestWord, word.length());
            }

            //Create Dictionary
            originDictionary = new ArrayList[longestWord];
            dictionary = new ArrayList[longestWord];
            for(int i = 0; i < longestWord; i++){
                originDictionary[i] = new ArrayList<String>();
                dictionary[i] = new ArrayList<String>();
            }
            //Add words to dictionary
            for(int i = 0; i < allWords.size();i++){
                int len = allWords.get(i).length();
                originDictionary[len-1].add(allWords.get(i));
            }
            for(int i = 0; i < longestWord; i++){
                dictionary[i].addAll(originDictionary[i]);
            }


        }
        catch (java.io.IOException ex) {
            System.out.println("An error occurred trying to read the dictionary: " + ex);
        }
    }

    public boolean difference(String wordOne, String wordTwo){
        int howManyAway = 0;
        for (int i = 0; i < wordOne.length(); i++){
            if (wordOne.charAt(i) != wordTwo.charAt(i)){
                howManyAway++;
            }
        }
        if (howManyAway == 1) {
            return true;
        }
        return false;
    }
}