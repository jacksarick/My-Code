#lang racket

; Macro for (define (lambda ...))
(define-syntax-rule (defn name args body)
  (define name
    (λ args
      body)))

; (defn len (arr)
;   (apply + (map (lambda (x) (if (list? x) (len x) 1)) arr)))

; (defn transform (equation)
;   (zip equation (map '. equation)))

(apply equation)