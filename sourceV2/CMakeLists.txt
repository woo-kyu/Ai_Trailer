cmake_minimum_required(VERSION 3.26)
project(sourceV2)

set(CMAKE_CXX_STANDARD 17)

add_executable(sourceV2 main.cpp
        DataReceptionModule.h
        MotorControlModule.h
        SteeringControlModule.h
        Utility.h)
