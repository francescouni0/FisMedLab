#----------------------------------------------------------------------------
# Setup the project
cmake_minimum_required(VERSION 3.16...3.21)
project(LAB2023)

#----------------------------------------------------------------------------
# Find Geant4 package, activating all available UI and Vis drivers by default
# You can set WITH_GEANT4_UIVIS to OFF via the command line or ccmake/cmake-gui
# to build a batch mode only executable
#
#set(Geant4_DIR "/home/user/Geant4/geant4-v11.1.1-install/lib/Geant4-11.1.1" CACHE PATH "Geant4 directory override" FORCE)
set(Geant4_DIR "//home/francesco/software/geant4/geant4-v11.1.1-install/lib/Geant4-11.1.1" CACHE PATH "Geant4 directory override" FORCE)

option(WITH_GEANT4_UIVIS "Build example with Geant4 UI and Vis drivers" ON)
if(WITH_GEANT4_UIVIS)
  find_package(Geant4 REQUIRED ui_all vis_all)
else()
  find_package(Geant4 REQUIRED)
endif()

#----------------------------------------------------------------------------
# Setup Geant4 include directories and compile definitions
#
include(${Geant4_USE_FILE})

#----------------------------------------------------------------------------
# Locate sources and headers for this project
#
include_directories(${PROJECT_SOURCE_DIR}/include 
                    ${Geant4_INCLUDE_DIR})
file(GLOB sources ${PROJECT_SOURCE_DIR}/src/*.cc)
file(GLOB headers ${PROJECT_SOURCE_DIR}/include/*.hh)

#----------------------------------------------------------------------------
# Add the executable, and link it to the Geant4 libraries
#
add_executable(LAB2023 LAB2023.cc ${sources} ${headers})
target_link_libraries(LAB2023 ${Geant4_LIBRARIES} tbb)

#----------------------------------------------------------------------------
# Copy all scripts to the build directory, i.e. the directory in which we
# build LAB2023. This is so that we can run the executable directly because it
# relies on these scripts being in the current working directory.
#
set(LAB2023_SCRIPTS
    input.mac
    init_vis.mac
    vis.mac
  )

foreach(_script ${LAB2023_SCRIPTS})
  configure_file(
    ${PROJECT_SOURCE_DIR}/${_script}
    ${PROJECT_BINARY_DIR}/${_script}
    COPYONLY
    )
endforeach()

#----------------------------------------------------------------------------
# Install the executable to 'bin' directory under CMAKE_INSTALL_PREFIX
#
install(TARGETS LAB2023 DESTINATION bin)

