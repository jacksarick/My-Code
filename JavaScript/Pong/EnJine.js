			/*
				Jack's magical JS engine!
				Notes: 
					- add "r" to the front of functions to set them to robust
			*/
			var canvas;
			var ctx;
			var GameObjects = [];

			//Simple setup-types
			//-Simple object maker
			//-- X position, Y position, height, width, x velocity, y velocity
			function newObj (xPos,yPos,xh,yw,v1,v2) {
				//gravity, x/y maxspeed, x/y friction are both default 
				tempObj = {x:xPos, y:yPos, h:xh, w:yw, vx:v1, vy:v2, 
					g:0, fx:0.98, fy:0.98, xmv:7, ymv:7};
				//GameObjects[GameObjects.length] = tempObj;
				return tempObj;
			}

			//-random int function
			function randint (min, max) {
				return Math.floor(Math.random() * (max - min + 1)) + min;
			}

			//-clears canvas
			function clear(colour) {
				ctx.clearRect(0, 0, WIDTH, HEIGHT);
				rect({x:0,y:0,w:WIDTH,h:HEIGHT}, colour, colour);
			}

			//-generate rectangle from object
			//--Leave cOut as 0 to set them as the same
			function Orect(objectIn,cOut,cIn) {
				ctx.strokeStyle = cOut;
				ctx.fillStyle = cIn;
				ctx.beginPath();
				ctx.rect(objectIn.x,
						objectIn.y,
						objectIn.w,
						objectIn.h);
				ctx.closePath();
				ctx.fill();
				ctx.stroke();
			}
			//generate simple rectangle
			function rect(w,h,x,y,colour) {
				ctx.strokeStyle = colour;
				ctx.fillStyle = colour;
				ctx.beginPath();
				ctx.rect(x, y, w, h);
				ctx.closePath();
				ctx.fill();
				ctx.stroke();
			}

			//Slightly more complex behind the scenes math
			//-Simple collision detection
			function checkCol (object1, object2) {
				if (!(
					((object2.y + object2.h) < object1.y ) ||
					(object2.y  > (object1.y + object1.h)) ||
					((object2.x + object2.w) < object1.x ) ||
					(object2.x  > (object1.x + object1.w))
					)){
					return true;
				}
				else {
					return false;
				}
			}

			//-velocity-based movement
			function rmovement (object, friction, bounds, bounce) {
				//object will stop upon colliding with a wall
				object.vx *= friction;
				object.vy *= friction;
				
				// Y movement
				if (!(
					((object.y + object.vy + object.h) > bounds.d) || 
					((object.y + object.vy) < bounds.u)

					)){ 
					object.y += object.vy; 
				}

				else {
					object.vy *= -bounce; 
				}

				// X movement
				if (!(
					((object.x + object.vx + object.w) > bounds.r) || 
					((object.x + object.vx) < bounds.l)

					)){ 
					object.x += object.vx; 
				}

				else {
					object.vx *= -bounce; 
				}
			}

			//-simplified movement. doesnt allow charachter to go off screen
			function movement (object) {
				rmovement(object, world.friction, {h:0,d:HEIGHT,l:0,r:WIDTH}, world.bounce);
			}

			// This function updates all objects position in game unless told otherwise
			// function update(){
			// 	for(item in GameObjects){

			// 	}
			// }