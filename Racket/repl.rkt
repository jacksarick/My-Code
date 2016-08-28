#!/usr/local/bin/racket
#lang racket

(define-namespace-anchor anchored-namespace)
(define repl-namespace (namespace-anchor->namespace anchored-namespace))

(define eval+
	(λ (input)
		; Setup error message
		(with-handlers ([exn:fail:contract?
			; Return error message
			(lambda (exn) (display exn))])
			(case (eof-object? input)
				[(#t) (write 'goodbye!) (exit)]
				; eval statement
				[else (eval input repl-namespace)]))))

(define repl
	(λ ()
		; Show prompt
		(display "↳ ")
		; Display input
		(displayln (eval+ (read)))
		; Repeat
		(repl)))

(repl)