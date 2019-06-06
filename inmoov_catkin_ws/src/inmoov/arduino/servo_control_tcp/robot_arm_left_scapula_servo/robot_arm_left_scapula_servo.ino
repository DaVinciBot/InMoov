#include <SPI.h>
#include <Ethernet.h>

#include <Servo.h>

#define ROSSERIAL_ARDUINO_TCP

#include <ros.h>
#include <std_msgs/UInt8.h>

/****************************************/
/*************** CONFIG *****************/
/****************************************/

#define SERVO_PIN 9
#define SERVO_ANGLE_MAX 150
#define SERVO_ANGLE_MIN 0

#define TOPIC_NAME "/robot/arm/left/scapula/servo/angle"

// TCP/IP settings
IPAddress ip(10, 42, 0, 3);
uint16_t serverPort = 11412;
byte mac[] = { 0xFF, 0xFF, 0xFF, 0xFF, 0xFB, 0xFF };

/****************************************/
/***************** END ******************/
/****************************************/


/************* DO NOT TOUCH *************/

ros::NodeHandle  nh;

Servo servo_;
uint8_t angle_;

// Server settings
IPAddress server(10, 42, 0, 232);

void onServoMsg( const std_msgs::UInt8& msg){
  angle_ = msg.data;
  
  if( angle_ > SERVO_ANGLE_MAX ) angle_ = SERVO_ANGLE_MAX;
  if( angle_ < SERVO_ANGLE_MIN ) angle_ = SERVO_ANGLE_MIN;

  servo_.write(angle_);
}

ros::Subscriber<std_msgs::UInt8> sub(TOPIC_NAME, &onServoMsg );

void setup()
{
  Ethernet.begin(mac, ip);
  delay(1000);

  servo_.attach(SERVO_PIN);
  
  nh.getHardware()->setConnection(server, serverPort);
  nh.initNode();
  
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
