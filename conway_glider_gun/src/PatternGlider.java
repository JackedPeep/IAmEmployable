public class PatternGlider extends Pattern{
    public PatternGlider(){
        glideWorm = new boolean[][]{
                {false, false, false, false, false},
                {false, false,  true, false, false},
                {false, false, false,  true, false},
                {false,  true,  true,  true, false},
                {false, false, false, false, false},


        };

    }
    boolean[][] glideWorm;
    public int getSizeX() {
        return 5;
    }
    public int getSizeY() {
        return 5;
    }
    public boolean getCell(int x, int y) {
        return glideWorm[y][x];
    }
}
