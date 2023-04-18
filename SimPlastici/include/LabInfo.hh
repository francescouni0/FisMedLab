/*
 * file:   LabInfo.hh
 * author: EC
 * date:   2017
 */

#ifndef LabInfo_h
#define LabInfo_h 1

#include "stdio.h"
#include "stdlib.h"
#include <atomic>

#include "G4Types.hh"
#include "G4ThreeVector.hh"

class LabInfo {

public:

    LabInfo();
    virtual ~LabInfo();

    void dump();

    G4String summaryFileName;
    
    G4int seed;
    G4int optPhysVerb;
//     G4int verbose;
    
    G4double stepLimiter;
    
    // Dimensions for detector construction
    G4double worldSize[3];
    G4double scintSize[3];
    
    // Positions for detector construction
    G4double scintPos[3];
    
    G4double enRange[2];
    
    G4double greaseThickness;
    
    G4String scintToLateralWrappingType, scintToLateralWrappingModel, scintToLateralWrappingFinish;
    G4String scintToGreaseType, scintToGreaseModel, scintToGreaseFinish;
    G4String greaseToScintType, greaseToScintModel, greaseToScintFinish;
    G4String greaseToSiPMType, greaseToSiPMModel, greaseToSiPMFinish;
    G4double reflectivityLateral;
    
    // particle creation
    G4int numOfEvents;
    
    // For output by primary generator action
    G4String particleName;    
    G4double beamEnergy;
    G4double beamPos[3];
    G4double beamDirection[3];
    G4int event_id;
    
    // For run action
    G4double timer[3];
    
    // For stepping action
    std::atomic<G4int> gammaIntCounter;
    std::atomic<G4int> detectedPhotonsCounter;
    
    // Optical interactions counters
    G4int FresnelRefraction, FresnelReflection, TotalInternalReflection, LambertianReflection, LobeReflection, SpikeReflection, BackScattering, Absorption, Detection1, Detection2, NotAtBoundary, SameMaterial, /*StepTooSmall,*/ NoRINDEX;
    
    //////////////////////////////////////////////////////////////////////
    
    
//     G4int trackID;
//     G4int opticalLastStep;
// 
//     G4int typeOfParticle;
//     G4int creationTimeCounter;
//     static const int creationTimeSize = 1000;
//     G4double creationTime[creationTimeSize];
//     
//     
//     G4double optPhStartAngle[3];
//     
//     // Constants for detector construction
//     G4double wrappingLayerThick, wrappingRindex;
//     G4double scintRindex[2];
//     G4double scintAbsLength[2];
//     G4double scintScattLength[2];
//     G4double scintResolScale;
//     G4double scintRiseTime;
//     G4double scintFastDecayTime;
//     G4double scintLightYield;
//     G4double reflectivityLateral;
//     G4double lambdaRange[2];
//     
//     
//     G4double CaloRindex[2], CaloDim[5];
//     G4int wrap;
//     
//     G4double greaseThickness, greaseRindex;
//     
//     
//     G4double siPMthick;
//     
//     
//     // Optical interfaces;
//     G4String scintToEntranceType, scintToEntranceModel, scintToEntranceFinish;
//     G4String entranceToScintType, entranceToScintModel, entranceToScintFinish;
//     G4String wrappingMaterial;
//     
//     G4String lateralWrapToScintType, lateralWrapToScintModel, lateralWrapToScintFinish;
//     G4String scintToDetectorType,    scintToDetectorModel,    scintToDetectorFinish;
//     G4String detectorToScintType,    detectorToScintModel,    detectorToScintFinish;
//     
//     // Optical interactions counters
//     G4int PolishedTyvekAirReflection, FresnelRefraction, FresnelReflection, TotalInternalReflection, LambertianReflection, LobeReflection, SpikeReflection, BackScattering, Absorption, Detection, NotAtBoundary, SameMaterial, /*StepTooSmall,*/ NoRINDEX;
    
    
};

#endif

