#lang racket

(define list '(1 2 (3 4 (5 6)) 7 8 (9 10)))

; 1: Find the last element of a list
(define lst
	(lambda (x)
		(if (= 1 (length x))
			(car x)
			(lst (cdr x)))))

; 2: Find the last but one element of a list
(define lst-2
	(λ (x)
		(if (> (length x) 1)
			(if (= 2 (length x))
				(car x)
				(lst-2 (cdr x)))
			(error "Wrong size list"))))

; 3: Find the Kth element of a list
;; It doesn't not work, it just does it backwards
(define lst-k
	(λ (x k)
		(if (= k (length x))
			(car x)
			(lst-k (cdr x) k))))

; 4: Find the number of elements of a list
(define len
	(λ (x [y 0])
		(if (= 0 (length x))
			y
			(len (cdr x) (+ y 1)))))

; 5: Reverse a list
(define rev
	(λ (x [y '()])
		(if (= 0 (length x))
			y
			(rev (cdr x) (cons (car x) y)))))

; 6: Find out whether a list is a palindrome
(define palindrome
	(λ (x)
		(equal? x (rev x))))

; 7: Flatten a nested list structure
;; HAHAHAH IDK
(define flatten
	(λ (x)
		; If it contains no lists
		(while (andmap list? x)
			; Combine the first item of x and the second
			()
			; Else return x
			(car x))))

(write (palindrome list))