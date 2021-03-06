package main;

import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JPanel;

public class gamePanel extends JPanel implements KeyListener{

	private int playerX = 10;
	private int playerY = 10;
	private float velocityX = 0;
	private float velocityY = 0;
	
	//default constructor
	public gamePanel() {
		
		this.setSize(800,600);
		this.setVisible(true);
		this.addKeyListener(this);
		this.setFocusable(true);
		
	}
	
	@Override
	public void paint(Graphics g){
		playerX += velocityX;
		playerY += velocityY;
		velocityX *= .9;
		velocityY += .09;
		g.fillOval(playerX, playerY, 30, 30);
		
	}

	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyPressed(KeyEvent e) {
		int key = e.getKeyCode();
		switch(key){
			case 37:
				velocityX -= 1;
				break;
			case 39:
				velocityX += 1;
				break;
			case 40:
				velocityY -= 9;
				break;
		}
		repaint();
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}
	
}
