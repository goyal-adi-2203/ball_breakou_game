
import java.awt.*;

public class Map_Gen {
    public int map[][];
    public int brick_wid;
    public int brick_hei;

    public Map_Gen(int row,int col) {
        map = new int[row][col];

        for(int []map1 : map){
            for(int j=0; j <map[0].length;j++){
                map1[j] = 1;
            }
        }

        brick_wid = 540/col;
        brick_hei = 540/row;

    }

}
