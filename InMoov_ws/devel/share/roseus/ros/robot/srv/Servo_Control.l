;; Auto-generated. Do not edit!


(when (boundp 'robot::Servo_Control)
  (if (not (find-package "ROBOT"))
    (make-package "ROBOT"))
  (shadow 'Servo_Control (find-package "ROBOT")))
(unless (find-package "ROBOT::SERVO_CONTROL")
  (make-package "ROBOT::SERVO_CONTROL"))
(unless (find-package "ROBOT::SERVO_CONTROLREQUEST")
  (make-package "ROBOT::SERVO_CONTROLREQUEST"))
(unless (find-package "ROBOT::SERVO_CONTROLRESPONSE")
  (make-package "ROBOT::SERVO_CONTROLRESPONSE"))

(in-package "ROS")





(defclass robot::Servo_ControlRequest
  :super ros::object
  :slots (_angle ))

(defmethod robot::Servo_ControlRequest
  (:init
   (&key
    ((:angle __angle) 0)
    )
   (send-super :init)
   (setq _angle (round __angle))
   self)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:serialization-length
   ()
   (+
    ;; uint16 _angle
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _angle
       (write-word _angle s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _angle
     (setq _angle (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(defclass robot::Servo_ControlResponse
  :super ros::object
  :slots (_success ))

(defmethod robot::Servo_ControlResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass robot::Servo_Control
  :super ros::object
  :slots ())

(setf (get robot::Servo_Control :md5sum-) "914915d0b64fe2ea004b3cbed7ecc77f")
(setf (get robot::Servo_Control :datatype-) "robot/Servo_Control")
(setf (get robot::Servo_Control :request) robot::Servo_ControlRequest)
(setf (get robot::Servo_Control :response) robot::Servo_ControlResponse)

(defmethod robot::Servo_ControlRequest
  (:response () (instance robot::Servo_ControlResponse :init)))

(setf (get robot::Servo_ControlRequest :md5sum-) "914915d0b64fe2ea004b3cbed7ecc77f")
(setf (get robot::Servo_ControlRequest :datatype-) "robot/Servo_ControlRequest")
(setf (get robot::Servo_ControlRequest :definition-)
      "uint16 angle
---
bool success
")

(setf (get robot::Servo_ControlResponse :md5sum-) "914915d0b64fe2ea004b3cbed7ecc77f")
(setf (get robot::Servo_ControlResponse :datatype-) "robot/Servo_ControlResponse")
(setf (get robot::Servo_ControlResponse :definition-)
      "uint16 angle
---
bool success
")



(provide :robot/Servo_Control "914915d0b64fe2ea004b3cbed7ecc77f")


