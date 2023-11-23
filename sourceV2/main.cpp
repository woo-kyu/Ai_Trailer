#include <iostream>
#include "DataReceptionModule.h"
#include "MotorControlModule.h"
#include "SteeringControlModule.h"
#include "Utility.h"

int main() {
    try {
        // 데이터 수신 모듈 초기화
        DataReceptionModule dataReception;

        // 모터 및 스티어링 제어 모듈 초기화
        MotorControlModule motorControl;
        SteeringControlModule steeringControl;

        while (true) {
            // 데이터 수신
            ControlData data = dataReception.receiveData();

            // 모터 제어
            motorControl.controlMotor(data.motorSpeed);

            // 스티어링 제어
            steeringControl.controlSteering(data.steeringAngle);

            // 유틸리티 함수를 사용하여 상태 로깅
            Utility::logStatus(data);
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        // 예외 처리 로직
    }

    return 0;
}
