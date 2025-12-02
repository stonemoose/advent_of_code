(define (parse-file port)
  (define (parse-line line)
    (list
      (substring line 0 1)
      (string->number (substring line 1 (string-length line)))))

  (define (read-file-inner)
    (let ((line (read-line port)))
      (if (eof-object? line)
        '()
        (cons (parse-line line) (read-file-inner)))))
  (read-file-inner))

(define (read-file file-name)
  (call-with-input-file file-name parse-file))


(define (solve input)
  (define (turn-dial turn position)
    (define (inner-turn amount position zeros)
      (if (zero? amount)
        (list position zeros)
        (inner-turn
          (- amount 1)
          (modulo
            ((if (string=? (car turn) "L") - +) position 1)
          100)
          (+ zeros (if (zero? position) 1 0)))))
    (inner-turn (cadr turn) position 0))



  (define (find-password position password zeros remaining-turns)
    (if (null? remaining-turns)
      (list (+ password (if (zero? position) 1 0)) zeros)
        (let ((pos-zeros (turn-dial (car remaining-turns) position)))
          (find-password
            (car pos-zeros)
            (+ password (if (zero? position) 1 0))
            (+ zeros (cadr pos-zeros))
            (cdr remaining-turns)))))
  (find-password 50 0 0 input))


(display "Solutions: ")
(display (solve (read-file "input.txt"))) (newline)
