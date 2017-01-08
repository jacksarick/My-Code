#lang racket/base

(define-syntax-rule (defn name args body...)
	(define name
		(λ args body...)))

(defn subtract (x y)
	(- x y))

(subtract 10 5)