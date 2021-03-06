package main;

import javax.swing.Timer;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;

public class gameFrame extends JFrame{
	private static final long serialVersionUID = 1L;
	public static int HEIGHT = 300;
	public static int WIDTH = 400;
	
	private static Timer timer;
	
	public gameFrame(){
		this.setSize(WIDTH, HEIGHT);
		this.setVisible(true);
		this.setResizable(false);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	
	public static void main(String args[]){
		gameFrame frame = new gameFrame();
		final gamePanel panel = new gamePanel();
		frame.setTitle("My Title");
		frame.getContentPane().add(panel);
		timer = new Timer(16, new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				panel.repaint();
			}
		});
		timer.start();
	}
}
