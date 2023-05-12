import java.io.File;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
//        System.out.println(hash("apple",2));
//        System.out.println(hash("banana",2));
//        System.out.println(hash("carrot",2));
//        System.out.println(hash("digglett",2));
//        System.out.println(hash("engine",2));
//        System.out.println(hash("figgypudding",2));
//        System.out.println(hash("guild",2));
//
//        System.out.println();
//        System.out.println(hash("apple",5));
//        System.out.println(hash("banana",5));
//        System.out.println(hash("carrot",5));
//        System.out.println(hash("digglett",5));
//        System.out.println(hash("engine",5));
//        System.out.println(hash("figgypudding",5));
//        System.out.println(hash("guild",5));
//
//        System.out.println();
//        System.out.println(hash("apple",10));
//        System.out.println(hash("banana",10));
//        System.out.println(hash("carrot",10));
//        System.out.println(hash("digglett",10));
//        System.out.println(hash("engine",10));
//        System.out.println(hash("figgypudding",10));
//        System.out.println(hash("guild",10));
//        String word = "bottled.";
//        System.out.println(word.substring(0,1));
//        System.out.println(word.substring(0,2));
//        System.out.println(word.substring(0,3));
//        System.out.println(word.substring(0,4));
//        System.out.println(cleanWord("bottle."));
//        System.out.println(cleanWord("sasquatch!"));
//        System.out.println(cleanWord("tea."));
//        System.out.println(cleanWord("half-day"));
        HashTable<String,WordFreqInfo> table = createHashTable("green.txt");
        System.out.println(table.toString(50));


    }
    public static int hash(String key, int TABLESIZE){
        int hashValue = 0;

        for(int i = 0; i < key.length(); i++){
            //prevents overflow
            hashValue = (hashValue << 5)^key.charAt(i)^hashValue;
        }
        //returns a positive value
        hashValue = Math.abs(hashValue) % TABLESIZE;

        return hashValue;
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

                if (baseWord.length()>1){
                     word = cleanWord(baseWord);
                }
                else {
                    word = baseWord;
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
    private static boolean punctuated(String word){
        if(word.length() == 1){
            return false;
        }
        return !Character.isAlphabetic(word.charAt(word.length()-1));
    }

}