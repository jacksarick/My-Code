#lang racket/gui

;;;;;;;;;;;;;;;;;;;;;;;;;
;;; GENERAL FUCNTIONS ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;

;Macro for 'defn'
;;macro (define (λ () ...)) -> (defn () ...)
(define-syntax-rule (defn name args body...)
  (define name
    (λ args
      body...)))

;Macro for renaming function
;;macro (defn x a (y a)) -> (alt y x)
(define-syntax-rule (alt old new)
	(defn new args (apply old args)))

;For (x y) returns ((+ x y) y)
;; (value increment) -> (new-value increment)
(defn update (x)
  (list (+ (car x) (cadr x)) (cadr x)))

;Function for degrees to radians
;; degrees -> radians
(defn rad (x)
  (* x (/ pi 180)))

;Rotates a point around another point
;; point, distance from centre, function, rotation -> new point
(defn transform (p d f r)
  (+ p (* d (f (rad r)))))

;;alt transform -> tform
(alt transform tform)

;Function to draw a circle with centre at (x y)
;; context, x coord , y coord, radius -> nil
(defn draw-circle (dc x y r)
  (send dc draw-ellipse (- x ( / r 2)) (- y ( / r 2)) r r))

;;;;;;;;;;;;;;;;;;;;;;
;;; GAME FUNCTIONS ;;;
;;;;;;;;;;;;;;;;;;;;;;

;Draw our character
;; context, x coord, y coord, radius, rotation -> nil
(defn draw-char (dc x y d r)
  ;Define a radius
  (let ([radius 30])

    ;Draw the char at center (x, y)
    (send dc set-pen   "black" 1 'solid)
    (send dc set-brush "black"   'solid)
    (draw-circle dc (tform x d sin (+ r   0)) (tform y d cos (+ r   0)) radius)
    (draw-circle dc (tform x d sin (+ r 120)) (tform y d cos (+ r 120)) radius)
    (draw-circle dc (tform x d sin (+ r 240)) (tform y d cos (+ r 240)) radius)))

;Function triggered on key stroke
;; racket-event -> nil
(defn key-stroke (event)
  (let ([action (send event get-key-code)])
    (match action
    ['up    (set! char-d (list (+ (car char-d) 5)))]
    ['down  (set! char-d (list (- (car char-d) 5)))]
    ['left  (set! char-r (list (car char-r) (+ (cadr char-r) .25)))]
    ['right (set! char-r (list (car char-r) (- (cadr char-r) .25)))]
    ['release null]
    [_ (displayln action)])))

;;;;;;;;;;;;;;;;;;;;;;;;
;;; WINDOW FUCNTIONS ;;;
;;;;;;;;;;;;;;;;;;;;;;;;

;Function that is run every tick
;; canvas, context -> nil
(defn game-tick (canvas dc)
  (begin
    ;Clear the board
    (send dc erase)
  
    ;Draw the character
    (draw-char dc (car char-x) (car char-y) (car char-d) (car char-r))))

;Define our character's stats
(define char-x '(250 0))
(define char-y '(250 0))
(define char-d '(50)   )
(define char-r '(90  2))

;Define a window
(define frame (new frame%
  [label "Triple Helix"]
  [width 500]
  [height 500]))

;Define a new general canvas class
(define custom-canvas%
  (class canvas%
  
  (define/override (on-char event)
    (key-stroke event))
  
  (super-new)))

;Define a canvas
(define canvas (new custom-canvas% [parent frame]
  [paint-callback game-tick]))

;Define our game loop to update 60 times per second
(defn loop ()
  (begin
    ;Update our character
    (set! char-x (update char-x))
    (set! char-y (update char-y))
    (set! char-r (list (+ (car char-r) (cadr char-r)) (cadr char-r)))
    
    (send canvas on-paint)
    (sleep/yield (/ 1 60))
    (loop)))


;;;;;;;;;;;;
;;; MAIN ;;;
;;;;;;;;;;;;

;Show the window
(send frame show #t)

;Start the game
(loop)