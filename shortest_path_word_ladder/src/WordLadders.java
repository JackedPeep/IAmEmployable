public class WordLadders {
    public static void main(String[] args) {

        LadderGame g = new LadderGame("dictionary.txt");

        System.out.println("--- First 10 words of length 6 ---");
        g.listWords(6, 10);
        System.out.println();

        System.out.println("--- Words One Away from 'slow' ---");
        for (String word : g.oneAway("slow", false)) {
            System.out.println(word);
        }
        System.out.println();

        System.out.println("--- Word Ladders ---");
        g.play("oops", "tots");
        g.play("ride", "ands");
        g.play("happily", "angrily");
        g.play("slow", "fast");
        g.play("stone", "money");
        g.play("biff", "axis");
        g.play("fungi", "among");
        g.play("kiss", "woof");
    }
}
