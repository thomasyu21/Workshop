;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;nth-factorial function
(define fact
  (lambda
      (n)
    (if (= n 0)
        1
        (* n (fact (- n 1))))))

(fact 0)
(fact 1)
(fact 2)
(fact 3)
(fact 4)
(fact 5)

;nth-fibonacci function
(define fib
  (lambda (n)
    (if (<= n 1)
        n
        (+ (fib(- n 1)) (fib (- n 2))))))

(fib 0)
(fib 1)
(fib 2)
(fib 3)
(fib 4)
(fib 5)
(fib 6)