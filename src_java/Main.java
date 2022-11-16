package src_java;

import javax.swing.JFrame;

public class Main {
    public static void main(String[] args) {
        Game_play gp = new Game_play();
        JFrame jf = new JFrame();

        jf.setBounds(10,10,700,600);
        jf.setTitle("BREAKOUT");
        jf.setResizable(false);
        jf.setVisible(true);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.add(gp);
    }
    
}