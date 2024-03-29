cmake_minimum_required(VERSION 3.16)

project(GuardianCruise VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(Qt6 6.2 COMPONENTS Quick REQUIRED WebEngineQuick Positioning)

qt_add_executable(appGuardianCruise
    main.cpp
)

qt_add_qml_module(appGuardianCruise
    URI GuardianCruise
    VERSION 1.0
    QML_FILES main.qml
    RESOURCES bgAsset/bgAsset.qrc
    QML_FILES QMLfiles/home.qml
    RESOURCES fonts/fonts.qrc
    RESOURCES Images/images.qrc
    RESOURCES APIs/APIs.qrc
    QML_FILES QMLfiles/crash.qml
    QML_FILES QMLfiles/graphs.qml
    SOURCES videoreceiver.h videoreceiver.cpp
)

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
set_target_properties(appGuardianCruise PROPERTIES
#    MACOSX_BUNDLE_GUI_IDENTIFIER com.example.appGuardianCruise
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

target_link_libraries(appGuardianCruise
    PRIVATE Qt6::Quick
    PRIVATE Qt6::WebEngineQuick
    PRIVATE Qt6::Positioning)

include(GNUInstallDirs)
install(TARGETS appGuardianCruise
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
