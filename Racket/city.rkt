#lang racket/gui

;;;;;;;;;;;;
;;; INFO ;;;
;;;;;;;;;;;;

;* Made by Jack Sarick
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

;Sum of a list
;; '(x y z) -> (+ x y z)
(defn sum (l)
  (apply + l))

;Add vectors
;; '(a b), '(x y) -> '((+ a x) (+ b y))
(defn vsum (v1 v2)
  (map + v1 v2))

;Between function
;; min, var, max -> bool
(defn between (l x m)
  (and (< l x) (> m x)))

;;;;;;;;;;;;;;;;;;;;;
;;; SIM FUNCTIONS ;;;
;;;;;;;;;;;;;;;;;;;;;

(defn draw-iso-square (o l)
	)

;;;;;;;;;;;;;;;;;;;;;;;;
;;; WINDOW FUCNTIONS ;;;
;;;;;;;;;;;;;;;;;;;;;;;;

;Function that is run every tick
;; canvas, dc -> null
(defn tick (canvas dc)
  (begin
    ;Clear the board
    (send dc set-background (make-object color% 45 45 50))
    (send dc clear)))

;Define a window
(define frame (new frame%
  [label "My City"]
  [width  500]
  [height 500]))


;Define a canvas
(define canvas (new canvas% [parent frame]
  [paint-callback tick]))

;Define our loop to update 60 times per second
(defn loop ()
  (begin

    
    (send canvas on-paint)
    (sleep/yield (/ 1 60))
    (loop)))

;;;;;;;;;;;;
;;; MAIN ;;;
;;;;;;;;;;;;

;Show the window
(send frame show #t)

;Start the sim
(loop)