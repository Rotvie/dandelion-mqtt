#include <DHT.h> 
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#define DHTPIN 0 //Seleccionamos el pin en el que se conectará el sensor
#define DHTTYPE DHT22 //Se selecciona el DHT22(hay otros DHT)
#define pirPin 4
#define ledPin 14
#define BUZZER 5

int val = 0;
bool motionState = false;

DHT dht(DHTPIN, DHTTYPE); //Se inicia una variable que será usada por Arduino para comunicarse con el sensor

void setup() {
  Serial.begin(9600); //Se inicia la comunicación serial 
  pinMode(ledPin, OUTPUT);
  pinMode(pirPin, INPUT);
  pinMode(BUZZER,OUTPUT);
  dht.begin(); //Se inicia el sensor
  
}

void loop() {
  float h = dht.readHumidity(); //Se lee la humedad
  float t = dht.readTemperature(); //Se lee la temperatura
  //Se imprimen las variables
  Serial.print(h);
  Serial.print(", ");
  Serial.println(t);
  delay(3000); //Se espera 3 segundos para seguir leyendo datos

  // Lee el valor de pirpin y lo guarda en val:
  val = digitalRead(pirPin);
  // Si se detecta movimiento (pirPin = HIGH), se ejecuta lo siguiente:
  if (val == HIGH) {
    digitalWrite(ledPin, HIGH); // enciende el LED.
    // Cambia el estado de motion a true (movimiento detectado):
    if (motionState == false) {
      digitalWrite(BUZZER,HIGH);
      motionState = true;
    }
  }
  // Si ningun movimiento es detectado (pirPin = LOW), se ejecuta lo siguiente:
  else {
    digitalWrite(ledPin, LOW); // Apaga el LED.
    // Cambia el estado de motion a false (no hay movimiento):
    if (motionState == true) {
      digitalWrite(BUZZER,LOW);
      motionState = false;
    }
  }
}
