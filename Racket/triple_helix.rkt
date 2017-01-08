#lang racket/gui

;;;;;;;;;;;;
;;; INFO ;;;
;;;;;;;;;;;;

;* Made by Jack Sarick

;* TODO:
;* [ ] Make expand/contract velocity based (like spinning) (maybe)
;* [ ] Add obstacles
;* [ ] Add score system
;* [ ] Make docs

;* dc is shorthand for "drawing context"

;;;;;;;;;;;;;;;;;;;;;;;;;
;;; GENERAL FUCNTIONS ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;

;Macro for 'defn'
;;macro (define (λ () ...)) -> (defn () ...)
(define-syntax-rule (defn name args body)
  (define name
    (λ args
      body)))

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

;Rotates a half-point around another half-point (helper for transform)
;; half-point, distance from centre, function, rotation -> new half-point
(defn half-transform (p d f r)
  (+ p (* d (f (rad r)))))

;Rotates point around another-point
;; (x, y), distance from centre, rotation -> new (x, y)
(defn transform (p d r)
  (list
    (half-transform (car p)  d sin r)
    (half-transform (cadr p) d cos r)))

;;alt transform -> tform
(alt transform tform)

;Function to draw a circle with centre at (x y)
;; dc, x coord , y coord, radius -> null
(defn draw-circle (dc p r)
  (let ([x (car p)]
        [y (cadr p)])
  (send dc draw-ellipse (- x ( / r 2)) (- y ( / r 2)) r r)))

;;;;;;;;;;;;;;;;;;;;;;
;;; GAME FUNCTIONS ;;;
;;;;;;;;;;;;;;;;;;;;;;

;Draw our character
;; dc, x coord, y coord, radius, rotation -> null
(defn draw-char (dc x y d r)
  ;Define a radius
  (let ([radius 30]
        [point (list x y)])

    ;Draw the char at center (x, y)
    (send dc set-pen   "black" 1 'solid)
    (send dc set-brush "black"   'solid)
    (draw-circle dc (tform point d (+ r   0)) radius)
    (draw-circle dc (tform point d (+ r 120)) radius)
    (draw-circle dc (tform point d (+ r 240)) radius)))

;Draw obstacle
;; dc, (x, y) -> null
(defn draw-obstacle (dc p)
  null)

;Draw obstacles
;; dc, list of (x, y) -> null
(defn draw-obstacles (dc obs-list)
  (begin
    (send dc set-pen   "black" 1 'solid)
    (send dc set-brush "black"   'solid)
    (map draw-obstacle obs-list)))

;Function triggered on key stroke
;; racket-event -> null
(defn key-stroke (event)
  (let ([action (send event get-key-code)])
    (match action
    ['up    (set! char-d (list (+ (car char-d) 5)))]
    ['down  (set! char-d (list (- (car char-d) 5)))]
    ['left  (set! char-r (list (car char-r) (+ (cadr char-r) .25)))]
    ['right (set! char-r (list (car char-r) (- (cadr char-r) .25)))]
    [_ null])))

;;;;;;;;;;;;;;;;;;;;;;;;
;;; WINDOW FUCNTIONS ;;;
;;;;;;;;;;;;;;;;;;;;;;;;

;Function that is run every tick
;; canvas, dc -> null
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