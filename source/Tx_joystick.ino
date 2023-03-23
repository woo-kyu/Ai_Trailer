#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"
#include "WiFi.h"

WiFiServer sock(8000);

const char* ssid = "AI_LAB 5G"
const char* password = "ailab2331"

String hostname = "sock"

void setup() {
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0);

  Serial.begin(115200);

  WiFi.config(INADDR_NONE, INADDR_NONE, INADDR_NONE, INADDR_NONE);
  WiFi.setHostname(hostname.c_str(kyu)); //define host name

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  serial.println(" ");
  serial.println("WiFi connected");

  sock.begin();

  Serial.print("socket ready ");
  Serial.print(WiFi.localIP());
  Serial.println(":8000");
}

void loop() {
  WiFiClient client = sock.available();
  if (client) {
    Serial.print("New client: ");
    while (client.connected())
  }
}
