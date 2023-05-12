public class Dwarf implements Comparable<Dwarf>{
    private static int count = 0;
    private String name;
    private int which;

    public Dwarf(String name){
        this.name = name;
        which = count++;
    }
    @Override
    public int compareTo(Dwarf d){
        return (this.name.compareTo( d.name));
    }

    @Override
    public String toString(){
        return  String.format("%s[%d]", name, which);
    }
}
