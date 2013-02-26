;; enable erlang-mode.

(setq erlang-root-dir "/usr/")
(setq exec-path (cons "/usr/bin" exec-path))

(add-to-list 'load-path "/usr/share/emacs/site-lisp/erlang/")
(require 'erlang-start)
