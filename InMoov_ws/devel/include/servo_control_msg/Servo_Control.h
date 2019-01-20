// Generated by gencpp from file servo_control_msg/Servo_Control.msg
// DO NOT EDIT!


#ifndef SERVO_CONTROL_MSG_MESSAGE_SERVO_CONTROL_H
#define SERVO_CONTROL_MSG_MESSAGE_SERVO_CONTROL_H

#include <ros/service_traits.h>


#include <servo_control_msg/Servo_ControlRequest.h>
#include <servo_control_msg/Servo_ControlResponse.h>


namespace servo_control_msg
{

struct Servo_Control
{

typedef Servo_ControlRequest Request;
typedef Servo_ControlResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Servo_Control
} // namespace servo_control_msg


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::servo_control_msg::Servo_Control > {
  static const char* value()
  {
    return "914915d0b64fe2ea004b3cbed7ecc77f";
  }

  static const char* value(const ::servo_control_msg::Servo_Control&) { return value(); }
};

template<>
struct DataType< ::servo_control_msg::Servo_Control > {
  static const char* value()
  {
    return "servo_control_msg/Servo_Control";
  }

  static const char* value(const ::servo_control_msg::Servo_Control&) { return value(); }
};


// service_traits::MD5Sum< ::servo_control_msg::Servo_ControlRequest> should match 
// service_traits::MD5Sum< ::servo_control_msg::Servo_Control > 
template<>
struct MD5Sum< ::servo_control_msg::Servo_ControlRequest>
{
  static const char* value()
  {
    return MD5Sum< ::servo_control_msg::Servo_Control >::value();
  }
  static const char* value(const ::servo_control_msg::Servo_ControlRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::servo_control_msg::Servo_ControlRequest> should match 
// service_traits::DataType< ::servo_control_msg::Servo_Control > 
template<>
struct DataType< ::servo_control_msg::Servo_ControlRequest>
{
  static const char* value()
  {
    return DataType< ::servo_control_msg::Servo_Control >::value();
  }
  static const char* value(const ::servo_control_msg::Servo_ControlRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::servo_control_msg::Servo_ControlResponse> should match 
// service_traits::MD5Sum< ::servo_control_msg::Servo_Control > 
template<>
struct MD5Sum< ::servo_control_msg::Servo_ControlResponse>
{
  static const char* value()
  {
    return MD5Sum< ::servo_control_msg::Servo_Control >::value();
  }
  static const char* value(const ::servo_control_msg::Servo_ControlResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::servo_control_msg::Servo_ControlResponse> should match 
// service_traits::DataType< ::servo_control_msg::Servo_Control > 
template<>
struct DataType< ::servo_control_msg::Servo_ControlResponse>
{
  static const char* value()
  {
    return DataType< ::servo_control_msg::Servo_Control >::value();
  }
  static const char* value(const ::servo_control_msg::Servo_ControlResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // SERVO_CONTROL_MSG_MESSAGE_SERVO_CONTROL_H
