#define BUTTON_PIN           3

enum RESULTS{
  RES_OK,
  RES_NONE,
  RES_ERROR
};

boolean button_flag = 0;
  
void setup() {
  delay(1000);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(115200); // Установка скорости общения 
                        //по последовательному порту
  

  Serial.println("AT+ADDRESS=1");
  receive();
  Serial.println("AT+NETWORKID=1");
  receive(); 
  Serial.println("AT+BAND=868500000");
  receive();
  Serial.println("AT+PARAMETER=10,7,1,7");
  receive();
  
  blink(2); // Конфигурация успешна  
}

void loop() { 
  boolean button = !digitalRead(BUTTON_PIN);

  if (button == 1 && button_flag == 0)
  {
    button_flag = 1;
    Serial.println("AT+SEND=2,5,HELLO");
    receive();
    blink(2);
  }
  if (button == 0 && button_flag == 1)
  {
    button_flag = 0;
  }
}

void receive(){
  String answer = Serial.readString(); 
  if(get_result(answer) != RES_OK){
    deinit(); 
  }
}

uint8_t get_result(String str){
  if (str == "+OK\r\n"){
    return RES_OK;
  }
  else if (str == ""){
    return RES_NONE;
  }
  else{
    return RES_ERROR;
  }
}

void deinit(){
  blink(5);
  while(true){
    // end of program
  }
}

void blink(uint8_t  cnt) {
  for(uint8_t i = 0; i < cnt; i++){
    digitalWrite(LED_BUILTIN, HIGH);   
    delay(250);                       
    digitalWrite(LED_BUILTIN, LOW); 
    delay(50);    
  }
  delay(200);
}
