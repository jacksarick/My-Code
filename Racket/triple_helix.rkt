#lang racket/gui

;Function for degrees -> radians
;; degrees -> radians
(define rad
  (lambda (x)
    (* x (/ pi 180))))

;Rotates a point around another point
;; point, distance from centre, function, rotation -> new point
(define transform
  (lambda (p d f r)
    (+ p (* d (f (rad (+ r)))))))

;Function to draw a circle with centre at (x, y)
;; target, x coord , y coord, radius -> void
(define draw-circle
  (lambda (dc x y r)
    (send dc draw-ellipse (- x ( / r 2)) (- y ( / r 2)) r r)))

;Draw our character
;; target, x coord, y coord, distance of circle from centre, rotation of charachter -> void
(define draw-char
  (lambda (dc x y d r)
    
    ;Clear the board
    (send dc erase)

    ;Define a radius
    (let ([radius 30])
      
      ;Draw the char at center (x, y)
      (send dc set-pen "black" 1 'solid)
      (send dc set-brush "black" 'solid)
      (draw-circle dc (transform x d sin (+ r   0)) (transform y d cos (+ r   0)) radius)
      (draw-circle dc (transform x d sin (+ r 120)) (transform y d cos (+ r 120)) radius)
      (draw-circle dc (transform x d sin (+ r 240)) (transform y d cos (+ r 240)) radius))))

;Function that is run every tick
(define game-tick
  (lambda (canvas dc)
                (draw-char dc char-x char-y char-d char-r)))

;Define our character's stats
(define char-x 250)
(define char-y 250)
(define char-d  50)
(define char-r  90)

;Define a window
(define frame (new frame%
                   [label "Triple Helix"]
                   [width 500]
                   [height 500]))

;Define a canvas
(define canvas (new canvas% [parent frame]
             [paint-callback game-tick]))

;Define our game loop to update 40 times per second
(define (loop)
  (send canvas on-paint)
  (set! char-r (+ char-r 2))
  (sleep/yield (/ 1 60))
  (loop))

(send frame show #t)

(loop)