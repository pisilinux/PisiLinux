--- clisp-2.49.orig/src/init.lisp
+++ clisp-2.49/src/init.lisp
@@ -1570,6 +1570,10 @@
       (apply #'format *error-output* format-string args)
       (elastic-newline *error-output*)
       nil))))
+
+(unless (fboundp 'ext::muffle-cerrors) ; predef for bootstrap
+  (sys::%putd 'ext::muffle-cerrors #'identity))
+
 (defun open-for-load (filename extra-file-types external-format
                       &aux stream (present-files t) obj path bad-file)
  (block open-for-load
@@ -1639,11 +1643,12 @@
         ;; File with precisely this name not present OR bad
         ;; Search among the files the most recent one
         ;; with the same name and the Extensions "LISP", "FAS":
-        (setq present-files (search-file filename
-                                         (append extra-file-types
+        (setq present-files
+              (ext::muffle-cerrors ; ignore encoding errors in DIRECTORY
+               (search-file filename (append extra-file-types 
                                                  *compiled-file-types*
                                                  *source-file-types*)
-                                         nil)))
+                            nil))))
       (if present-files
         ;; proceed with the next present file
         (setq path (car present-files) present-files (cdr present-files)
