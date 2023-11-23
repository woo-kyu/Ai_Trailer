// DataReceptionModule.h
#ifndef DATARECEPTIONMODULE_H
#define DATARECEPTIONMODULE_H

struct ControlData {
    float motorSpeed;
    float steeringAngle;
};

class DataReceptionModule {
public:
    ControlData receiveData();
};

#endif
