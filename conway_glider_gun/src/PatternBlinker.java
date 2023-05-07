public class PatternBlinker extends Pattern{

    public PatternBlinker(){
        blinkWorm = new boolean[][]{
                {false, false, false, false, false},
                {false, false, false, false, false},
                {false,  true,  true,  true, false},
                {false, false, false, false, false},

        };

    }
    boolean[][] blinkWorm;
    public int getSizeX() {
        return 5;
    }
    public int getSizeY() {
        return 4;
    }
    public boolean getCell(int x, int y) {
        return blinkWorm[y][x];
    }
}

