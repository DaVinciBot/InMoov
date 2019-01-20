
(cl:in-package :asdf)

(defsystem "servo_control_msg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Servo_Control" :depends-on ("_package_Servo_Control"))
    (:file "_package_Servo_Control" :depends-on ("_package"))
  ))