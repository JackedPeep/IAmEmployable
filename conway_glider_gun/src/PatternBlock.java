public class PatternBlock extends Pattern{
    public PatternBlock(){
        blockWorm = new boolean[][]{
                {false, false, false, false},
                {false,  true,  true, false},
                {false,  true,  true, false},
                {false, false, false, false},

        };

    }
    boolean[][] blockWorm;
    public int getSizeX() {
        return 4;
    }
    public int getSizeY() {
        return 4;
    }
    public boolean getCell(int x, int y) {
        return blockWorm[y][x];
    }
}
