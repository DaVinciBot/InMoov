;; Auto-generated. Do not edit!


(when (boundp 'servo_control_msg::Servo_Control)
  (if (not (find-package "SERVO_CONTROL_MSG"))
    (make-package "SERVO_CONTROL_MSG"))
  (shadow 'Servo_Control (find-package "SERVO_CONTROL_MSG")))
(unless (find-package "SERVO_CONTROL_MSG::SERVO_CONTROL")
  (make-package "SERVO_CONTROL_MSG::SERVO_CONTROL"))
(unless (find-package "SERVO_CONTROL_MSG::SERVO_CONTROLREQUEST")
  (make-package "SERVO_CONTROL_MSG::SERVO_CONTROLREQUEST"))
(unless (find-package "SERVO_CONTROL_MSG::SERVO_CONTROLRESPONSE")
  (make-package "SERVO_CONTROL_MSG::SERVO_CONTROLRESPONSE"))

(in-package "ROS")





(defclass servo_control_msg::Servo_ControlRequest
  :super ros::object
  :slots (_angle ))

(defmethod servo_control_msg::Servo_ControlRequest
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

(defclass servo_control_msg::Servo_ControlResponse
  :super ros::object
  :slots (_success ))

(defmethod servo_control_msg::Servo_ControlResponse
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

(defclass servo_control_msg::Servo_Control
  :super ros::object
  :slots ())

(setf (get servo_control_msg::Servo_Control :md5sum-) "914915d0b64fe2ea004b3cbed7ecc77f")
(setf (get servo_control_msg::Servo_Control :datatype-) "servo_control_msg/Servo_Control")
(setf (get servo_control_msg::Servo_Control :request) servo_control_msg::Servo_ControlRequest)
(setf (get servo_control_msg::Servo_Control :response) servo_control_msg::Servo_ControlResponse)

(defmethod servo_control_msg::Servo_ControlRequest
  (:response () (instance servo_control_msg::Servo_ControlResponse :init)))

(setf (get servo_control_msg::Servo_ControlRequest :md5sum-) "914915d0b64fe2ea004b3cbed7ecc77f")
(setf (get servo_control_msg::Servo_ControlRequest :datatype-) "servo_control_msg/Servo_ControlRequest")
(setf (get servo_control_msg::Servo_ControlRequest :definition-)
      "uint16 angle
---
bool success
")

(setf (get servo_control_msg::Servo_ControlResponse :md5sum-) "914915d0b64fe2ea004b3cbed7ecc77f")
(setf (get servo_control_msg::Servo_ControlResponse :datatype-) "servo_control_msg/Servo_ControlResponse")
(setf (get servo_control_msg::Servo_ControlResponse :definition-)
      "uint16 angle
---
bool success
")



(provide :servo_control_msg/Servo_Control "914915d0b64fe2ea004b3cbed7ecc77f")


