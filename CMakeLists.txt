cmake_minimum_required(VERSION 3.8...3.15)

project (Agglomerator LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Finding NeoPZ package
find_package(PZ REQUIRED)

add_executable(Test main.cpp Tools.cpp Tools.h)

target_link_libraries(Test pz)
target_include_directories(Test PUBLIC ${PZ_INCLUDE_DIRS})
