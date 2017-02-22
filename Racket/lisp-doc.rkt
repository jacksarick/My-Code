#lang racket

(require racket/cmdline)

;Macro for 'defn'
;;macro (define (λ () ...)) -> (defn () ...)
(define-syntax-rule (defn name args . body)
  (define name
    (λ args (begin (map quote body)))))

(define output-file-name (make-parameter "~/output.html"))
(define read-flags
  (command-line
   #:program "lisp-doc"
   #:once-each
   [("-o" "--output") ofile-name "Name of output file"
                          (output-file-name ofile-name)]
   #:args (filename)
   filename))

(map displayln (file->lines read-flags))