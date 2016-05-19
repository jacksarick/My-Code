(defun rev (data)
	(if data					; If the list is not empty...
		(append					; join...
			(rev (cdr data))	; reverse the rest
			(list (car data)))	; the head.
		nil))					; else do nothing

(print (rev '(1 2 3 4 5 6)))