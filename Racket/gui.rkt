#lang racket
(require racket/gui/base)

(define f (new frame% [label "Simple Edit"]
	[width 800]
	[height 600]))
(define c (new editor-canvas% [parent f]))
(define t (new text%))
(define mb (new menu-bar% [parent f]))
(define m-edit (new menu% [label "Edit"] [parent mb]))

(append-editor-operation-menu-items m-edit #f)

(send c set-editor t)
(send f show #t)
