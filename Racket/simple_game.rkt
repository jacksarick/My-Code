#lang racket/gui

;Function for radian -> degrees
(define rad
  (lambda (x)
    (* x (/ pi 180))))

;Make a window
(define frame (new frame%
                   [label "Game"]
                   [width 500]
                   [height 500]))

(define char-x 100)
(define char-y 100)
(define char-r   0)

;Draw our character
(define draw-char
  (lambda (dc x y d)
    
    ;Clear the board
    (send dc erase)

    ;Define a radius
    (let ([radius 30])
      ;Draw the char at center (x, y)
      (send dc draw-ellipse (- x ( / radius 2)) (- y ( / radius 2)) radius radius))
    ;Draw char view
    (let ([vision 40]
          [r (rad (- 180 d))])
      (send dc draw-line
            x y
            (+ x (* (sin r) vision)) (+ y (* (cos r) vision))))))

;Keystroke event
(define keystroke
  (lambda (key)
    (display "event")
    (set! char-x (+ char-x 10))
    (display "redraw")))

(define canvas (new canvas% [parent frame]
             [paint-callback
              (lambda (canvas dc)
                (draw-char dc char-x char-y char-r))]))

(send canvas on-event keystroke)
(send frame show #t)