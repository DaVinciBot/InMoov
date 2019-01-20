;; Auto-generated. Do not edit!


(when (boundp 'robot::test)
  (if (not (find-package "ROBOT"))
    (make-package "ROBOT"))
  (shadow 'test (find-package "ROBOT")))
(unless (find-package "ROBOT::TEST")
  (make-package "ROBOT::TEST"))

(in-package "ROS")
;;//! \htmlinclude test.msg.html


(defclass robot::test
  :super ros::object
  :slots (_a ))

(defmethod robot::test
  (:init
   (&key
    ((:a __a) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:serialization-length
   ()
   (+
    ;; int16 _a
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _a
       (write-word _a s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _a
     (setq _a (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get robot::test :md5sum-) "55dc7b156d5624062efec16350895ec2")
(setf (get robot::test :datatype-) "robot/test")
(setf (get robot::test :definition-)
      "int16 a
")



(provide :robot/test "55dc7b156d5624062efec16350895ec2")


