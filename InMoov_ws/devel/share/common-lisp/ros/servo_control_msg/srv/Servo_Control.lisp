; Auto-generated. Do not edit!


(cl:in-package servo_control_msg-srv)


;//! \htmlinclude Servo_Control-request.msg.html

(cl:defclass <Servo_Control-request> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Servo_Control-request (<Servo_Control-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Servo_Control-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Servo_Control-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name servo_control_msg-srv:<Servo_Control-request> is deprecated: use servo_control_msg-srv:Servo_Control-request instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <Servo_Control-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader servo_control_msg-srv:angle-val is deprecated.  Use servo_control_msg-srv:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Servo_Control-request>) ostream)
  "Serializes a message object of type '<Servo_Control-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'angle)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'angle)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Servo_Control-request>) istream)
  "Deserializes a message object of type '<Servo_Control-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'angle)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'angle)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Servo_Control-request>)))
  "Returns string type for a service object of type '<Servo_Control-request>"
  "servo_control_msg/Servo_ControlRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Servo_Control-request)))
  "Returns string type for a service object of type 'Servo_Control-request"
  "servo_control_msg/Servo_ControlRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Servo_Control-request>)))
  "Returns md5sum for a message object of type '<Servo_Control-request>"
  "914915d0b64fe2ea004b3cbed7ecc77f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Servo_Control-request)))
  "Returns md5sum for a message object of type 'Servo_Control-request"
  "914915d0b64fe2ea004b3cbed7ecc77f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Servo_Control-request>)))
  "Returns full string definition for message of type '<Servo_Control-request>"
  (cl:format cl:nil "uint16 angle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Servo_Control-request)))
  "Returns full string definition for message of type 'Servo_Control-request"
  (cl:format cl:nil "uint16 angle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Servo_Control-request>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Servo_Control-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Servo_Control-request
    (cl:cons ':angle (angle msg))
))
;//! \htmlinclude Servo_Control-response.msg.html

(cl:defclass <Servo_Control-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Servo_Control-response (<Servo_Control-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Servo_Control-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Servo_Control-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name servo_control_msg-srv:<Servo_Control-response> is deprecated: use servo_control_msg-srv:Servo_Control-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <Servo_Control-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader servo_control_msg-srv:success-val is deprecated.  Use servo_control_msg-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Servo_Control-response>) ostream)
  "Serializes a message object of type '<Servo_Control-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Servo_Control-response>) istream)
  "Deserializes a message object of type '<Servo_Control-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Servo_Control-response>)))
  "Returns string type for a service object of type '<Servo_Control-response>"
  "servo_control_msg/Servo_ControlResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Servo_Control-response)))
  "Returns string type for a service object of type 'Servo_Control-response"
  "servo_control_msg/Servo_ControlResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Servo_Control-response>)))
  "Returns md5sum for a message object of type '<Servo_Control-response>"
  "914915d0b64fe2ea004b3cbed7ecc77f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Servo_Control-response)))
  "Returns md5sum for a message object of type 'Servo_Control-response"
  "914915d0b64fe2ea004b3cbed7ecc77f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Servo_Control-response>)))
  "Returns full string definition for message of type '<Servo_Control-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Servo_Control-response)))
  "Returns full string definition for message of type 'Servo_Control-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Servo_Control-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Servo_Control-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Servo_Control-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Servo_Control)))
  'Servo_Control-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Servo_Control)))
  'Servo_Control-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Servo_Control)))
  "Returns string type for a service object of type '<Servo_Control>"
  "servo_control_msg/Servo_Control")