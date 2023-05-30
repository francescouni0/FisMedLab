// EC (12/01/2022)
#ifndef LabDetectorConstruction_h
#define LabDetectorConstruction_h 1

#include "globals.hh"
#include "G4VUserDetectorConstruction.hh"
#include "LabInfo.hh" 

#include "G4NistManager.hh"
#include "G4Material.hh"
#include "G4Element.hh"
#include "G4MaterialTable.hh"
#include "G4MaterialPropertiesTable.hh"
#include "G4LogicalBorderSurface.hh"
#include "G4LogicalSkinSurface.hh"
#include "G4OpticalSurface.hh"
#include "G4Box.hh"
#include "G4Trd.hh"
#include "G4LogicalVolume.hh"

class G4UserLimits;
class G4VPhysicalVolume;
class G4LogicalVolume;

class LabDetectorConstruction : public G4VUserDetectorConstruction
{
  public:
    LabDetectorConstruction(LabInfo* info);
    virtual ~LabDetectorConstruction();
  public:
    virtual G4VPhysicalVolume* Construct();
    
  private:
      
    void defineMaterials();
    void constructMaterialPropertiesTable();
    void constructWorld();

    void constructScintillator();
    void constructGrease();
    void constructSiPM();
    void constructOpticalSurfaces();
    
    G4bool checkOverlaps;
    
    G4Element *C, *H, *O, *Si;

    G4Material *Air, *EJ200, *Grease;
     
    G4Box *solidWorld, *solidScint, *solidGrease1, *solidGrease2, *solidSiPM1, *solidSiPM2, *solidScint1, *solidGrease3, *solidGrease4, *solidSiPM3, *solidSiPM4; 
    
    G4LogicalVolume  *logicWorld, *logicScint, *logicGrease1, *logicGrease2, *logicSiPM1, *logicSiPM2,*logicScint1, *logicGrease3, *logicGrease4, *logicSiPM3, *logicSiPM4;

    G4VPhysicalVolume *physWorld, *physScint, *physGrease1, *physGrease2, *physSiPM1, *physSiPM2, *physScint1, *physGrease3, *physGrease4, *physSiPM3, *physSiPM4;
    
    G4OpticalSurface *ScintToLateralWrapping, *ScintToGrease, *GreaseToScint, *GreaseToSiPM, *SiPMToGrease, *WrapToScint;
    
    G4UserLimits* fStepLimit;            // pointer to user step limits

    LabInfo *info;
};





#endif

