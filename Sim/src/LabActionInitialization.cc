
#include "LabActionInitialization.hh"
#include "LabInfo.hh" 
#include "LabPrimaryGeneratorAction.hh"
#include "LabRunAction.hh"
#include "LabSteppingAction.hh"
#include "LabStackingAction.hh"
#include "LabSteppingVerbose.hh"

LabActionInitialization::LabActionInitialization(LabInfo *info_)
 : G4VUserActionInitialization(){ 
    info = info_;
}

LabActionInitialization::~LabActionInitialization(){}

void LabActionInitialization::BuildForMaster() const{
  SetUserAction(new LabRunAction(info));
}

void LabActionInitialization::Build() const{
  SetUserAction(new LabRunAction(info));
  
  
  SetUserAction(new LabPrimaryGeneratorAction(info));
  SetUserAction(new LabSteppingAction(info)); 
  SetUserAction(new LabStackingAction(info));
 
}



G4VSteppingVerbose* LabActionInitialization::InitializeSteppingVerbose() const{
  return new LabSteppingVerbose();
}  


