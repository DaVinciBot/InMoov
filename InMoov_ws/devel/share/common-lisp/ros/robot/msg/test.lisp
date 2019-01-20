; Auto-generated. Do not edit!


(cl:in-package robot-msg)


;//! \htmlinclude test.msg.html

(cl:defclass <test> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:fixnum
    :initform 0))
)

(cl:defclass test (<test>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <test>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'test)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot-msg:<test> is deprecated: use robot-msg:test instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <test>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot-msg:a-val is deprecated.  Use robot-msg:a instead.")
  (a m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <test>) ostream)
  "Serializes a message object of type '<test>"
  (cl:let* ((signed (cl:slot-value msg 'a)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <test>) istream)
  "Deserializes a message object of type '<test>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'a) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<test>)))
  "Returns string type for a message object of type '<test>"
  "robot/test")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'test)))
  "Returns string type for a message object of type 'test"
  "robot/test")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<test>)))
  "Returns md5sum for a message object of type '<test>"
  "55dc7b156d5624062efec16350895ec2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'test)))
  "Returns md5sum for a message object of type 'test"
  "55dc7b156d5624062efec16350895ec2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<test>)))
  "Returns full string definition for message of type '<test>"
  (cl:format cl:nil "int16 a~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'test)))
  "Returns full string definition for message of type 'test"
  (cl:format cl:nil "int16 a~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <test>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <test>))
  "Converts a ROS message object to a list"
  (cl:list 'test
    (cl:cons ':a (a msg))
))
