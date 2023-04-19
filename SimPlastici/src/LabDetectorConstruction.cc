#include "LabDetectorConstruction.hh"

#include "G4RunManager.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"
#include "G4PhysicalConstants.hh"
#include "G4UnitsTable.hh"
#include "LabInfo.hh" 
#include "G4UserLimits.hh"


LabDetectorConstruction::LabDetectorConstruction(LabInfo *info_)
: G4VUserDetectorConstruction(){
    info = info_; 
}


LabDetectorConstruction::~LabDetectorConstruction(){
}


G4VPhysicalVolume* LabDetectorConstruction::Construct(){

    // Boolean variable to switch on/off the check of volume overlaps
    checkOverlaps = true;
   
    // Call functions to construct geometry
    defineMaterials();
    constructMaterialPropertiesTable();
    constructWorld();
    constructScintillator();
    //constructGrease();
    //constructSiPM();
    //constructOpticalSurfaces();
    return physWorld;
  
}


void LabDetectorConstruction::defineMaterials() {

    G4NistManager* nist = G4NistManager::Instance();
    
    // check the following website for all the elements and materials available in the G4 database:
    // http://geant4-userdoc.web.cern.ch/geant4-userdoc/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)
    
    // NIST Elements (required for PVT)
    C  = nist->FindOrBuildElement("C");
    H  = nist->FindOrBuildElement("H"); 
    O  = nist->FindOrBuildElement("O");
    Si = nist->FindOrBuildElement("Si");
    Y = nist->FindOrBuildElement("Y");
    Lu = nist->FindOrBuildElement("Lu");
    
    // NIST Materials
    Air      = nist->FindOrBuildMaterial("G4_AIR");
   // note the difference with element Si: the material Si can be assigned to a volume while the element cannot
  
    // EJ200
    EJ200 = new G4Material("EJ200", 1.023*g/cm3, 2); //eljen technology 1.023
    G4int natoms;
    EJ200->AddElement(H, natoms = 524); // su G4 nist database
    EJ200->AddElement(C, natoms = 475); 
    
    // Grease
    Grease = new G4Material("BC-630", 1.06*g/cm3, 4); // density of BC-630, composition of Polydimethylsiloxane (PDMS) su wiki
    Grease->AddElement(C,2);
    Grease->AddElement(H,6);
    Grease->AddElement(O,1); 
    Grease->AddElement(Si,1);

     //LYSO
    LYSO = new G4Material("LYSO", 7.1*g/cm3, 4);
    LYSO->AddElement(Lu, 71.43*perCent);
    LYSO->AddElement(Y,  4.76*perCent);
    LYSO->AddElement(Si, 6.81*perCent);
    LYSO->AddElement(O,  17*perCent);

}


void LabDetectorConstruction::constructMaterialPropertiesTable() {
  
    G4double photon_energies[] = {info->enRange[0]*eV, info->enRange[1]*eV};
    const G4int num_ph_en = sizeof(photon_energies)/sizeof(G4double);

  //    if (1){
  //    G4cout << G4endl;
  //    G4cout <<"Internal units: " << photon_energies[0] << G4endl;
  //    G4cout <<"Best units: " << G4BestUnit(photon_energies[0],"Energy") << G4endl;
  //   G4cout << " " <<photon_energies[0]*eV << "*eV" << G4endl;
  //    G4cout << " " <<photon_energies[0]/eV << "/eV" << G4endl;
  //    G4cout << " " <<photon_energies[0]*keV << "*keV" << G4endl;
  //    G4cout << " " <<photon_energies[0]/keV << "/keV" << G4endl;
  //    G4cout << G4endl;
  //    exit(EXIT_FAILURE);

    //}
 
    // Air
    G4double air_rindex[]  = {1.0, 1.0};
    G4MaterialPropertiesTable* air_MPT = new G4MaterialPropertiesTable();
    air_MPT->AddProperty("RINDEX", photon_energies, air_rindex, num_ph_en);
    Air->SetMaterialPropertiesTable(air_MPT);
    
    // Grease
    G4double grease_rindex[] = {1.55, 1.55}; 
    G4MaterialPropertiesTable* grease_MPT = new G4MaterialPropertiesTable();
    grease_MPT->AddProperty("RINDEX", photon_energies, grease_rindex, num_ph_en);
    Grease->SetMaterialPropertiesTable(grease_MPT);
    
    // EJ200
    G4double ej200_rindex [] = {1.58, 1.58}; 
    G4double ej200_absLength[] = {380.*cm, 380.*cm};
    G4MaterialPropertiesTable* ej200_MPT = new G4MaterialPropertiesTable();
    ej200_MPT->AddProperty("RINDEX", photon_energies, ej200_rindex, num_ph_en);       
    ej200_MPT->AddProperty("ABSLENGTH", photon_energies, ej200_absLength, num_ph_en);
    EJ200->SetMaterialPropertiesTable(ej200_MPT);
  
    G4double enPlastic[] = {2.40*eV,3.10*eV};
    G4double emSpectrumEJ200[] = {0.5, 0.5};
    const G4int nrEJ200 = sizeof(enPlastic)/sizeof(G4double);
    assert(sizeof(enPlastic) == sizeof(emSpectrumEJ200));
    ej200_MPT->AddProperty("SCINTILLATIONCOMPONENT1", enPlastic, emSpectrumEJ200, nrEJ200);    
    ej200_MPT->AddConstProperty("SCINTILLATIONYIELD", 10./keV); 
    ej200_MPT->AddConstProperty("RESOLUTIONSCALE",    1);
    ej200_MPT->AddConstProperty("SCINTILLATIONTIMECONSTANT1",   2.1*ns);
    ej200_MPT->AddConstProperty("SCINTILLATIONRISETIME1", 0.9*ns);   
    //EJ200->GetIonisation()->SetBirksConstant(3.00e-3*cm/MeV); // <------------- UPDATE



    // print tables of material properties
    G4cout << "----- Material properties table printed by DetectorConstruction: -----" << G4endl;
    G4cout << *(G4Material::GetMaterialTable()) << G4endl;
    G4cout << "----- End on material properties table -----" << G4endl;
    G4cout << G4endl;

   

        
}

void LabDetectorConstruction::constructWorld() {
 
    solidWorld = new G4Box("World", 0.5*info->worldSize[0]*mm, 0.5*info->worldSize[1]*mm, 0.5*info->worldSize[2]*mm);  
    logicWorld = new G4LogicalVolume(solidWorld, Air, "World");            
    physWorld  = new G4PVPlacement(0, G4ThreeVector(), logicWorld, "World", 0, false, 0, checkOverlaps);        

}



void LabDetectorConstruction::constructScintillator() {
  
    solidScint = new G4Box("Scintillator", 0.5*info->scintSize[0]*mm, 0.5*info->scintSize[1]*mm, 0.5*info->scintSize[2]*mm);  
    logicScint = new G4LogicalVolume(solidScint, LYSO, "Scintillator");            
    physScint  = new G4PVPlacement(0, G4ThreeVector(info->scintPos[0]*mm, info->scintPos[1]*mm, info->scintPos[2]*mm), logicScint, "Scintillator", logicWorld, false, 0, checkOverlaps);  
    
    fStepLimit = new G4UserLimits(info->stepLimiter);
    logicScint->SetUserLimits(fStepLimit);
    
}



void LabDetectorConstruction::constructGrease() {
  
    //placed in world
  
    solidGrease1 = new G4Box("Grease1", 0.5*info->scintSize[0]*mm, 0.5*info->scintSize[1]*mm, 0.5*info->greaseThickness*um);  
    logicGrease1 = new G4LogicalVolume(solidGrease1, Grease, "Grease1");            
    physGrease1  = new G4PVPlacement(0, G4ThreeVector(info->scintPos[0]*mm, info->scintPos[1]*mm, info->scintPos[2]*mm + 0.5*info->scintSize[2]*mm + 0.5*info->greaseThickness*um), logicGrease1, "Grease1", logicWorld, false, 0, checkOverlaps);  
    
    fStepLimit = new G4UserLimits(info->stepLimiter);
    logicGrease1->SetUserLimits(fStepLimit);
    
    solidGrease2 = new G4Box("Grease2", 0.5*info->scintSize[0]*mm, 0.5*info->scintSize[1]*mm, 0.5*info->greaseThickness*um);
    logicGrease2 = new G4LogicalVolume(solidGrease2, Grease, "Grease2");
    physGrease2  = new G4PVPlacement(0, G4ThreeVector(info->scintPos[0]*mm, info->scintPos[1]*mm, -(info->scintPos[2]*mm + 0.5*info->scintSize[2]*mm + 0.5*info->greaseThickness*um)), logicGrease2, "Grease2", logicWorld, false, 0, checkOverlaps);
    
    logicGrease2->SetUserLimits(fStepLimit);
}


void LabDetectorConstruction::constructSiPM() { // check rindex! <-----------------------------
  
    solidSiPM1 = new G4Box("SiPM1", 0.5*info->scintSize[0]*mm, 0.5*info->scintSize[1]*mm, 0.5*info->greaseThickness*um);  
    logicSiPM1 = new G4LogicalVolume(solidSiPM1, Air, "SiPM1");            
    physSiPM1  = new G4PVPlacement(0, G4ThreeVector(info->scintPos[0]*mm, info->scintPos[1]*mm, +(info->scintPos[2]*mm + 0.5*info->scintSize[2]*mm + info->greaseThickness*um + 0.5*info->greaseThickness*um)), logicSiPM1, "SiPM1", logicWorld, false, 0, checkOverlaps);  
    
    fStepLimit = new G4UserLimits(info->stepLimiter);
    logicSiPM1->SetUserLimits(fStepLimit);
    
    solidSiPM2 = new G4Box("SiPM2", 0.5*info->scintSize[0]*mm, 0.5*info->scintSize[1]*mm, 0.5*info->greaseThickness*um);
    logicSiPM2 = new G4LogicalVolume(solidSiPM2, Air, "SiPM2");
    physSiPM2  = new G4PVPlacement(0, G4ThreeVector(info->scintPos[0]*mm, info->scintPos[1]*mm, -(info->scintPos[2]*mm + 0.5*info->scintSize[2]*mm + info->greaseThickness*um + 0.5*info->greaseThickness*um)), logicSiPM2, "SiPM2", logicWorld, false, 0, checkOverlaps);
    
    logicSiPM2->SetUserLimits(fStepLimit);
}

G4SurfaceType getEnumSurfaceType(std::string input){
   if (input == "dielectric_metal")
    return dielectric_metal;
   else if (input == "dielectric_dielectric")
     return dielectric_dielectric;
   else if (input == "dielectric_LUTDAVIS")
     return dielectric_LUTDAVIS;
   else {
        G4cerr << "Error in LabDetectorConstruction: G4OpticalSurface->SetType(undefined)" << G4endl;
        exit(EXIT_FAILURE);
    }
 }

G4OpticalSurfaceModel getEnumSurfaceModel(std::string input){
  
   if (input == "unified")
    return unified;
   else if (input == "glisur")
     return glisur;
   else if (input == "DAVIS")
     return DAVIS;
   else {
        G4cerr << "Error in LabDetectorConstruction: G4OpticalSurface->SetModel(undefined)" << G4endl;
        exit(EXIT_FAILURE);
    }
 }
 
G4OpticalSurfaceFinish getEnumSurfaceFinish(std::string input){
  
   if (input == "polished")
    return polished;
   else if (input == "polishedfrontpainted")
     return polishedfrontpainted;
   else if (input == "polishedbackpainted")
     return polishedbackpainted;
   else if (input == "ground")
     return ground;
   else if (input == "groundfrontpainted")
     return groundfrontpainted;
   else if (input == "groundbackpainted")
     return groundbackpainted;
   else if (input == "PolishedESRGrease_LUT")
     return PolishedESRGrease_LUT;
   else if (input == "PolishedESR_LUT")
     return PolishedESR_LUT;
   else if (input == "Polished_LUT")
     return Polished_LUT;
   else if (input == "Rough_LUT")
     return Rough_LUT;
   else if (input == "RoughTeflon_LUT")
     return RoughTeflon_LUT;
   else if (input == "Detector_LUT")
     return Detector_LUT;
   else {
        G4cerr << "Error in LabDetectorConstruction: G4OpticalSurface->SetFinish(undefined)" << G4endl;
        exit(EXIT_FAILURE);
    }
 } 
 
void LabDetectorConstruction::constructOpticalSurfaces() {
  
   
    // ************ Scintillator to Lateral Wrapping (4 sides) ************ 

    ScintToLateralWrapping = new G4OpticalSurface("ScintToLateralWrapping");
    
    new G4LogicalBorderSurface("ScintToLateralWrapping", physScint, physWorld, ScintToLateralWrapping);

    ScintToLateralWrapping->SetType( getEnumSurfaceType(info->scintToLateralWrappingType) );
    ScintToLateralWrapping->SetModel(getEnumSurfaceModel(info->scintToLateralWrappingModel) );
    ScintToLateralWrapping->SetFinish(getEnumSurfaceFinish(info->scintToLateralWrappingFinish) );
    
    if (info->scintToLateralWrappingFinish == "polishedbackpainted" || info->scintToLateralWrappingFinish == "groundbackpainted")  { 
      G4double sigma_alpha = 0.0;
      ScintToLateralWrapping->SetSigmaAlpha(sigma_alpha);
    }
    
    G4MaterialPropertiesTable* WrappingProperty = new G4MaterialPropertiesTable();
    G4double en_wrap[] = {info->enRange[0]*eV, info->enRange[1]*eV};
    const G4int n_w = sizeof(en_wrap)/sizeof(G4double);
    G4double reflectivity_wrap[] = {info->reflectivityLateral, info->reflectivityLateral};
    assert(sizeof(reflectivity_wrap) == sizeof(en_wrap));
    WrappingProperty->AddProperty("REFLECTIVITY", en_wrap, reflectivity_wrap, n_w);
    ScintToLateralWrapping->SetMaterialPropertiesTable(WrappingProperty);
    
    // ************ Scintillator to Grease ************ 
    
    ScintToGrease = new G4OpticalSurface("ScintToGrease");
    
    ScintToGrease->SetType( getEnumSurfaceType(info->scintToGreaseType) );
    ScintToGrease->SetModel(getEnumSurfaceModel(info->scintToGreaseModel) );
    ScintToGrease->SetFinish(getEnumSurfaceFinish(info->scintToGreaseFinish) );
    if (info->scintToGreaseFinish == "polishedbackpainted" || info->scintToGreaseFinish == "groundbackpainted")  { 
      G4double sigma_alpha = 0.0;
      ScintToGrease->SetSigmaAlpha(sigma_alpha);
    }
    
    new G4LogicalBorderSurface("ScintToGrease1", physScint, physGrease1, ScintToGrease);
    new G4LogicalBorderSurface("ScintToGrease2", physScint, physGrease2, ScintToGrease);

    // ************ Grease to Scintillator ************ 
    
    GreaseToScint = new G4OpticalSurface("GreaseToScint");
    
    GreaseToScint->SetType( getEnumSurfaceType(info->greaseToScintType) );
    GreaseToScint->SetModel(getEnumSurfaceModel(info->greaseToScintModel) );
    GreaseToScint->SetFinish(getEnumSurfaceFinish(info->greaseToScintFinish) );
    if (info->greaseToScintFinish == "polishedbackpainted" || info->greaseToScintFinish == "groundbackpainted")  { 
      G4double sigma_alpha = 0.0;
      GreaseToScint->SetSigmaAlpha(sigma_alpha);
    }
    
    new G4LogicalBorderSurface("GreaseToScint1", physGrease1, physScint, GreaseToScint);
    new G4LogicalBorderSurface("GreaseToScint2", physGrease2, physScint, GreaseToScint);
    
    // ************ Grease to Detector ************ 
    
    GreaseToSiPM = new G4OpticalSurface("GreaseToSiPM");
    
    GreaseToSiPM->SetType( getEnumSurfaceType(info->greaseToSiPMType) );
    GreaseToSiPM->SetModel(getEnumSurfaceModel(info->greaseToSiPMModel) );
    GreaseToSiPM->SetFinish(getEnumSurfaceFinish(info->greaseToSiPMFinish) );
    if (info->greaseToSiPMFinish == "polishedbackpainted" || info->greaseToSiPMFinish == "groundbackpainted")  { 
      G4double sigma_alpha = 0.0;
      GreaseToSiPM->SetSigmaAlpha(sigma_alpha);
    }
    
    new G4LogicalBorderSurface("GreaseToSiPM1", physGrease1, physSiPM1, GreaseToSiPM);
    new G4LogicalBorderSurface("GreaseToSiPM2", physGrease2, physSiPM2, GreaseToSiPM);
    
    // This step is needed so that the detector is recognized as sensitive
    // See SteppingAction
    
    G4MaterialPropertiesTable* ScintSiPMProperty = new G4MaterialPropertiesTable();
    
    G4double pp[] = {info->enRange[0]*eV, info->enRange[1]*eV};
    const G4int num = sizeof(pp)/sizeof(G4double);
    
    G4double reflectivity[] = {0., 0.};
    assert(sizeof(reflectivity) == sizeof(pp));
    
    G4double efficiency[] = {1.00, 1.00};
    assert(sizeof(efficiency) == sizeof(pp));
    
    ScintSiPMProperty->AddProperty("REFLECTIVITY", pp, reflectivity, num);
    ScintSiPMProperty->AddProperty("EFFICIENCY",   pp, efficiency,   num);
    
    GreaseToSiPM->SetMaterialPropertiesTable(ScintSiPMProperty);
    
    // Settings for all black surfaces (in case any photon is reflected)
    G4MaterialPropertiesTable* BlackSurfaceMPT = new G4MaterialPropertiesTable();
    G4double en_black[] = {info->enRange[0]*eV, info->enRange[1]*eV};
    const G4int n_black = sizeof(en_black)/sizeof(G4double);
    G4double reflectivity_black[] = {0.0, 0.0};
    assert(sizeof(reflectivity_black) == sizeof(en_black));
    G4double efficiency_black[] = {0.0, 0.0};
    assert(sizeof(efficiency_black) == sizeof(en_black));
    BlackSurfaceMPT->AddProperty("REFLECTIVITY", en_black, reflectivity_black, n_black);
    BlackSurfaceMPT->AddProperty("EFFICIENCY",   en_black, efficiency_black,   n_black);
    
    // ************ Wrapping to Scintillator ************ 
    WrapToScint = new G4OpticalSurface("WrapToScint");
    WrapToScint->SetMaterialPropertiesTable(BlackSurfaceMPT);
    new G4LogicalBorderSurface("WrapToScint", physWorld, physScint, WrapToScint);
    
    // ************ Detector to Grease ************ 
    SiPMToGrease = new G4OpticalSurface("SiPMToGrease");
    SiPMToGrease->SetMaterialPropertiesTable(BlackSurfaceMPT);
    new G4LogicalBorderSurface("SiPMToGrease1", physSiPM1, physGrease1, SiPMToGrease);
    new G4LogicalBorderSurface("SiPMToGrease2", physSiPM2, physGrease2, SiPMToGrease);
    
   
}

