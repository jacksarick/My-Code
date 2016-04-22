(defun fizzy (num)
	(cond ((zerop (+ (mod num 5) (mod num 3))) "FizzBuzz")
		( (zerop (mod num 3)) "Fizz")
		( (zerop (mod num 5)) "Buzz")
		(t num)))

(print
	(mapcar #'fizzy (cdr (loop for i upto 10 collect i)))
)