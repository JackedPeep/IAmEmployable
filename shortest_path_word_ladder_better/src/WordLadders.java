public class WordLadders {
    public static void main(String[] args) {
        //testAvlTree();
        ladderGame();
    }

    private static void ladderGame() {
        LadderGame gamePriority = new LadderGamePriority("dictionary.txt");
        LadderGame gameExhaustive = new LadderGameExhaustive("dictionary.txt");

        gameExhaustive.play("kiss", "woof");
        gamePriority.play("kiss", "woof");
        System.out.println();

        gameExhaustive.play("rock", "numb");
        gamePriority.play("rock", "numb");
        System.out.println();

        gameExhaustive.play("rums", "numb");
        gamePriority.play("rums", "numb");
        System.out.println();

        gameExhaustive.play("jura", "such");
        gamePriority.play("jura", "such");
        System.out.println();

        gameExhaustive.play("stet", "whey");
        gamePriority.play("stet", "whey");
        System.out.println();

        gameExhaustive.play("butter", "plates");
        gamePriority.play("butter", "plates");
        System.out.println();

        gameExhaustive.play("crafted", "mommies");
        gamePriority.play("crafted", "mommies");
        System.out.println();

        gameExhaustive.play("stone", "money");
        gamePriority.play("stone", "money");
    }

    public static void testAvlTree() {
        AVLTree<Integer> primeTree = new AVLTree<>();
        AVLTree<Dwarf> dwarfTree = new AVLTree<>();

        String[] nameList = {"Snowflake", "Sneezy", "Doc", "Grumpy", "Bashful", "Dopey", "Happy", "Doc", "Grumpy", "Bashful", "Doc", "Grumpy", "Bashful"};
        for (var name : nameList) {
            dwarfTree.insert(new Dwarf(name));
        }

        Integer[] primeList = { 1, 2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43};
        for (var number : primeList) {
            primeTree.insert(number);
        }

        primeTree.printTree("Prime Tree");
        dwarfTree.printTree( "Dwarf Tree" );

        System.out.println("\n\n-- Calling deleteMin on primeTree --");
        primeTree.deleteMin();
        primeTree.printTree("The Tree after deleteMin");
        System.out.println("-- Calling deleteMin on primeTree --");
        primeTree.deleteMin();
        primeTree.printTree("The Tree after deleteMin");

        System.out.println("-- Calling deleteMin on dwarfTree until it is empty");
        while (!dwarfTree.isEmpty()) {
            System.out.printf("%s\n", dwarfTree.deleteMin());
        }
        System.out.println("-- Calling deleteMin on primeTree until it is empty");
        while (!primeTree.isEmpty()) {
            var max = primeTree.findMax();
            System.out.printf("%d[%d] ", primeTree.deleteMin(), max);
        }
        System.out.println();
    }
}
