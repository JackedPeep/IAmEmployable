public class LifeSimulator {
    public LifeSimulator(int sizeX, int sizeY) {
        //Initialize all class variables
        this.sizeX = sizeX;
        this.sizeY = sizeY;
        wormWorldParty = new boolean[sizeX][sizeY]; //wormWorldParty is a 2d array of sizeX by sizeY


    }

    private int sizeX;
    private int sizeY;

    boolean[][] wormWorldParty;

    public int getSizeX() {
        return sizeX;
    }
    public int getSizeY() {
        return sizeY;
    }
    public boolean getCell(int x, int y) {
        return wormWorldParty[x][y];

        //true if cell is alive false otherwise
    }

    //adds a pattern to the world
    public void insertPattern(Pattern pattern, int startX, int startY) {
        //upper left corner starts at startX and startY
        //copy the cell values from the pattern into wormWorldParty

        for (int x = 0; x < pattern.getSizeX(); x++) {
            for (int y = 0; y < pattern.getSizeY(); y++) {

                wormWorldParty[startX+x][startY+y] = pattern.getCell(x,y);


            }

        }
    }
    public void update() {
        //Make a new grid the same size as wormWorldParty(read only)
        //For each cell decide new state of that cell
        boolean[][] psudowormWorldParty = new boolean[sizeX][sizeY];
        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                psudowormWorldParty[x][y] = wormNextGenCheck(x,y);
            }

        }
        wormWorldParty = psudowormWorldParty;

    }

    private boolean wormNextGenCheck(int x,int y) {

        int leftX = x-1;
        int rightX = x+1;
        int upY = y-1;
        int downY = y+1;
        if (x-1 < 0){
            leftX = sizeX-1;
        }
        if (x+1 > sizeX-1){
            rightX = 0;
        }
        if (y-1 < 0){
            upY = sizeY-1;
        }
        if (y+1 > sizeY-1){
            downY = 0;
        }


        int liveCells = 0;

        if (getCell(leftX,upY)) {
            liveCells++;
        }
        if (getCell(leftX,y)) {
            liveCells++;
        }
        if (getCell(x,upY)) {
            liveCells++;
        }
        if (getCell(rightX,downY)) {
            liveCells++;
        }
        if (getCell(rightX,y)) {
            liveCells++;
        }
        if (getCell(x,downY)) {
            liveCells++;
        }
        if (getCell(leftX,downY)) {
            liveCells++;
        }
        if (getCell(rightX,upY)) {
            liveCells++;
        }
        if (getCell(x,y)){
            if (liveCells == 2 || liveCells == 3){
                    return true;
                }
            }
        else{
            if (liveCells == 3){
                return true;
            }

        }
        return false;

//    bros = []
//            for length in range(-1, 2):
//            for height in range(-1, 2):
//    broLength = lengthCheck + length
//            broHeight = heightCheck + height
//    trueBros = True
//                if broLength == lengthCheck and broHeight == heightCheck:
//    trueBros = False
//                if broLength < 0 or broLength >= self.length:
//    trueBros = False
//                if broHeight < 0 or broHeight >= self.height:
//    trueBros = False
//                if trueBros:
//            bros.append(self.board[broLength][broHeight])
//
//    Any live cell with two or three live neighbours survives.
//    Any dead cell with three live neighbours becomes a live cell.
//    All other live cells die in the next generation. Similarly, all other dead cells stay dead.

        //Add new cell state in new grid
        //set wormWorldParty to refer to new grid
    }
};

//class Board:
//    def __init__(self, length, height):
//    self.length = length
//    self.height = height
//    self.board = [[Cell() for lengthBros in range(self.length)] for heightBros in range(self.height)]  # Matrix example from
//        self.creatBoard()
//
//    def printBoard(self):
//    print("\n\n\n\n\n\n\n\n\n         Game of life!")
//        for height in self.board:
//            for length in height:
//    print(length.cellPicture(), end=" ")
//    print()
//
//    def creatBoard(self):
//            for height in self.board:
//            for width in height:
//    percentChance = random.randint(0, 2)
//            if percentChance == 1:
//            width.reviveCell()
//
//    def broCheck(self, lengthCheck, heightCheck):
//    bros = []
//            for length in range(-1, 2):
//            for height in range(-1, 2):
//    broLength = lengthCheck + length
//            broHeight = heightCheck + height
//    trueBros = True
//                if broLength == lengthCheck and broHeight == heightCheck:
//    trueBros = False
//                if broLength < 0 or broLength >= self.length:
//    trueBros = False
//                if broHeight < 0 or broHeight >= self.height:
//    trueBros = False
//                if trueBros:
//            bros.append(self.board[broLength][broHeight])
//
//
//
//            return bros