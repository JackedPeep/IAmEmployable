import java.util.*;

public class WordFreqInfo {
    private String word;
    private int occurCount;
    private ArrayList<Frequency> followList;

    public WordFreqInfo(String word, int count) {
        this.word = word;
        this.occurCount = count;
        this.followList = new ArrayList<Frequency>();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Word :" + word+":");
        sb.append(" (" + occurCount + ") : ");
        for (Frequency f : followList) {
            sb.append(f.toString());
        }

        return sb.toString();
    }

    public void updateFollows(String follow) {
        this.occurCount++;
        boolean updated = false;
        for (Frequency f : followList) {
            if (follow.compareTo(f.follow) == 0) {
                f.followCount++;
                updated = true;
            }
        }
        if (!updated) {
            followList.add(new Frequency(follow, 1));
        }
    }
    public String getFollowWord(int count){
        if(count > occurCount) {
            return "ERROR: The count has exceeded its range. This shouldn't happen";
        }

        for (int i = 0; count >= 0; i++) {
            count -= followList.get(i).followCount;
//            System.out.print(count+" ");
            if(count <= 0){
//                System.out.println(followList.get(i).follow);
                return followList.get(i).follow;
            }
        }

        return "ERROR; Something went horribly WRONG!!!";

    }

    public int getOccurCount() {
        return this.occurCount;
    }

    private class Frequency {
        String follow;
        int followCount;

        public Frequency(String follow, int ct) {
            this.follow = follow;
            this.followCount = ct;
        }

        @Override
        public String toString() {
            return follow + " [" + followCount + "] ";
        }

        @Override
        public boolean equals(Object f2) {
            return this.follow.equals(((Frequency)f2).follow);
        }
    }
}
