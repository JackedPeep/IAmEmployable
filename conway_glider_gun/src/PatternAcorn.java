public class PatternAcorn extends Pattern {
    public PatternAcorn(){
        acornWorm = new boolean[][]{
                {false, false, false, false, false, false, false, false, false},
                {false, false,  true, false, false, false, false, false, false},
                {false, false, false, false,  true, false, false, false, false},
                {false,  true,  true, false, false,  true,  true,  true, false},
                {false, false, false, false, false, false, false, false, false},

        };

    }
    boolean[][] acornWorm;
    public int getSizeX() {
        return 9;
    }
    public int getSizeY() {
        return 5;
    }
    public boolean getCell(int x, int y) {
        return acornWorm[y][x];
    }
}
