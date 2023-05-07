
import java.io.File;
import java.util.Scanner;


public class WritePoetry {
    public String writePoem(String file, String startWord, int length, boolean printHashtable) {
        //file contains the document to read.
        //startWord is the first word of the poem to generate
        // length is how many words(including punctuation) to generate
        HashTable<String, WordFreqInfo> hashTable = createHashTable(file);
        String newWord = startWord;
        String poem = "";
        for (int i = 0; i < length - 2; i++){

            if (!Character.isAlphabetic(newWord.charAt(0))) {
                poem += newWord + "\n";
            } else {
                poem += " " + newWord;
            }
            if (hashTable.contains(newWord)) {
                WordFreqInfo curWord = hashTable.find(newWord);
                int randomCount = (int) (Math.random() * (curWord.getOccurCount() + 1));
                newWord = curWord.getFollowWord(randomCount);
            }
            else {
                newWord = ".";
                System.out.println("Failed to find word");
            }

        }
        poem += " " + newWord;
        if (Character.isAlphabetic(newWord.charAt(0))) {
            poem += ".";
        }
        if(printHashtable){
            System.out.println(hashTable.toString(hashTable.size()));
        }
        //print the hashtable to consol as shown in the example output
        //YOU MAY WRITE PRIVATE METHODS TO AID IN THE PUBLIC METHOD ABOVE
        return poem;


    }

    public static HashTable<String, WordFreqInfo> createHashTable(String fileName) {
        HashTable<String, WordFreqInfo> hashTable = new HashTable<>();

        File ofile = new File(fileName);
        HashTable<String, WordFreqInfo> allWords = new HashTable<>();

        try (Scanner input = new Scanner(ofile)) {
            String baseWord = input.next();
            String nextWord;
            String word;
            // Start by reading all the words into memory.
            while (input.hasNext()) {

                if (baseWord.length()==1 && !Character.isAlphabetic(baseWord.charAt(0))){
                    word = baseWord;
                }
                else {
                    word = cleanWord(baseWord);
                }
                if(punctuated(baseWord)){
                    char charPunctuation = baseWord.charAt(baseWord.length()-1);
                    nextWord = Character.toString(charPunctuation);
                    baseWord = nextWord;

                }
                else{
                    baseWord = input.next();
                    nextWord = cleanWord(baseWord);
                }


                if (word.length() > 0) {

                    if(hashTable.contains(word)){
                        //If not new update WordFreqInfo count
                        WordFreqInfo wordInfo = hashTable.find(word);
                        wordInfo.updateFollows(nextWord);
                    }
                    else{
                        //If new word create new WordFreqInfo
                        WordFreqInfo newWord = new WordFreqInfo(word,0);
                        newWord.updateFollows(nextWord);
                        hashTable.insert(word, newWord);
                    }

                }
            }
        } catch (java.io.IOException ex) {
            System.out.println("An error occurred trying to read the poem: " + ex);
        }
        return hashTable;
    }

    private static String cleanWord(String word) {
        word = word.toLowerCase();

        // Remove any punctuation
        String newWord = "";
        for (int i = 0; i < word.length(); i++) {
            if (Character.isAlphabetic(word.charAt(i)) || word.charAt(i) == '\'') {
                newWord += word.charAt(i);
            }
        }

        if (newWord.length() > 0 && !Character.isAlphabetic(newWord.charAt(0))) {
            newWord = newWord.substring(1);
        }

        return newWord;
    }
    /**
     * Checks to see if the end character of the word is a punctuation symbol.
     *
     * @param word the string to check.
     * @return "true" if the last character in the word is a punctuation, & "false" if the last character in the word is alphabetical.
     *
     * @author K. Brady Christianson
     */

    private static boolean punctuated(String word){
        if(word.length() == 1){
            return false;
        }
        return !Character.isAlphabetic(word.charAt(word.length()-1));
    }
}