#lang racket/base

;Macro for 'defn'
;;macro (define (λ () ...)) -> (defn () ...)
(define-syntax-rule (defn name args body)
  (define name
    (λ args
      body)))

(defn subtract (x y)
  (println "subtracting...")
  (- x y))

(subtract 10 5)

;Macro for renaming function
(define-syntax-rule (alt new old)
	(defn new args (apply old args)))

(alt subs subtract)

(subs 20 10)