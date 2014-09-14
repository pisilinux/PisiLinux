
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Default configuration file for GNU/Emacs on Pisi Linux ;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(setq column-number-mode t)                  ; show column numbers below

(display-time-mode t)                        ; display time below

(show-paren-mode t)                          ; show parenthesis

(transient-mark-mode t)                      ; show mark visually...

;; (setq make-backup-files nil)              ; no nasty back-up files

(setq-default show-trailing-whitespace t)    ; show trailing whitespace

(setq frame-title-format "%b (%m)")          ; descriptive frame title "filename (mode)"

(setq scroll-step 1)                         ; scroll one line at a time

(setq load-path (cons "~/.elisp" load-path)) ; add ~/.elisp as a custom load path

(set-face-foreground 'font-lock-comment-face "red") ; show comments in red

(set-scroll-bar-mode 'right) ; show scrollbar on the right

;; use ibuffer by default
(global-set-key (kbd "C-x C-b") 'ibuffer)
(autoload 'ibuffer "ibuffer" "List buffers." t)


;; for zpspell
(setq ispell-program-name "zpspell")
(setq ispell-local-dictionary-alist
              `((nil
              "[A-ZŞĞIa-zşğı]"
              "[^A-ZŞĞIa-zşğı]"
              "[']" nil ("") "~utf-8" utf-8)))


;; Autoload init files under /etc/emacs/site-lisp
(defun pardus-auto-load-all ()
  "Autoload all init files under /etc/emacs/site-lisp"
  (mapcar '(lambda (f)
             (if (pardus-file-or-symlink-exists-p f)
                 (load f)
               nil))
          (sort
           (el-files-in-directory "/etc/emacs/site-lisp/")
           'string-lessp)))

(defun pardus-file-or-symlink-exists-p (f)
  "Check if file or symlink exists"
  (let ((f-symlink-target (file-symlink-p f)))
    (if f-symlink-target
        (let ((f-symlink-target-path
               (concat (file-name-directory f) f-symlink-target)))
          (if (file-exists-p f-symlink-target-path)
              t
            nil))
      (file-exists-p f))))

(defun el-files-in-directory (directory)
  "List the .el files in DIRECTORY and in its sub-directories."
  (let (el-files-list
        (current-directory-list
         (directory-files-and-attributes directory t)))
    ;; while we are in the current directory
    (while current-directory-list
      (cond
       ;; check to see whether filename ends in `.el'
       ;; and if so, append its name to a list.
       ((equal ".el" (substring (car (car current-directory-list)) -3))
        (setq el-files-list
              (cons (car (car current-directory-list)) el-files-list)))
       ;; check whether filename is that of a directory
       ((eq t (car (cdr (car current-directory-list))))
        ;; decide whether to skip or recurse
        (if
            (equal (or "." "..")
                   (substring (car (car current-directory-list)) -1))
            ;; then do nothing if filename is that of
            ;;   current directory or parent
            ()
          ;; else descend into the directory and repeat the process
          (setq el-files-list
                (append
                 (el-files-in-directory
                  (car (car current-directory-list)))
                 el-files-list)))))
      ;; move to the next filename in the list; this also
      ;; shortens the list so the while loop eventually comes to an end
      (setq current-directory-list (cdr current-directory-list)))
    ;; return the filenames
    el-files-list))
