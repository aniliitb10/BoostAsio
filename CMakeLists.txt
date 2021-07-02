cmake_minimum_required(VERSION 3.19)
project(BoostAsio)

set(CMAKE_CXX_STANDARD 17)

add_executable(async_echo_server async_tcp_echo_server.cpp)
target_link_libraries(async_echo_server pthread)
